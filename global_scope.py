
from fastapi import Depends, FastAPI


def depfun1():
    pass

def depfun2():
    pass

app = FastAPI(dependencies=[Depends(depfun1), Depends(depfun2)])

@app.get("/main")
def get_main():
    pass


