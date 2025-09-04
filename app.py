import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app uses a machine learning for predicting house prices with given features of the house. For using this app you can enter the input from this UI and then use predict button")

st.divider()

st.caption("Made by Romeena Shaikh")

bedrooms = st.number_input("Number of Bedrooms", min_value= 0, value =0)
bathrooms = st.number_input("Number of Bathrooms", min_value= 0, value = 0)
living_area = st.number_input("Living Area (in sqft)", min_value= 0, value = 2000)
condition = st.number_input("Condition of the House (1-5)", min_value= 0, max_value=5)

st.divider()

X =[[bedrooms, bathrooms, living_area, condition]]

predictbutton = st.button("Predict Price")
    
if predictbutton:
   
   st.balloons()

   X_array = np.array(X)

   prediction = model.predict(X_array)[0]    

   st.write(f"The predicted price of the house is {prediction:,.2f}")

else:
    st.write("Click on Predict button to get the price of the house after entering the values")     



#Order of X ['number of bedrooms', 'number of
#  bathrooms', 'living area',
      # 'condition of the house']