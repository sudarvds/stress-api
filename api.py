from fastapi import FastAPI
import pandas as pd
import pickle
from pydantic import BaseModel

app = FastAPI()

model = pickle.load(open("stress_model.pkl", "rb"))

class StressInput(BaseModel):
    Age: int
    Gender: int
    Job_Role: int
    Industry: int
    Years_of_Experience: int
    Work_Location: int
    Hours_Worked_Per_Week: int
    Number_of_Virtual_Meetings: int
    Work_Life_Balance_Rating: int
    Mental_Health_Condition: int
    Access_to_Mental_Health_Resources: int
    Productivity_Change: int
    Social_Isolation_Rating: int
    Satisfaction_with_Remote_Work: int
    Company_Support_for_Remote_Work: int
    Physical_Activity: int
    Sleep_Quality: int
    Region: int


@app.get("/")
def home():
    return {"message": "API Running"}


@app.post("/predict")
def predict(data: StressInput):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        result = "Low Stress"
    elif prediction == 1:
        result = "Medium Stress"
    else:
        result = "High Stress"

    return {
        "prediction": int(prediction),
        "stress_level": result
    }
