from fastapi import FastAPI

app = FastAPI(
    title = "RAGLab API",
    description = "Backend API for RAGLab application",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "message": "RAGLab backend is running successfully"
    }