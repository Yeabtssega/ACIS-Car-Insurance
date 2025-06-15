# AlphaCare Insurance Solutions (ACIS) Car Insurance Analytics Project

## Overview
This project analyses historical car insurance claims data from South Africa to optimize marketing strategies and develop a dynamic, risk-based pricing system. The goals are to identify key risk drivers and build predictive models for claim severity and premium pricing.

---

## Task 3: Hypothesis Testing

We tested the following null hypotheses using A/B testing and statistical tests:

1. **No risk differences across provinces**  
   - Rejected the null hypothesis (p < 0.05), indicating significant risk variation between provinces.

2. **No risk differences across postal codes**  
   - Rejected the null hypothesis (p < 0.05), showing that risk varies significantly by postal code.

3. **No margin differences between postal codes**  
   - Rejected the null hypothesis for the top two postal codes (p < 0.05), implying margin (profit) differences exist by location.

4. **No risk differences between Women and Men**  
   - Failed to reject the null hypothesis (p >= 0.05), suggesting no significant gender-based risk difference.

**Business Insight:**  
Premiums should be adjusted regionally based on province and postal code risk levels. Gender does not appear to affect claim risk significantly.

---

## Task 4: Predictive Modeling

We built and evaluated three models to predict claim severity (total claim amount for policies with claims):

- **Linear Regression**  
- **Random Forest Regressor**  
- **XGBoost Regressor**

| Model              | RMSE     | R-squared |
|--------------------|----------|-----------|
| Linear Regression  | *value*  | *value*   |
| Random Forest      | *value*  | *value*   |
| XGBoost            | *value*  | *value*   |

(*Values will appear from running the models*)

**Feature Importance (XGBoost model, top 10):**

| Feature            | Importance |
|--------------------|------------|
| *Feature name*     | *value*    |
| ...                | ...        |

**Interpretation:**  
For example, vehicle age and province significantly influence claim severity. Older vehicles and certain provinces correlate with higher claim amounts, informing premium pricing.

---

## Recommendations

- Adjust premiums dynamically by incorporating province and postal code risk factors.
- Focus marketing efforts on low-risk regions identified in the analysis to attract clients with potentially lower premiums.
- Consider implementing machine learning-based premium predictions in the underwriting process.
- Continue monitoring gender-related risks but currently gender-based adjustments are not recommended.

---

## Limitations and Future Work

- Data covers Feb 2014 - Aug 2015 only; more recent data would improve models.
- More advanced feature engineering and hyperparameter tuning could enhance predictive performance.
- Expanding to model claim probability alongside severity would enable full risk-based premium calculations.

---

*Report prepared by: [Your Name]*  
*Date: June 2025*
