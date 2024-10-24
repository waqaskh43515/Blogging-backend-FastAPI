

from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from schemas import login
from database import get_db
from models import user as User
from hashing import Hash
from routers.JWTtoken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["login"])


@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User not found")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Wrong password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token":access_token, "token_type":"bearer"}