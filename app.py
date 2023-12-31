from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), 'static')

templates = Jinja2Templates(directory='templates')


@app.get('/', name='index')
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
