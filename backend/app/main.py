from fastapi import FastAPI

from backend.app.routes.system import router as system_router

app = FastAPI(
    title="TwinOS API",
    description="AI Powered Personal System Digital Twin",
    version="1.0.0"
)

app.include_router(system_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to TwinOS 🚀",
        "status": "Running",
        "version": "1.0.0"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }