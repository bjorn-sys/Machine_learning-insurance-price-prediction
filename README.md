
INSURANCE CHARGES PREDICTION - README

PROJECT OVERVIEW

This project predicts individual medical insurance charges based on demographic and health-related data. The objective is to identify the most impactful features on cost and to build an accurate model for predicting charges.


---

LIBRARIES USED

NumPy – for numerical operations

Pandas – for data manipulation and analysis

Matplotlib – for data visualization

Seaborn – for statistical graphics

Scikit-learn – for machine learning models and evaluation

LinearRegression

SVR

RandomForestRegressor

GradientBoostingRegressor

train_test_split, cross_val_score, r2_score

LabelEncoder


XGBoost – for optimized gradient boosting

Pickle – for saving and loading the trained model



---

DATASET SUMMARY

Rows: 1,328 (after cleaning)

Columns: 7

Target: charges (annual medical insurance cost)


FEATURES:

age: Age in years

sex: 0 = Male, 1 = Female

bmi: Body Mass Index

children: Number of dependents covered by insurance

smoker: 1 = Smoker, 0 = Non-smoker

region: 0 = northwest, 1 = northeast, 2 = southeast, 3 = southwest



---

EXPLORATORY DATA ANALYSIS (EDA)

CATEGORICAL INSIGHTS:

Sex is roughly balanced (about 50/50 male/female)

About 20% of the individuals are smokers

Southeast region has the highest representation


NUMERICAL INSIGHTS:

Age vs Charges: Costs increase exponentially with age, more so for smokers

BMI vs Charges: Charges increase with higher BMI, especially among smokers

Children vs Charges: A slight positive correlation

Smoker vs Charges: Smokers have drastically higher costs than non-smokers


CORRELATION WITH CHARGES:

Smoker: +0.79

Age: +0.30

BMI: +0.20

Children: +0.07

Sex: ~0.00


Key insight: Smoking status is by far the most influential factor on insurance costs.


---

DISTRIBUTION ANALYSIS

Charges are right-skewed (most under $15,000, with some over $50,000)

BMI is normally distributed; outliers were removed using IQR

Age is evenly distributed between 18 and 64



---

DATA PREPROCESSING

Removed 1 duplicate and missing values

Label-encoded categorical features

Removed BMI outliers using IQR

No scaling applied (not needed for tree-based models)



---

MODEL COMPARISON & RESULTS

Final model: XGBoost Regressor
Hyperparameters:

n_estimators=15

max_depth=3

gamma=0



---

FEATURE IMPORTANCE (XGBoost)

Smoker: 81%

BMI: 11%

Age: 5%

Children: 1%


Smoker status is the dominant predictor of charges.


---

RESIDUAL ANALYSIS

Residuals follow an approximately normal distribution

No major signs of heteroscedasticity (variance is constant)

Indicates a good model fit



---

INSIGHTS FROM GROUPED DATA

Average Charges by Smoking Status:

Smokers: ~$32,000

Non-smokers: ~$8,400
(Smokers pay ~3.8x more)


Average Charges by Age Range:

18–30: ~$7,000

31–45: ~$11,500

46–60: ~$18,000

60+: ~$21,000


Average Charges by BMI Group:

BMI < 25: ~$9,500

BMI 25–30: ~$12,000

BMI > 30: ~$16,000



---

MODEL TESTING EXAMPLE

Input:

age: 29

sex: 1

bmi: 30.9

children: 0

smoker: 1

region: 1


Predicted Charges: $37,213.40


---

BUSINESS RECOMMENDATIONS

1. Implement differential pricing for smokers (higher premiums)


2. Incentivize healthy BMI via discounts or rewards


3. Focus on preventive healthcare for older age groups


4. Consider a dynamic, data-driven pricing tool for insurance quoting




---

MODEL DEPLOYMENT

Saved using Pickle:

from pickle import dump
dump(finalmodel, open('insurancemodelf.pkl', 'wb'))

