# Pydantic used for Data validation and Type Validation
from pydantic import BaseModel,EmailStr,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name : Annotated[str,Field(max_length=50,description='Set the name of patient')]
    email: EmailStr
    age:int = Field(gt=18,lt=35)
    weight:Annotated[float,Field(gt=0, strict=True)]
    married:bool = False
    allergies: Optional[List[str]]
    contact_details: Dict[str,str]

def insert_Patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)
    print(patient.allergies)
    print("Success")

patient_info = {'name':'Aditya','email':'abc@gmail.com','age':20,'weight':70,'married':True,'allergies':['pollen','dust','smoke'],'contact_details':{'email':'abc@gmail.com','contact':'786354116'}}

patient1 = Patient(**patient_info)

insert_Patient(patient1)
    

