from typing import TypedDict

# Dictinory Format Specified
class Person(TypedDict):
    name: str
    age: int

# Dictionary Created on Specified Format
new_person: Person ={'name':'nitish' , 'age':13}

print(new_person)

# new_person → Variable name , that store dictinoary
# : Person → this part is called a type hint / type annotation.
#             new_person should follow the structure defined by Person”
#             Without type hint: Python doesn’t know what structure you to follow
#             i.e: new_person = {'name': 'nitish', 'age': 13}
