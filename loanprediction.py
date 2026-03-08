import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("train_u6lujuX_CVtuZ9i (1).csv")

df.drop(columns=['Loan_ID'], inplace=True)

df['Dependents'] = df['Dependents'].replace('3+',3)
df['Dependents'] = pd.to_numeric(df['Dependents'], errors='coerce')

df.fillna(df.mode().iloc[0], inplace=True)

label_encoders = {}

for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

X = df.drop(columns=['Loan_Status'])
y = df['Loan_Status']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=300)
model.fit(X_train,y_train)

pred = model.predict(X_test)
accuracy = accuracy_score(y_test,pred)*100

st.title("🏦 Loan Approval Prediction")
st.write(f"Model Accuracy : {accuracy:.2f}%")

st.sidebar.header("Enter Applicant Details")

gender = st.sidebar.selectbox("Gender", ["Male","Female"])
married = st.sidebar.selectbox("Married", ["Yes","No"])
dependents = st.sidebar.selectbox("Dependents",[0,1,2,3])
education = st.sidebar.selectbox("Education",["Graduate","Not Graduate"])
self_employed = st.sidebar.selectbox("Self Employed",["Yes","No"])
applicant_income = st.sidebar.number_input("Applicant Income",0)
coapplicant_income = st.sidebar.number_input("Coapplicant Income",0)
loan_amount = st.sidebar.number_input("Loan Amount",0)
loan_term = st.sidebar.number_input("Loan Amount Term",0)
credit_history = st.sidebar.selectbox("Credit History",[0,1])
property_area = st.sidebar.selectbox("Property Area",["Urban","Semiurban","Rural"])

input_data = pd.DataFrame({
    'Gender':[gender],
    'Married':[married],
    'Dependents':[dependents],
    'Education':[education],
    'Self_Employed':[self_employed],
    'ApplicantIncome':[applicant_income],
    'CoapplicantIncome':[coapplicant_income],
    'LoanAmount':[loan_amount],
    'Loan_Amount_Term':[loan_term],
    'Credit_History':[credit_history],
    'Property_Area':[property_area]
})

for col in input_data.columns:
    if col in label_encoders:
        input_data[col] = label_encoders[col].transform(input_data[col])

if st.button("Predict Loan Approval"):

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Not Approved")