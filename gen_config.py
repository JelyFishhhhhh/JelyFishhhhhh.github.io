from modules import Json

async def gen_CONFIG():
    
    CONFIG: dict[str, dict] = {
        "HOST" : "",
        "PORT" : "",
    }

    CONFIG["HOST"] = input("Your server HOST:\n> ")
    CONFIG["PORT"] = input("Your server PORT:\n> ")

    Json.dump_nowait("config.json", CONFIG)