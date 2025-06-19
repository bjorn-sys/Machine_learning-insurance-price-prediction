import pandas as pd
import numpy as np
import streamlit as st
import pickle
import numpy as np


with open('insurancemodelf.pkl', 'rb') as f:
    model = pickle.load(f)

def input_data():
        
        age = st.number_input("Enter your age", min_value=18, max_value=100, value=30)
        sex = st.selectbox("Select your sex", options=["Male", "Female"])
        bmi = st.number_input("Enter your BMI", min_value=10.0, max_value=50.0, value=25.0)
        children = st.number_input("Enter number of children", min_value=0, max_value=10, value=0)
        smoker = st.selectbox("Are you a smoker?", options=["Yes", "No"])
        region = st.selectbox("Select your region", options=["North", "South", "East", "West"])


        sex_encoded = 1 if sex =='Male' else 0
        smoker_encoded = 1 if smoker == "Yes" else 0
        region_map = {'North': 1, 'South': 0, 'East': 2, 'West': 3}
        region_encoded = region_map[region]

        input_data = {
            "age": [age],
            "sex": [sex_encoded],
            "bmi": [bmi],
            "children": [children],
            "smoker": [smoker_encoded],
            "region":[region_encoded]
        }

    
    
        return pd.DataFrame(input_data)
      

def predict():
    st.title("Insurance Cost Prediction")
    st.subheader("Enter your details below:")
    new_data = input_data()

    if st.button("Predict"):
        prediction = model.predict(new_data)
        st.success(f"The predicted insurance cost is: ${np.round(prediction[0], 2)}")

if __name__ == "__main__":
    predict()