'''
Pydantic is a Python library used for data validation, parsing, and settings management using Python type hints. 
It ensures that the data your program receives is correct, structured, and safe to use.

Think of Pydantic as a gatekeeper 🛂 that checks incoming data and converts it into clean Python objects.
'''

from pydantic import BaseModel
from pydantic import EmailStr , Field
from typing import Optional 

# Class | Schema   Created 
class Student(BaseModel):
    name: str
    lastName: str ='devgan'    # Deafult Value Set
    age: Optional[int] = None  # if age is not given then it is None
    email: EmailStr            # validation applied [Emailstr is built in data type present in pydantic]
    cgpa: float = Field(gt=0 , lt=10) # Constraint applied {cgpa should greater than 0 and less than 10}

# Created a dictionary
new_student = {'name':'nitish','email': "raghavdevgan333@gmail.com",'cgpa':9}

# object created of Student Class
student = Student(**new_student)

# Printing Pydantic Object
print(student)

# Converting pydantic object in to {Dict} 
print(dict(student))

# Converting pydantic object in to {Json}
print(student.model_dump_json())

 

