---

# 🏥 Insurance Charges Prediction - README

# 📊 Project Overview

* This project predicts individual medical insurance charges using demographic and health-related data. The goal is to understand which features most influence insurance cost and build a robust predictive model that generalizes well to new data.


---

# 📚 Libraries Used

* Pandas – Data manipulation and analysis

* NumPy – Numerical computing

* Matplotlib – Plotting and visualization

* Seaborn – Statistical visualization

* Scikit-learn – Machine learning models and utilities

* Models: LinearRegression, SVR, RandomForestRegressor, GradientBoostingRegressor

* Tools: train_test_split, cross_val_score, r2_score, LabelEncoder


* XGBoost – Optimized gradient boosting model

* Pickle – Model persistence and deployment



---

# 📁 Dataset Summary

* Rows: 1,328 (after cleaning)

* Columns: 7

* Target: charges (annual medical insurance cost)


**Features:**

* age: Age in years

* sex: 0 = Male, 1 = Female

* bmi: Body Mass Index

* children: Number of dependents covered

* smoker: 1 = Smoker, 0 = Non-smoker

* region: 0 = northwest, 1 = northeast, 2 = southeast, 3 = southwest



---

# 🔍 Exploratory Data Analysis (EDA)

**👥 Categorical Analysis**

* Sex: Balanced dataset (50/50)

* Smoker: ~20% of individuals are smokers

* Region: Southeast is the most common region


# 📈 Numerical Trends

**Age vs Charges:**
* Charges increase steeply with age, especially for smokers. Elderly smokers face the highest premiums.

**BMI vs Charges:**
* A curvilinear relationship—charges rise faster for BMIs above 30. Obesity contributes to higher risk factors.

**Children vs Charges:**
* Small positive relationship. Having more dependents slightly increases insurance costs.

**Smoker vs Charges:**
* The most dramatic trend. Smokers can incur charges 3–4 times higher than non-smokers.


# 🧮 Correlation Matrix (Top Correlated to charges):

* smoker: +0.79

* age: +0.30

* bmi: +0.20

* children: +0.07

* sex: ~0.00


**Insight: Smoking status dominates the relationship with insurance costs, dwarfing other features.**




---

# 📉 Distribution Analysis

* Charges: Right-skewed. Most values under **$15,000** some exceed **$50,000** (smoking-driven).

* BMI: Approximately normal. Outliers (extreme obesity) removed via IQR filtering.

* Age: Uniformly spread between 18 and 64, ensuring broad demographic coverage.



---

# 🔧 Data Preprocessing

* ✅ Removed missing values and 1 duplicate
* ✅ Label-encoded categorical variables (sex, smoker, region)
* ✅ Removed outliers in bmi using IQR
* ❌ No scaling applied (not required for tree-based models like Random Forest, XGBoost)


---

# 🧠 Model Building & Evaluation

* Models Compared:

* Linear Regression

* Support Vector Regressor (SVR)

* Random Forest Regressor

* Gradient Boosting Regressor

* XGBoost Regressor ✅ (Final Model)


**Hyperparameters for Final Model:**

* XGBRegressor(n_estimators=15, max_depth=3, gamma=0)

**Performance Summary:**
| Model                | Train R² | Test R² | CV R²   |
|----------------------|----------|---------|---------|
| Linear Regression    | 0.75     | 0.74    | 0.74    |
| SVR                  | -0.10    | -0.09   | -0.10   |
| Random Forest        | 0.98     | 0.81    | 0.83    |
| Gradient Boosting    | 0.89     | 0.85    | 0.86    |
| XGBoost (Final)  | 0.88     | 0.85    | 0.86    |

**🔍 Insight: XGBoost outperformed all other models in terms of generalization and test accuracy.**




---

# 🏁 Final Model Insights

**🔬 Feature Importance (XGBoost)**

* smoker: 81%

* bmi: 11%

* age: 5%

* children: ~1%

* 🔍 Smoking status alone accounts for 80%+ of the model’s predictive power.



# 🔍 Residual Analysis

* Residuals are normally distributed (bell-shaped curve)

* No clear heteroscedasticity → consistent variance in errors across prediction range

* Indicates the model is well-calibrated and unbiased



---

# 📊 Additional Cost Insights

**💰 Cost by Smoker Status**

* Smokers: **$32,000** average

* Non-smokers: **$8,400** average

* Smoking multiplies insurance cost by ~3.8x



# 📅 Cost by Age Group

* Age 18–30: **$7,000**

* Age 31–45: **$11,500**

* Age 46–60: **$18,000**

* Age 60+: **$21,000**


# ⚖️ Cost by BMI Category

* BMI < 25: ~$9,500

* BMI 25–30: ~$12,000

* BMI > 30: ~$16,000


**Obesity adds approximately 70% more to predicted charges.**




---

# 🧪 Testing on New Data

new_data = pd.DataFrame({
  'age': 29,
  'sex': 1,
  'bmi': 30.9,
  'children': 0,
  'smoker': 1,
  'region': 1
}, index=[0])

charges = finalmodel.predict(new_data)
print(charges)

Predicted Charge: **$37,213.40**


---

# 💡 Business Recommendations

1. Charge More for Smokers: Use tiered pricing plans. Consider legal and ethical constraints.


2. Health Incentives: Offer premium reductions for maintaining BMI < 25 or quitting smoking.


3. Preventive Care: Introduce wellness programs for adults 40+ to reduce long-term claims.


4. Real-time Premium Pricing: Use predictive models to give instant quotes based on user inputs.




---

# 📁 Model Deployment

Model was saved using Pickle:

from pickle import dump
dump(finalmodel, open('insurancemodelf.pkl', 'wb'))
