
from fastapi import FastAPI,Depends,status,Response,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import user
from schemas import users,showuser
from passlib.context import CryptContext
from routers import blogs
from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


pwd_cxt = CryptContext(schemes=["bcrypt"],deprecated="auto")


@router.post("",status_code=status.HTTP_201_CREATED,response_model=showuser)
def Post_user(request : users,db: Session = Depends(get_db)):
    Hashpassword = pwd_cxt.hash(request.password)
    new_user = user(name=request.name,email=request.email,password=Hashpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.get("/{id}",response_model=showuser,status_code=status.HTTP_200_OK)
def get_user(id,db: Session = Depends(get_db)):
    users = db.query(user).filter(user.id == id).first()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id of {id} not found")
    return users    