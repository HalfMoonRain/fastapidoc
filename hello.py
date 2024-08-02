from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get('/agent')
def greet(user_agent:str = Header()):
    return user_agent

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)