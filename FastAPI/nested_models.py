from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pincode: int

class Patient(BaseModel):
    name:str
    age:int
    weight:int
    address:Address

address_info = {'city':'Raipur','state':'Chhattisgarh','pincode':492099}
address1 = Address(**address_info)

patient_info = {'name':'Aditya','age':20,'weight':70,'address':address1}
patient = Patient(**patient_info)

print(patient.name)
print(patient.age)
print(patient.address.state)
print(patient.address.pincode)
