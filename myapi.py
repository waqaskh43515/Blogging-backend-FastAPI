from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

# creating FastAPI object here
# FASTAPI help us in creaying documentation of the code on website
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# Path/Endpoint parameter is used to return the input 
#We can also specify the type of the input that what the user need to input in the path

students = {
    1 : {
        "name": "Waqas",
        "age": 18,
        "year": "10th"
    },
     2 : {
        "name": "khan",
        "age": 20,
        "year": "11th"
    },
      3 : {
        "name": "Ahmed",
        "age": 22,
        "year": "12th"
    }
}

# gt= greater than
# lt= less than
# lte= less than equal to
# gte= greater than equal to
@app.get("/student/{student_id}")
def student_details(student_id: int = Path(description="Enter the student id")):
    return students.get(student_id)




#Query parameters
#Pytho do not allow us to have optional variable before required variable
@app.get("/student_by_name")
def student_by_name(name: Optional[str] = None):
    for i in students:
        if students[i]['name'] == name:
            return students.get(i)
        return {"Name":"Name not Found"}
   




#Request Body and post method
#Request Body is used to take the input from the user
#Post method is used to send the data to the server  
#In the post method we need to pass the data in json format

class Student(BaseModel):
    name: str
    age: int
    year: str


@app.post("/create_student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student already exists"}
    students[student_id] = student
    return students[student_id]


class updatestudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

#Put method is used to update the data
#In the put method we need to pass the data in json format

@app.put("/update_student/{student_id}")
def update_student(student_id: int, student2: updatestudent):

    if student_id not in students:
        return {"Error": "Student does not exist"}
    

    if student2.name != None:
        students[student_id].name = student2.name
    if student2.age != None:
        students[student_id].age = student2.age
    if student2.year != None:
        students[student_id].year = student2.year        
    return students[student_id]
 


 #Delete method is used to delete the data
 #In the delete method we need to pass the data in json format
 
@app.delete("/delete_student/{student_id}")
def delete_Student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Success": "Student deleted successfully"}
