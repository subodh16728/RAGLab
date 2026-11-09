from fastapi import FastAPI, HTTPException
from app.database import get_db_connection

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

@app.get("/health/database")
def database_health_check():
    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        connection.close()

        return {
            "status": "healthy",
            "database": "connected",
            "result": result[0]
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Database connection failed: {str(error)}"
        )