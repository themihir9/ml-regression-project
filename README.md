# Solar_Power_Generation_Prediction_Using_Regression_Models

## 📌 Project Overview
This project predicts solar power generation using environmental and weather-related variables. Since the target variable is continuous, regression techniques are applied to build and evaluate predictive models.

## 🎯 Objective
To develop a machine learning regression model that accurately predicts solar energy production based on meteorological conditions.

## 📂 Dataset Description
- File: solarpowergeneration.csv
- Records: 2,920
- Features: 9 input variables + 1 target variable

### Features:
- Distance to solar noon
- Temperature
- Wind direction
- Wind speed
- Sky cover
- Visibility
- Humidity
- Average wind speed
- Average pressure

### Target:
- Power generated (Joules)

## 🛠️ Tools & Technologies
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

## 🔍 Exploratory Data Analysis
- Analyzed feature distributions and correlations
- Identified key factors affecting power generation
- Observed strong impact of distance to solar noon and sky cover

## ⚙️ Machine Learning Models
- Linear Regression
- Ridge Regression
- Lasso Regression
- Random Forest Regressor

## 📊 Model Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🏆 Best Model
- Random Forest Regressor achieved the highest R² score
- Distance to solar noon was the most influential feature

## ✅ Conclusion
The project successfully predicts solar power generation using regression models, with Random Forest providing the best performance. This approach can help in renewable energy planning and optimization.

## 🚀 Future Improvements
- Hyperparameter tuning
- Feature engineering
- Time-series forecasting
.
