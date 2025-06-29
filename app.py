import streamlit as st
import pandas as pd
import numpy as np
import joblib

def run_PREDICTION():
    st.title("🏋️‍♀️ Calories & Nutrition Prediction")

    @st.cache_data
    def load_data():
        return pd.read_csv("fitness_data.csv")

    @st.cache_resource
    def load_models():
        model = joblib.load("final_multi_output_model.pkl")
        scaler = joblib.load("scaler.pkl")
        label_encoders = joblib.load("label_encoders.pkl")
        return model, scaler, label_encoders

    df = load_data()
    model, scaler, label_encoders = load_models()
    st.success("✅ Data and Model Loaded Successfully")

    with st.form("user_input_form"):
        sleep = st.number_input("🛌 Sleep Hours", min_value=0, max_value=12, value=7)
        gender = st.selectbox("Gender", list(label_encoders['Gender'].classes_))
        age = st.number_input("Age", min_value=5, max_value=100, value=30)
        height = st.number_input("Height (cm)", min_value=50, max_value=250, value=175)
        weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0)

        bmi_val = weight / ((height / 100) ** 2)
        st.markdown(f"**🧮 Calculated BMI:** `{bmi_val:.2f}`")

        activity = st.selectbox("Activity Level", list(label_encoders['Activity_Level'].classes_))
        goal = st.selectbox("Fitness Goal", list(label_encoders['Fitness_Goal'].classes_))

        submitted = st.form_submit_button("🎯 Predict My Nutrition Plan")

    if submitted:
        try:
            user_input = {
                'Age': age,
                'Gender': label_encoders['Gender'].transform([gender])[0],
                'Height_cm': height,
                'Weight_kg': weight,
                'Sleep_hrs': sleep,
                'Activity_Level': label_encoders['Activity_Level'].transform([activity])[0],
                'Fitness_Goal': label_encoders['Fitness_Goal'].transform([goal])[0]
            }

            input_array = np.array([[user_input[col] for col in user_input]])
            input_scaled = scaler.transform(input_array)
            prediction = model.predict(input_scaled)[0]

            daily_need, protein, carbs, fats, water, bmi, maintenance, delta = prediction
            decoded_goal = goal.lower().strip()

            st.write("🎯 Selected fitness goal (debug):", decoded_goal)

            st.subheader("🔥 Caloric Analysis")

            if "maintain" in decoded_goal or "maintenance" in decoded_goal:
                st.markdown(f"⚖️ **Maintenance Calories:** `{maintenance:,.0f} kcal`")
                st.info("Your goal is to maintain weight. Stay close to your maintenance level.")

            elif "loss" in decoded_goal or "weight loss" in decoded_goal:
                recommended = daily_need - 500 if daily_need - 500 > 1200 else daily_need - 300
                deficit = recommended - daily_need
                st.markdown(f"⚖️ **Maintenance Calories:** `{maintenance:,.0f} kcal`")
                st.markdown(f"📉 **Recommended Deficit:** `{deficit:.0f} kcal`")
                st.warning(f"Suggested Intake for Weight Loss: `{recommended:,.0f} kcal/day`")

            elif "gain" in decoded_goal or "muscle" in decoded_goal or "weight gain" in decoded_goal:
                surplus = daily_need - maintenance
                st.markdown(f"🔥 **Suggested Calories for Gain:** `{daily_need:,.0f} kcal`")
                st.markdown(f"⚖️ **Maintenance Calories:** `{maintenance:,.0f} kcal`")
                st.markdown(f"📈 **You need a Caloric Surplus of `{surplus:.0f} kcal`**")
                st.success("This will support healthy weight or muscle gain.")

            st.subheader("🍎 Nutrition Analysis")

            if "loss" in decoded_goal or "weight loss" in decoded_goal:
                st.markdown(f"💪 **Protein:** `{protein:.0f} g` — High intake helps preserve lean muscle during fat loss.")
                st.markdown(f"🍃 **Carbs:** `{carbs:.0f} g` — Focus on complex carbs like oats, quinoa, and vegetables.")
                st.markdown(f"🥑 **Fat:** `{fats:.0f} g` — Stick to healthy fats like nuts, olive oil, and avocado.")
                st.markdown(f"💧 **Water Intake:** `{water:.1f} L` — Ensure hydration, especially when in a deficit.")
                st.markdown(f"📏 **Predicted BMI:** `{bmi:.2f}` — Aim for slow, consistent BMI reduction.")

            elif "gain" in decoded_goal or "muscle" in decoded_goal or "weight gain" in decoded_goal:
                st.markdown(f"💪 **Protein:** `{protein:.0f} g` — Essential for muscle growth; aim for spread across meals.")
                st.markdown(f"🍚 **Carbs:** `{carbs:.0f} g` — Prioritize starchy carbs like rice, potatoes, whole grains.")
                st.markdown(f"🧈 **Fat:** `{fats:.0f} g` — Include energy-dense sources like nut butters and ghee.")
                st.markdown(f"💧 **Water Intake:** `{water:.1f} L` — Helps with digestion and recovery.")
                st.markdown(f"📏 **Predicted BMI:** `{bmi:.2f}` — Gradual increase indicates healthy muscle gain.")

            elif "maintain" in decoded_goal or "maintenance" in decoded_goal:
                st.markdown(f"💪 **Protein:** `{protein:.0f} g` — Helps maintain muscle and keep metabolism stable.")
                st.markdown(f"🍞 **Carbs:** `{carbs:.0f} g` — Include a mix of complex carbs and moderate sugars.")
                st.markdown(f"🥜 **Fat:** `{fats:.0f} g` — Balance saturated and unsaturated fats.")
                st.markdown(f"💧 **Water Intake:** `{water:.1f} L` — Maintain 2–3L per day for overall wellness.")
                st.markdown(f"📏 **Predicted BMI:** `{bmi:.2f}` — Indicates your current body composition status.")

        except ValueError as e:
            st.error(f"Label encoding error: {e}")



