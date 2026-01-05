# Insurance Premium Prediction API (FastAPI + Docker)

This project is a **machine learning–powered REST API** built using **FastAPI** that predicts insurance premium based on user details such as age group, BMI, income, occupation, lifestyle risk, and city tier.  
The API is production-ready and containerized using **Docker**.

---

## 🚀 Features

- Fast and lightweight **FastAPI** backend
- Machine Learning–based insurance premium prediction
- **Health check endpoint** with model versioning
- Request & response validation using **Pydantic schemas**
- Dockerized for easy deployment
- Clean and modular project structure

---

## 🛠 Tech Stack

- **Backend:** FastAPI
- **ML Model:** Scikit-learn (pre-trained)
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Containerization:** Docker
- **Language:** Python 3.9+

---

## 📁 Project Structure
│
├── insurance.py            # FastAPI backend (ML API)
├── web_insrurance.py       # Streamlit frontend
├── model.pkl               # Trained ML model
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
└── README.md               # Project documentation

📊 Input Features
The application collects the following inputs:

Feature	Description
Age	User's age
Weight	Weight in kg
Height	Height in meters
Income	Annual income (LPA)
Smoker	Smoking status
City	City of residence
Occupation	Job type

⚙️ Feature Engineering (Automatic)

The backend computes additional features:
BMI = Weight / Height²
Age Group → Young / Adult / Middle Age / Senior
Lifestyle Risk → Based on smoking & BMI
City Tier → Tier 1 / Tier 2 / Tier 3 cities

# 🔗 API Endpoint
POST /predict

Request JSON

{
  "age": 45,
  "weight": 65.5,
  "height": 1.7,
  "income_lpa": 10,
  "smoker": true,
  "city": "Mumbai",
  "occupation": "private_job"
}


# Response

{
  "Predicted_category": "Medium"
}

# 🖥️ Running the Project (Without Docker)
1️⃣ Install Dependencies
pip install -r requirements.txt

# 2️⃣ Run FastAPI Backend
uvicorn insurance:app --reload


# API will be available at:
http://localhost:8000

# 3️⃣ Run Streamlit Frontend
streamlit run web_insrurance.py

# 🐳 Running with Docker
1️⃣ Build Docker Image
docker build -t insurance-api .

# 2️⃣ Run Container
docker run -p 8000:8000 insurance-api


# FastAPI will be available at:
http://localhost:8000/docs

# 📌 Streamlit UI
The Streamlit app sends user input to the FastAPI backend and displays the predicted insurance premium category in real-time.

# ✅ Output
Low Premium
Medium Premium
High Premium
(Based on trained ML model)

# 📈 Future Enhancements

Deploy on AWS / Azure
Add authentication
Improve model accuracy
Store predictions in database
Add CI/CD pipeline

# 👤 Author 
Ashutosh Kumar Ranjan

⭐ Support
If you like this project, please ⭐ the repository and share it!

