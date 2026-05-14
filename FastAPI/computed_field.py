from pydantic import BaseModel,EmailStr,computed_field

class Patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight / (self.height**2))
        return bmi

def update_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.bmi)
    print('success')

patient_info = {'name':'Aditya','age':20,'weight':100,'height':10}
patient = Patient(**patient_info)

update_patient(patient)
