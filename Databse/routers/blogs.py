from fastapi import APIRouter
from fastapi import Depends,status,Response,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Blog
from schemas import Blog1,users
from schemas import show_Blog
from routers.Oauth2 import get_current_user



router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=show_Blog)
def show(id,db: Session = Depends(get_db),current_user: users = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id of {id} not found")
    return blog






#Status code helps in showing status of request
@router.post("",status_code=status.HTTP_201_CREATED)
async def root(request: Blog1,db: Session = Depends(get_db),current_user: users = Depends(get_current_user)):
    new_blog = Blog(title=request.title,body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



@router.get("")
def index(db: Session = Depends(get_db),current_user: users = Depends(get_current_user)):
    blogs = db.query(Blog).all()
    return blogs






@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db: Session = Depends(get_db),current_user: users = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id of {id} not found")
    db.commit() 
    return 'done'





@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request: Blog1,db: Session = Depends(get_db),current_user: users = Depends(get_current_user)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with the id of {id} not found")
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'updated'