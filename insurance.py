import pandas as pd
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import List,Dict,Literal,Annotated
from pydantic import BaseModel,Field,computed_field
import pickle


# import ml model
with open('model.pkl','rb') as f:
    model=pickle.load(f)

# make a Fastapi app object
app=FastAPI()

# for computed field classification of Tier
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

#Build pydantic class model to validate input   
class UserInput(BaseModel):

    age:Annotated[int,Field(...,gt=0,lt=120,description='Age of Person')]
    weight:Annotated[float,Field(...,gt=0,description='weight of Person')]
    height:Annotated[float,Field(...,gt=0,lt=2.5,description='Height of Person')]
    income_lpa:Annotated[float,Field(...,gt=0,description='Income of Person')]
    smoker:Annotated[bool,Field(...,description='Is Person smoker')]
    city:Annotated[str,Field(...,description='City of Person')]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description="Occupation of Person")]
    
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def lifestyle_risk(self)->str:
        if self.smoker and self.bmi>30:
            return "Low"
        elif self.smoker and self.bmi>27:
            return "Medium"
        else:
            return "Low"
        
    @computed_field
    @property
    def age_group(self)->str:
        if self.age<25:
            return "Young"
        elif self.age<45:
            return "Adult"
        elif self.age<60:
            return "Middle Age"
        else:
            return "Senior"
        
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3
@app.post('/predict')
def predict_premium(data:UserInput):

    input_df=pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.occupation    
    }])

    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={"Predicted_category":prediction})

