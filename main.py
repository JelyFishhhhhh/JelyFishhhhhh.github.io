from modules import Json

from fastapi import FastAPI
from uvicorn import Config, Server

from aiofiles import open as aopen

app = FastAPI()

CONFIG = Json.load_nowait("config.json")

@app.get("/")
async def home():
    return "Hello, World."

def Run():
    config = Config(app, host = CONFIG["HOST"], port = CONFIG["PORT"])
    server = Server(config = config)
    server.run()

if __name__ == "__main__":
    Run()