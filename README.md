# Titanic Survival Prediction AI System API

### Live Production API Link
[Live FastAPI Application Endpoint](https://ai-systems-and-development.onrender.com/)

## Project Overview
This project represents the practical implementation of model serialization, backend API development, and production cloud deployment for Week 7 of the AnalystLab Africa (ALA) internship. The system encapsulates a trained machine learning classification engine and exposes it to the web as a responsive REST API using FastAPI.

## Problem Being Solved
Machine learning models are frequently isolated within data science development environments (like Jupyter Notebooks). This separation prevents real-world software applications, business platforms, or end-users from leveraging their predictive power. 

This project solves that operational bottleneck by packaging a Titanic Survival prediction engine into an internet-ready microservice. This allows any external client to send structured passenger data to our server and receive instantaneous, real-time survival probabilities.

## Technologies & Stack Used
- **Programming Language:** Python 3.10+
- **Framework Architecture:** FastAPI (Asynchronous Server Gateway Interface)
- **Production Server Wrapper:** Uvicorn 
- **Machine Learning Core:** Scikit-Learn (Random Forest Classifier)
- **Serialization Engine:** Joblib (Data Persistence Architecture)
- **Data Manipulation:** Pandas
- **Version Control:** GitHub
- **Cloud Hosting Platform:** Render (Free Tier Web Service)

## How the AI System Works
1. **Model Persistence:** The mathematical patterns and decision boundaries learned by our Random Forest Classifier are frozen into a portable binary layout (`titanic_model.joblib`). This completely bypasses the need to retrain the model on every incoming request.
2. **API Data Ingestion:** The FastAPI backend utilizes `Pydantic` validation schemas to enforce strict data-typing on incoming user information. 
3. **Inference Execution:** When a client sends a valid payload, the server converts the JSON data into a single-row Pandas DataFrame, passes it directly into the loaded model's memory space, executes the `.predict()` and `.predict_proba()` sequences, and returns the calculated outputs in milliseconds.

---

## API Endpoints Documentation

### 1. Base Health Check
- **Endpoint:** `GET /`
- **Description:** Verifies that the cloud server is online and running normally.
- **Example Response:**
```json
  {
    "message": "Titanic API is Online!"
  }

  {
    "Pclass": 1,
    "Sex": 0,
    "Age": 29.0,
    "SibSp": 0,
    "Parch": 0,
    "Fare": 150.0
  }

  {
    "status": "Survived",
    "survival_probability": "81.50%"
  }

  
