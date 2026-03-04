# 💳 Credit Risk Prediction

A complete end-to-end Data Science project that predicts whether a credit application is **low risk (good)** or **high risk (bad)** — from raw data exploration all the way to a deployed interactive web application.

---

## 🎯 Project Overview

Banks and financial institutions need to evaluate the risk of lending money to applicants. This project builds a machine learning pipeline trained on the **German Credit Risk dataset** to automatically classify credit applications, and exposes the model through a clean **Streamlit web app** where anyone can input applicant details and get an instant prediction.

---

## 🖥️ App Demo

| Input applicant info | Get instant prediction |
|---|---|
| Age, sex, job, housing, saving & checking accounts, credit amount, duration | ✅ Good (low risk) or ❌ Bad (high risk) with model confidence |

To run the app locally, see the [Getting Started](#-getting-started) section below.

---

## 📁 Project Structure

```
credit_risk/
│
├── credit_risk_model.ipynb       # Full data science pipeline (EDA → modeling → export)
├── app.py                        # Streamlit web application
│
├── german_credit_data.csv        # Raw dataset (source: Kaggle)
│
├── extra_trees_credit_model.pkl  # Trained model (best performer)
├── Sex_encoder.pkl               # Label encoders for categorical features
├── Housing_encoder.pkl
├── Saving accounts_encoder.pkl
├── Checking account_encoder.pkl
└── target_encoder.pkl            # Label encoder for the target variable
```

---

## 📊 Dataset

- **Source:** [German Credit Risk — Kaggle](https://www.kaggle.com/datasets/uciml/german-credit)
- **Size:** 1,000 rows × 11 columns (after cleaning: ~520 rows)
- **Target column:** `Risk` → `good` (low risk) / `bad` (high risk)

| Feature | Type | Description |
|---|---|---|
| Age | Numeric | Applicant age |
| Sex | Categorical | male / female |
| Job | Numeric | 0 (unskilled) → 3 (highly skilled) |
| Housing | Categorical | own / rent / free |
| Saving accounts | Categorical | little / moderate / quite rich / rich |
| Checking account | Categorical | little / moderate / rich |
| Credit amount | Numeric | Loan amount in € |
| Duration | Numeric | Loan duration in months |
| Risk | **Target** | good (low risk) / bad (high risk) |

> Rows with missing values in `Saving accounts` or `Checking account` were dropped, as these are considered essential features for credit evaluation.

---

## 🔬 Data Science Pipeline

### 1. Exploratory Data Analysis (EDA)
- Distribution of numerical features (Age, Credit amount, Duration) via histograms and boxplots
- Distribution of categorical features via count plots
- Correlation matrix to identify relationships between variables
- Cross-analyses: average credit amount by job type and sex, pivot tables by housing and purpose
- Risk-split visualizations to understand which features drive credit risk

### 2. Feature Engineering
- Selected 8 relevant features out of 11 original columns
- Applied **Label Encoding** to categorical variables (Sex, Housing, Saving accounts, Checking account)
- Encoded the target variable: `good = 1` (low risk), `bad = 0` (high risk)
- All encoders saved as `.pkl` files for reuse in the web app
- No feature scaling applied — tree-based models do not require it

### 3. Modeling & Hyperparameter Tuning
Four tree-based classifiers were trained and tuned using **GridSearchCV (5-fold cross-validation)**. Class imbalance (~55% good / ~44% bad) was handled with `class_weight='balanced'` or `scale_pos_weight`.

| Model | Accuracy |
|---|---|
| Decision Tree | ~0.58 |
| Random Forest | ~0.61 |
| XGBoost | ~0.63 |
| **Extra Trees** ⭐ | **~0.66** |

**Extra Trees Classifier** was selected as the final model for its best accuracy on the test set.

> Extra Trees is an ensemble of decision trees that uses random splits, which reduces overfitting and variance. It is similar to Random Forest but more randomized, making it faster and often more accurate on tabular data.

---

## 🚀 Getting Started

### Prerequisites

Install the required libraries:

```bash
pip install streamlit pandas scikit-learn xgboost joblib
```

### Run the notebook

Open `credit_risk_model.ipynb` in Jupyter and run all cells top to bottom. This will:
- Train and evaluate all models
- Export the `.pkl` files needed by the app

### Launch the web app

**Option 1 — from terminal:**
```bash
streamlit run app.py
```

**Option 2 — from Jupyter notebook:**
```python
import subprocess
subprocess.Popen(["streamlit", "run", "app.py"])
```

Then open your browser at **http://localhost:8501**

---

## 🛠️ Tech Stack

| Tool | Usage |
|---|---|
| Python 3.10+ | Core language |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | Modeling, encoding, evaluation |
| XGBoost | Gradient boosting model |
| Joblib | Model & encoder serialization |
| Streamlit | Web application |
| Jupyter Notebook | Development environment |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
