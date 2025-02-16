from fastapi import FastAPI

from app.middleware.app_middleware import add_middlewares
from app.routers import auth_routes, rssplayground_routes

app = FastAPI()

add_middlewares(app)

app.include_router(auth_routes.router)
app.include_router(rssplayground_routes.router)


@app.get("/")
async def root() -> dict:
    return {
        "message": "Meltwater Feeds Revamped by Master Tyrone - Developing for Production"
    }
