from fastapi import FastAPI
from src.api.configuration import configure_db, configure_routes

def create_app():
    app = FastAPI()

    # Inicialisa rotas
    configure_routes(app)

    # inicializar db/tortoise
    configure_db(app)
    return app


app = create_app()

@app.get("/")
async def home():
    return {"status":"ok"}

