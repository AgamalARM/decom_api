from fastapi import FastAPI
from fastapi.params import Body
import requests
################################################
app = FastAPI()
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# x = requests.get('http://dexcom.invasso.com/api/dexcom/simulation', headers=headers)
# y = x.json()


# trend_name = y['trend']
# reading_value =  180  #y['sensor_treading_value']
# student_id = y['student_id']



def get_result(student_id,reading, trend):
   

    
    if ((reading >= 80) and (reading <= 140)):
        return {"value":reading,"Student_id": student_id, "Classification": 3}
        
        
    elif ((reading < 80) and (trend in ["Flat", "Double up", "Single up", "Forty_five up"])):
        return {"value":reading,"Student_id": student_id, "Classification": 2}
        
    elif ((reading < 80) and (trend in ["Double down", "Single down", "Forty_five down"])):
        return {"value":reading,"Student_id": student_id, "Classification": 1}
        
    elif ((reading > 140) and (trend in ["Double up", "Single up", "Forty_five up"])):
        return {"value":reading,"Student_id": student_id, "Classification": 5}
        
    elif ((reading > 140) and (trend in ["Flat", "Double down", "Single down", "Forty_five down"])):
        return {"value":reading,"Student_id": student_id, "Classification": 4}
       
        
  
@app.get("/api/Dexcom_classification")
async def root():
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    x = requests.get('http://dexcom.invasso.com/api/dexcom/simulation', headers=headers)
    y = x.json()


    trend_name = y['trend']
    reading_value =  y['sensor_treading_value']
    student_id = y['student_id']
    return get_result(student_id,reading_value, trend_name)