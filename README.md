
# 🍽️ Smart Calories & Nutrition Prediction

This project is a data-driven, interactive web application that provides personalized nutrition and caloric recommendations. Built using **Streamlit** and **Machine Learning**, it helps users align their dietary intake with their fitness goals like weight loss, muscle gain, or maintenance.

---

## 🧩 Business Problem

Most diet plans are generic and fail to account for individual differences like age, weight, height, gender, and activity levels. This lack of personalization often leads to inefficient results. Additionally, people rarely know their ideal macronutrient (protein, carbs, fat) and water intake.

---

## 🎯 Project Goal

The aim is to create a **smart, personalized nutrition recommendation system** that:
- Predicts **daily caloric needs**.
- Provides a **complete macronutrient breakdown**.
- Adjusts recommendations based on the user’s **fitness goals**.

---

## 🚀 Objectives

- Predict daily calorie needs using personal inputs:  
  `Age, Gender, Height, Weight, Activity Level, Sleep Hours`.
- Recommend personalized intake of:  
  `Protein`, `Carbohydrates`, `Fats`, and `Water`.
- Suggest caloric **deficit or surplus** based on selected fitness goals.
- Display predicted **BMI** and compare it with healthy BMI ranges.

---

## 📊 Data Understanding

The model uses a cleaned dataset and multiple regression models to predict nutrition values. User inputs are encoded and scaled, and predictions are made using a trained multi-output Random Forest model.

### ✅ Input Features

| Feature         | Description                                    | Importance                                   |
|-----------------|------------------------------------------------|----------------------------------------------|
| **Age**         | User's age in years                            | Affects BMR and metabolism                   |
| **Gender**      | Biological sex                                 | Influences calorie burn and body composition |
| **Height (cm)** | Height in centimeters                          | Used to calculate BMI and BMR                |
| **Weight (kg)** | Weight in kilograms                            | Crucial for energy expenditure               |
| **Sleep Hours** | Average sleep per day                          | Affects recovery and metabolic rate          |
| **Activity Level** | Physical activity level (Low, Moderate, High) | Major determinant of calorie needs        |
| **Fitness Goal**| Weight loss, gain, or maintenance              | Modifies caloric target accordingly          |

---

## 📥 Output

The model provides:
- **Target Calories** for goal-based intake like maintenance, weight loss & muscle gain
- **Macronutrient Breakdown**: Protein, Carbs, Fats (in grams)
- **Hydration Suggestion**: Water intake (in liters)
- **Predicted BMI**

> ℹ️ This app uses a MultiOutput Random Forest Regressor trained on lifestyle and biometric features.

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy, Scikit-learn ,Matplotlib , Sns, scipy
- Streamlit (Web App)
- Joblib (Model Saving)
- Hugging Face or Streamlit Cloud (Deployment)

---

## 🧠 Future Scope

- Integration with **wearable devices** (smartwatches, fitness trackers).
- Real-time updates and personalized dashboards.
- Adding features like **meal planning** and **macro tracking**.

---

## 📎 Author

Developed by [Subhransu Pradhan]  
Feel free to fork, modify, or deploy this for personal or academic use.

---

## 📄 License

This project is open source under the [MIT License](LICENSE).

