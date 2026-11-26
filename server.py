from fastapi import FastAPI

app = FastAPI()

@app.get("/get-message")
async def read_root(header, payload, trailer):
    return {"Message": "Header" + header + "Payload" + payload + "Trailer" + trailer}

