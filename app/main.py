from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()

# Monter le dossier des fichiers téléversés pour qu'ils soient accessibles
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Inclure les routes
app.include_router(router)
