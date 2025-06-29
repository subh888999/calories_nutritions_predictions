import streamlit as st

def run_Description():
    st.title("🍽️ :blue[Smart Calories & Nutrition Prediction]")

    st.markdown("### Business Problem")
    st.write("""
    People often follow generic diet plans that don't consider individual factors like age, gender, weight, height, activity level, and personal goals.
    As a result, they may not meet their nutritional needs or achieve fitness objectives. There’s also a lack of personalized insight into how much protein, carbohydrates, fat, and water intake is ideal for them.
    """)

    st.markdown("### Project Goal")
    st.write("""
    This project aims to provide a smart, data-driven recommendation system that predicts daily caloric needs and gives a complete macronutrient breakdown.
    It helps users align their food intake with fitness goals such as weight loss, weight gain, or maintenance.
    """)

    st.markdown("### Objectives")
    st.markdown("""
    - Predict daily calorie needs based on personal inputs (age, gender, weight, height, activity level, sleep hours).
    - Recommend personalized protein, carbs, fat, and water intake.
    - Suggest caloric deficit/surplus based on the selected fitness goal.
    - Display predicted BMI and compare it to ideal ranges.
    """)

    st.markdown("### Data Understanding")
    st.write("""
    The project uses processed user input along with a trained regression model and label encoders. The key input features include:
    """)

    st.markdown("""
    | Feature | Description | Importance |
    |--------|-------------|------------|
    | **Age** | User's age in years. | Affects BMR and metabolism. |
    | **Gender** | Biological sex. | Influences calorie burn rate and body composition. |
    | **Height (cm)** | User’s height in centimeters. | Used to calculate BMI and BMR. |
    | **Weight (kg)** | User’s weight in kilograms. | Crucial for determining energy needs. |
    | **Sleep Hours** | Average daily sleep duration. | Impacts recovery and metabolic rate. |
    | **Activity Level** | User's physical activity (Low, Moderate, High). | Major determinant of calorie needs. |
    | **Fitness Goal** | Goal like weight loss, gain, or maintenance. | Adjusts caloric intake accordingly. |
    """)

    st.info("🎯 The output includes maintenance calories, recommended intake for your goal, and a detailed breakdown of macronutrients with hydration suggestion.")

