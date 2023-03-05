import pickle
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from streamlit_lottie import st_lottie
import requests
global c

model = pickle.load(open('model_loan_classifier.pkl', 'rb'))
data = pd.read_csv('Loan_Approval_Data.csv')
data.dropna(inplace=True)

st.markdown("<h1 style='text-align: center; color: White;'>Loan Classification using ML</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: White;'>It predicts whether the loan will be approved or not based on given parameters</h6>",
            unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)
with col1:
    n7 = st.number_input('Loan Amount', 0.00)
with col2:
    n5=st.number_input('Applicant Income', 0.00)
with col3:
    n6=st.number_input('Co-applicant Income', 0.00)
n4=st.slider('Loan Duration (Days)', data['Loan_Amount_Term'].dropna().min().tolist(),
                  data['Loan_Amount_Term'].dropna().max().tolist(),
                  data['Loan_Amount_Term'].dropna().median().tolist())

col1, col2, col3, col4 = st.columns(4)
with col1:
    n1 = st.radio('Gender', (data['Gender'].sort_values(ascending=False).unique().tolist()))
with col2:
    a=st.radio('Married', (data['Married'].sort_values(ascending=False).unique().tolist()))
with col3:
    n3 = st.radio('Self_Employed', (data['Self_Employed'].sort_values(ascending=False).unique().tolist()))
with col4:
    c = st.radio('Credit History', (data['Credit_History'].sort_values(ascending=False).unique().tolist()))

col1, col2, col3 = st.columns(3)
with col1:
    b = st.selectbox('Education', (data['Education'].sort_values().unique().tolist()))
with col2:
    n2 = st.selectbox('Dependents', (data['Dependents'].sort_values(ascending=False).unique().tolist()))
with col3:
    d=st.selectbox('Property Area', (data['Property_Area'].sort_values().unique().tolist()))

a1=1 if a=='Yes' else 0
b1=1 if b=='Graduate' else 0
e=1 if d=='Rural' else 0
f=1 if d=='Semiurban' else 0
g=1 if d=='Urban' else 0

input_data = np.array([[a1,b1,c,e,f,g]])
input_data = pd.DataFrame(input_data, columns=['Married', 'Education', 'Credit_History', 'Rural', 'Semiurban', 'Urban'])


c=5
col1, col2, col3 = st.columns(3)
with col2:
    if st.button("CLick here to check your Loan Status", key="predict"):
        output = model.predict(input_data)
        if (output[0] == 1):
            c=1
        elif (output[0] == 0):
            c=0

if (c==1):
    st.balloons()
    st.markdown(
        "<h3 style='text-align: center; color: White; background-color:MediumSeaGreen;'>Your loan will get approved</h3>",
        unsafe_allow_html=True)
elif (c==0):
    st.markdown(
        "<h3 style='text-align: center; color: White; background-color:Tomato;'>Your loan will not get approved</h3>",
        unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    if (c == 1):
        r = requests.get("https://assets8.lottiefiles.com/private_files/lf30_c9fgeliv.json")
        if r.status_code == 200:
            st_lottie(r.json())
    elif (c == 0):
        r = requests.get("https://assets9.lottiefiles.com/private_files/lf30_o1myfbpb.json")
        if r.status_code == 200:
            st_lottie(r.json())
