from fastpai import FastAPI;

app + FastAPI() # type: ignore

@app.get("/") # type: ignore

async def  root(arg):
    return {"message" : "Hello worlds"}
