
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime


class Emp_data(BaseModel):
    date: str = datetime.now().strftime("%Y-%m-%d")
    id: str
    name: str
    entry_time: str = datetime.now().strftime("%I:%M %p")
    exit_time: str = datetime.now().strftime("%I:%M %p")

app=FastAPI()


example_data = [
    Emp_data(date="2025-10-23", id="EMP001", name="Pavan Manikanta", entry_time="09:00 AM", exit_time="06:00 PM"),
    Emp_data(date="2025-10-23", id="EMP002", name="Anita Sharma", entry_time="09:30 AM", exit_time="05:30 PM"),
    Emp_data(date="2025-10-23", id="EMP003", name="Ravi Kumar", entry_time="10:00 AM", exit_time="07:00 PM"),
    Emp_data(date="2025-10-23", id="EMP004", name="Sneha Reddy", entry_time="08:45 AM", exit_time="05:15 PM"),
    Emp_data(date="2025-10-23", id="EMP005", name="Arjun Verma", entry_time="09:15 AM", exit_time="06:15 PM"),
    Emp_data(date="2025-10-23", id="EMP006", name="Meena Joshi", entry_time="09:00 AM", exit_time="05:45 PM")
]

#get all
@app.get("/log")
def get_all():
    return example_data


#getbyid
@app.get("/log/{id}")
def getby_id(id=str):
    for record in example_data:
        if record.id.lower() == id.lower():
            return ("Record Was Sucessfuly Extracted",record)
    return "No Data Was Found"
        
#create
@app.post("/log")
def create_data(log:Emp_data):
    example_data.append(log)
    return ("Data was added sucessfuly",log)

#update

@app.put("/log")
def update_data(id:str,log:Emp_data):
    for i in range(len(example_data)):
        if example_data[i].id == id:
            example_data[i].id=log.id
            example_data[i].name = log.name
            return ("Data was Updated  sucessfuly",{'log': example_data[i]})
    
            

@app.delete("/log")
def dele_dat(id:str=None,name=str):
    for i in range(len(example_data)):
        if example_data[i].id.lower() == id.lower():
            del example_data[i].id 
            return "data was deleted sucsessfuly by"
    
        elif example_data[i].name.replace(" ","").lower() == name.lower():
            del example_data[i].name
            return "data deleted sucesffully by name"
    return "No data Found "