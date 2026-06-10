import streamlit as st

st.title("BMI CALCULATOR")

weight = st.number_input("Enter your weight (kg) ", min_value=1.0)

height_unit = st.radio("Select your unit for height", ["Centimeter", "Feet & Inches"])

if height_unit == "Centimeter":
    height_cm = st.number_input("Enter your height (cm) ")
    height_m = height_cm / 100

else:
    feet = st.number_input("Enter your height (feet) ")
    Inches = st.number_input("Enter your height (inches) ")

    total = (feet * 12) + Inches
    height_m = total * 0.0254

if st.button("Calculate BMI"):
    BMI = weight / (height_m * height_m)

    st.write(f"BMI : {BMI:.2f}")

    if BMI < 18:
        print("Underweight")
    elif BMI < 25:
        print("Normal weight")
    elif BMI < 30:
        print("Overweight")
    else:
        print("Obese")
        
