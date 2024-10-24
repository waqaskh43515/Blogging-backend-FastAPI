from database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


 
class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    creator = relationship("user", back_populates="blog")
    user_id = Column(Integer, ForeignKey("users.id"))



class user(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    blog = relationship("Blog", back_populates="creator")

