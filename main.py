from modules import Json
from gen_config import *

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from uvicorn import Config, Server

from asyncio import run
from aiofiles import open as aopen
from os.path import isfile, join
from os import listdir

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

if not isfile("config.json"):
    run(gen_CONFIG)

CONFIG = Json.load_nowait("config.json")

@app.get("/")
async def home():
    # files = [_f for _f in listdir("templates") if isfile(join("templates", _f))]
    
    files = "templates\\index.html"

    if isfile(files):

        async with aopen(files, mode="rb") as html_file:

            return HTMLResponse(await html_file.read())
    
    else:
        return "404 Not-Found"

def Run():
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    server.run()

if __name__ == "__main__":
    Run()