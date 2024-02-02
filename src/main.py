from urllib.parse import urljoin

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from src.api.routers.projects import router as project_router


app = FastAPI()
AVAILABLE_PATHS = ("projects",)


@app.get("/")
async def home(request: Request):
    return JSONResponse(
        status_code=200,
        content={path: urljoin(str(request.url), path) for path in AVAILABLE_PATHS},
    )


app.include_router(router=project_router)
