import datetime
import json
from fastapi import FastAPI, Body, Header, Response
from fastapi.encoders import jsonable_encoder
import pytest

app = FastAPI()

@app.get('/agent')
def greet(user_agent:str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

@app.get("/header/{name}/{value}")
def header(name:str, value: str, response: Response):
    response.headers[name] = value
    return 'normal body'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)


# @pytest.fixture
# def data():
#     return datetime.datetime.now()

# def test_json_dump(data):
#     with pytest.raises(Exception):
#         _ = json.dumps(data)

# def test_encoder(data):
#     out = jsonable_encoder(data)
#     assert out
#     json_out = json.dumps(out)
#     assert json_out