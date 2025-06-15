import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
from sklearn.metrics import mean_squared_error, r2_score
import shap

# Load data
df = pd.read_csv('historical_claims.csv')

# Filter for policies with claims > 0 (for claim severity prediction)
df_claims = df[df['TotalClaims'] > 0].copy()

# Handle missing values (drop rows with missing critical data)
df_claims = df_claims.dropna(subset=['TotalClaims', 'TotalPremium', 'Province', 'Gender', 'Make', 'Model', 'PostalCode'])

# Feature engineering example
df_claims['VehicleAge'] = 2025 - df_claims['RegistrationYear']

# Encode categorical variables using one-hot encoding
cat_vars = ['Province', 'Gender', 'Make', 'Model', 'PostalCode']
df_encoded = pd.get_dummies(df_claims, columns=cat_vars, drop_first=True)

# Define features and target
features = [col for col in df_encoded.columns if col not in ['TotalClaims', 'TotalPremium', 'PolicyID', 'UnderwrittenCoverID']]
X = df_encoded[features]
y = df_encoded['TotalClaims']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize models
lr = LinearRegression()
rf = RandomForestRegressor(random_state=42, n_estimators=100)
xgboost_model = xgb.XGBRegressor(objective='reg:squarederror', random_state=42)

# Train models
lr.fit(X_train, y_train)
rf.fit(X_train, y_train)
xgboost_model.fit(X_train, y_train)

# Predict
y_pred_lr = lr.predict(X_test)
y_pred_rf = rf.predict(X_test)
y_pred_xgb = xgboost_model.predict(X_test)

# Evaluate
def evaluate_model(y_true, y_pred, model_name):
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    print(f"{model_name} - RMSE: {rmse:.2f}, R2: {r2:.2f}")

evaluate_model(y_test, y_pred_lr, "Linear Regression")
evaluate_model(y_test, y_pred_rf, "Random Forest")
evaluate_model(y_test, y_pred_xgb, "XGBoost")

# SHAP interpretation for best model (assuming XGBoost)
explainer = shap.Explainer(xgboost_model, X_train)
shap_values = explainer(X_test)

# Plot summary (uncomment if running locally with GUI support)
# shap.summary_plot(shap_values, X_test)

# Print top 10 features by mean absolute SHAP value
shap_importance = np.abs(shap_values.values).mean(axis=0)
feature_importance = pd.DataFrame({'feature': X_train.columns, 'importance': shap_importance})
feature_importance = feature_importance.sort_values(by='importance', ascending=False).head(10)
print("\nTop 10 Important Features according to SHAP values:")
print(feature_importance)
