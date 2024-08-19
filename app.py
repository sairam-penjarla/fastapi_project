import yaml
import uvicorn
from utils import verify_token
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException, Depends

app = FastAPI()

# Load configuration
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

class Item(BaseModel):
    param1: str
    param2: int
    param3: float
    param4: bool
    param5: str

def get_oauth_token(request: Request):
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="OAuth token missing")
    return token

@app.post("/process")
def process_item(item: Item, token: str = Depends(get_oauth_token)):
    if not verify_token(token, config['oauth']['token']):
        raise HTTPException(status_code=403, detail="Invalid OAuth token")

    # Slightly modify the parameters
    response = {
        "param1": item.param1.upper(),
        "param2": item.param2 + 1,
        "param3": item.param3 * 1.1,
        "param4": not item.param4,
        "param5": f"Modified-{item.param5}"
    }
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
