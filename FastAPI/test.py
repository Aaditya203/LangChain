from fastapi import FastAPI,Path,HTTPException,Query
import json

app = FastAPI()

def load_data():
    with open('patients.json' ,'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {'message':'hello there'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get("/patient/{id}")
def get_patient(id:str = Path(..., description='Id of Patient',example='P001')):
    data = load_data()
    if id in data:
        return data[id]
    
    raise HTTPException(status_code=404,detail='Patient Not Found')

@app.get("/sort")
def sortingss(sort_by: str = Query(..., description='Sort on basis of height, weight, bmi'),order_by:str = Query('asc',description='Sort by asc or dsc')):
    data = load_data()
    if sort_by not in ['height','weight','bmi']:
        raise HTTPException(status_code=404,detail='Sort by not found')
    if order_by not in ['asc','dsc']:
        raise HTTPException(status_code=404,detail='Not Found')
    
    sorting = True
    if order_by == 'asc':
        sorting = False

    sorted_data = sorted(data.values(),key = lambda x:x.get(sort_by,0),reverse = sorting)
    return sorted_data