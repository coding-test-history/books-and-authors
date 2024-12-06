from fastapi import FastAPI
from config.connection import engine, Base
from app.routes.authors import router  # Import router yang akan digunakan
from config.app import settings
from config.routes import routes
from database.seeders.seeder import run_seeders
import uvicorn

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESC,
    version=settings.APP_VERSION,
)

# Buat tabel di database (jika belum ada)
Base.metadata.create_all(bind=engine)

# Register router
routes(app)

# Running seeder
run_seeders()

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to " + settings.APP_NAME}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_RELOAD,
    )
