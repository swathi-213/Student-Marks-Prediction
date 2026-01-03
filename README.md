# Student Marks Prediction

This project predicts a student’s **expected marks range** based on
**attendance** and **hours studied**.

The objective of the project is to demonstrate an end-to-end machine learning
workflow — from dataset creation and model training to deployment as a simple
web application.


## Problem Statement

Users (students, parents, and tutors) upload a CSV file containing:
- Attendance
- Hours studied

After clicking **Predict Marks**, the application displays the **expected marks
range**, rather than an exact score, to reflect real-world uncertainty.


## Features

- Upload CSV file with student data
- Predict expected marks range using a trained ML model
- Show exact marks only for:
  - Full effort (100% attendance, 30 study hours)
  - No effort (0% attendance, 0 study hours)
- Simple and clean Streamlit user interface


## Dataset Creation

A **synthetic dataset** was created using the following assumptions:

- Attendance range: **0–100 percent**
- Study hours range: **0–30 hours** (total over a period)
- Attendance contributes **up to 40 marks**
- Study hours contribute **up to 60 marks**
- Total marks range: **0–100**

These assumptions are clearly defined to keep the model interpretable and easy
to explain.


## Model Details

- Algorithm used: **Linear Regression**
- Libraries: `scikit-learn`, `pandas`
- Model trained and evaluated using **Google Colab**
- The trained model is saved and reused during deployment

The model predicts a numeric score internally, which is then converted into a
marks range for display.


## Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit


## How to Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the Streamlit app:
   ```bash
   streamlit run app.py

3. Open the browser and upload a CSV file to get predictions.
