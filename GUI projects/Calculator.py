# Simple Calculator using Streamlit

import streamlit as st

st.title("SIMPLE CALCULATOR❤️")

a = st.number_input("Enter first number: ")
b = st.number_input("Enter second number: ")

operations = st.selectbox("Choose operations", ("Addition", "Subtraction", "Multiplication", "Division"))

if st.button("Calculate"):

    if operations == "Addition":
        result = a+b
    elif operations == "Subtraction":
        result = a-b
    elif operations == "Multiplication":
        result = a*b
    elif operations == "Division":
        if b!=0:
            result = a/b
        else:
            raise ValueError("ZeroDivisionError")
    
    st.success(f'Result: {result}')