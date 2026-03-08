🏦 Loan Approval Prediction System

A Machine Learning web application built with Python, Scikit-Learn, and Streamlit that predicts whether a loan application will be approved or rejected based on applicant details.

This project uses a Random Forest Classifier trained on a real loan dataset to make predictions in real time through a simple Streamlit web interface.

🚀 Features

Predicts Loan Approval Status

Interactive Streamlit UI

Uses Random Forest Machine Learning model

Handles missing values and categorical encoding

Real-time prediction based on user inputs

Displays model accuracy

🧠 Machine Learning Model

Algorithm used:

Random Forest Classifier

Steps performed:

Data preprocessing

Handling missing values

Label encoding categorical features

Train-test split

Model training

Accuracy evaluation

Model accuracy is calculated using:

Accuracy Score

📊 Input Features

The model predicts loan approval using the following inputs:

Gender

Marital Status

Number of Dependents

Education Level

Self Employment Status

Applicant Income

Co-Applicant Income

Loan Amount

Loan Amount Term

Credit History

Property Area

🖥️ Streamlit Interface

Users can enter applicant information through the sidebar form, and the model will predict:

✅ Loan Approved
❌ Loan Not Approved

📂 Project Structure
Loan-Approval-Prediction
│
├── train_u6lujuX_CVtuZ9i.csv
├── loanprediction.py
├── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/yourusername/loan-approval-prediction.git

Go to the project directory:

cd loan-approval-prediction

Install dependencies:

streamlit,sklearn,pandas
▶️ Run the Application

Start the Streamlit app:

streamlit run loanprediction.py

The application will open in your browser:

http://localhost:8501
📦 Requirements
pandas
streamlit
scikit-learn
📈 Example Prediction

Input:

Gender: Male

Married: Yes

Dependents: 1

Education: Graduate

Self Employed: No

Applicant Income: 5000

Loan Amount: 150

Credit History: 1

Output:

Loan Approved
🛠️ Technologies Used

Python

Scikit-Learn

Streamlit

Pandas

Machine Learning

🎯 Future Improvements

Add probability prediction

Improve UI design

Use XGBoost for higher accuracy

Add data visualization dashboard
