from fastapi import Depends, FastAPI, Query


app = FastAPI()

# 의존성 함수:
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender, "valid": True}

# 경로 함수 / 웹 엔드포인트 : 
@app.get("/user")
def get_user(user:dict = Depends(user_dep)) -> dict:
    return user

# 의존성 함수
def check_dep(name: str = Query(...), gender:str=Query(...)):
    if not name:
        raise

# 경로 함수 / 웹 엔드 포인트
@app.get("/check_user", dependencies=[Depends(check_dep)])
def check_user() -> bool:
    return True
