# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 10:24:53 2021

@author: hp
"""
import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('RF_regression_model.pkl','rb'))

def predict_price(Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner,no_year):
    input=np.array([[Present_Price,Kms_Driven, Owner,no_year,Fuel_Type,
                   Seller_Type,Transmission,Owner]]).astype(np.float64)
    prediction=model.predict(input)
    return float(prediction)
def main():
    st.title("Car Price Prediction")
    html_temp="""
    <div style="background-color:#025246;padding:10px">
    <h2 style="color:white;text-align:center">Used Car Price Prediction ML App</h2>
    </dive>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Present_Price=st.number_input("what is the current market value if the car","In Lakhs",format="%.2f",min_value=0)
    Kms_Driven=st.number_input("how many km the car has deriven?","type here")
    Kms_Driven2=st.number_input('Kms_Driven')
    Owner=st.number_input("what is the number of owners","please type 0/1/2/3")
    no_year=st.number_input("how many years old")
    Fuel_Type=st.number_input("what is the type of fuel. type 0 for CNG/1 for Diesel/2 for Petrol")
    Seller_Type=st.number_input("what is the type of seller. type 0 for Dealer/1 for Individual")
    Transmission=st.number_input("what is the type of transmisssion.  type 0 for Automatic/1 for manual")
   
                 
    if st.button("predict"):
        output=predict_price(Present_Price,Kms_Driven2,Fuel_Type,Seller_Type,Transmission,Owner,no_year)
        st.success("The selling price of this vehicle is{}lakh".format(round(output,2)))
                     
if __name__=='__main__':
        main()