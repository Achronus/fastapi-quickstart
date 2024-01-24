import os

from . import FRONTEND_DIR, templates
from .routers import items, users

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/static", StaticFiles(directory=os.path.join(FRONTEND_DIR, 'public')), name="static")

app.include_router(users.router)
app.include_router(items.router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name='index.html', context={})
