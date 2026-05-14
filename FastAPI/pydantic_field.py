from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,EmailStr,field_validator,model_validator
from typing import Dict,List

app=FastAPI()

class Patient(BaseModel):
    name:str
    age:int
    email:EmailStr
    contact_details: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain =['hdfc.com','icici.com']
        data = value.split('@')[-1]
        if data not in valid_domain:
            raise HTTPException(status_code=404,detail='Invalid Email')
        return value
    
    @model_validator(mode='after')
    def validate_emergency(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patient age is more than 60 but no emergency number available!")
        return model

def show(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print('Succcess')

# patien_info = {'name':'Aditya','age':20,'email':'adi@gmail.com'} #error
patien_info = {'name':'Aditya','age':80,'email':'adi@hdfc.com','contact_details':{'contact':'434313213','emergency':'454331321'}}
patient = Patient(**patien_info)

show(patient)
