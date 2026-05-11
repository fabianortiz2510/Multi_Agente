"""FastAPI server for the multi-agent assistant."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.graph import assistant_graph

app = FastAPI(
    title="Multi-Agent Assistant",
    description="REST API for the LangGraph multi-agent assistant",
    version="1.0.0"
)


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str


class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "Multi-Agent Assistant API is running 🚀"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Send a message to the multi-agent assistant.
    
    Routes the message to the appropriate agent:
    - Weather Agent: for climate/weather queries
    - Crypto Agent: for cryptocurrency prices
    - Geocoding Agent: for location queries
    - RAG Agent: for document-based queries (default)
    """
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        result = assistant_graph.invoke({"input": request.message})
        return ChatResponse(response=result["output"])
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    """Health check with detailed status."""
    return {
        "status": "healthy",
        "service": "Multi-Agent Assistant",
        "version": "1.0.0"
    }
