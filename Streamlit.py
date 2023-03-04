import pickle
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

model = pickle.load(open('model_loan_classifier.pkl', 'rb'))
data = pd.read_csv('Loan_Approval_Data.csv')

st.markdown("<h1 style='text-align: center; color: White;'>Loan Classification using ML</h1>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col2:
    st.text('It takes 4 inputs: \n1. Married \n2. Education \n3. Credit History \n4. Property Area')
st.text('It predicts whether the loan will be approved or not based on given parameters.')

# adding some space
st.markdown("<h1 style='text-align: center; color: White;'>  </h1>", unsafe_allow_html=True)

data.dropna(inplace=True)

col1, col2, col3, col4, col5 = st.columns(5)
with col2:
    a=st.radio('Married', (data['Married'].sort_values(ascending=False).unique().tolist()))
with col4:
    c = st.radio('Credit History', (data['Credit_History'].sort_values(ascending=False).unique().tolist()))

col1, col2, col3, col4, col5 = st.columns(5)
with col2:
    b = st.radio('Education', (data['Education'].sort_values().unique().tolist()))
with col4:
    d=st.radio('Property Area', (data['Property_Area'].sort_values().unique().tolist()))


a1=1 if a=='Yes' else 0
b1=1 if b=='Graduate' else 0
e=1 if d=='Rural' else 0
f=1 if d=='Semiurban' else 0
g=1 if d=='Urban' else 0

input_data = np.array([[a1,b1,c,e,f,g]])
input_data = pd.DataFrame(input_data, columns=['Married', 'Education', 'Credit_History', 'Rural', 'Semiurban', 'Urban'])

# adding some space
st.markdown("<h1 style='text-align: center; color: White;'>  </h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col2:
    if st.button("Click here to check", key="predict"):
            output = model.predict(input_data)
            if (output[0]==1):
                st.success("Loan approved")
            else:
                st.warning("Loan not approved")