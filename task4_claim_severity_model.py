import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import shap

# Load dataset
df = pd.read_csv('cleaned_MachineLearningRating.csv')

# Filter to policies with claims > 0 for severity prediction
df_severity = df[df['TotalClaims'] > 0].copy()

# Select relevant features (example: numerical + some categorical)
features = ['CalculatedPremiumPerTerm', 'SumInsured', 'RegistrationYear', 
            'Cylinders', 'cubiccapacity', 'kilowatts', 'NumberOfDoors',
            'NewVehicle', 'WrittenOff', 'AlarmImmobiliser', 'TrackingDevice']

# Convert categorical boolean columns to numeric
for col in ['NewVehicle', 'WrittenOff', 'AlarmImmobiliser', 'TrackingDevice']:
    df_severity[col] = df_severity[col].astype(int)

# Target variable
target = 'TotalClaims'

X = df_severity[features]
y = df_severity[target]

# Handle missing values by simple imputation (mean)
X = X.fillna(X.mean())

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# Random Forest Regressor
rf = RandomForestRegressor(random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# XGBoost Regressor
xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', random_state=42)
xg_reg.fit(X_train, y_train)
y_pred_xgb = xg_reg.predict(X_test)

# Evaluation function
def evaluate(y_true, y_pred, model_name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} - RMSE: {rmse:.2f}, R-squared: {r2:.4f}")

print("Model Performance on Test Set:")
evaluate(y_test, y_pred_lr, "Linear Regression")
evaluate(y_test, y_pred_rf, "Random Forest")
evaluate(y_test, y_pred_xgb, "XGBoost")

# SHAP feature importance for XGBoost (best performing)
explainer = shap.Explainer(xg_reg)
shap_values = explainer(X_test)

# Summary plot (this will open a plot window)
shap.summary_plot(shap_values, X_test)
