"""
What is Dependency Injection?
When dependencies are injected to the code it is called Dependency Injection.
Dependency Injection is a design pattern that allows us to inject dependencies into our code without relying on the caller to do it.

USESE:-
1) Have shared Logic
2)Shared DataBase Connection
3)Explore Security, authentications ec

"""



from fastapi import FastAPI,Query,Depends
from typing import Optional
app = FastAPI()

# Have shared Logic
def common_params(q : Optional[str]="Waqas ahmed",skip:int=50,limit:int=100):
    return {"q":q,"skip":skip,"limit":limit}


@app.get("/items")
def read_items(commons:dict=Depends(common_params)):
    return commons.get("skip")


@app.get("/users")
def read_users(commons:dict=Depends(common_params)):
    return commons.get("q")



#class logic can also be shared
#Any callable can be used as a dependency

class commonparams:
    def __init__(self,q : Optional[str]="Waqas khan",skip:int=50,limit:int=100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/")
def read_root(commons:commonparams=Depends(commonparams)):
    return ("q",commons.q,"skip",commons.skip,"limit",commons.limit)
