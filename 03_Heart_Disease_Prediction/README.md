# ❤️ Heart Disease Prediction

A machine learning project that predicts whether a person is at risk of heart disease based on their clinical and health attributes, using the UCI Heart Disease dataset.

## 🎯 Objective

To build a binary classification model that predicts the presence or absence of heart disease in a patient based on health indicators such as age, cholesterol, blood pressure, and other clinical features.

## 📊 Dataset

- **Source:** [Heart Disease UCI Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data) (Kaggle)
- **Type:** Tabular clinical/medical data
- **Target Variable:** Presence of heart disease (binary: 0 = no disease, 1 = disease)

## 🛠️ Project Workflow

1. **Data Cleaning** – Handle missing or inconsistent values in the dataset to ensure data quality.
2. **Exploratory Data Analysis (EDA)** – Analyze distributions, correlations, and trends among health features to understand relationships with heart disease risk.
3. **Model Training** – Train a classification model (Logistic Regression) to predict heart disease risk.
4. **Model Evaluation** – Assess performance using:
   - Accuracy
   - ROC Curve and AUC Score
   - Confusion Matrix
5. **Feature Importance Analysis** – Identify and visualize the health features that most strongly influence the prediction, using model coefficients.

## 🧠 Skills Demonstrated

- Binary classification
- Medical data understanding and interpretation
- Model evaluation using ROC-AUC and confusion matrix
- Feature importance analysis

## 📦 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| `pandas`, `numpy` | Data cleaning and manipulation |
| `scikit-learn` | Model training and evaluation |
| `matplotlib`, `seaborn` | EDA visualizations and plotting |

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### Running the Project

1. Clone the repository:
```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
```
2. Run the notebook:
```bash
   jupyter notebook heart_disease_prediction.ipynb
```

## 📈 Sample Output

The model outputs:
- A confusion matrix showing true/false positives and negatives
- An ROC curve with the AUC score, illustrating the model's ability to distinguish between patients with and without heart disease
- A feature importance plot highlighting which clinical attributes (e.g., chest pain type, maximum heart rate, cholesterol) most influence predictions

## 📁 Project Structure
```
├── heart_disease_prediction.ipynb   # Main notebook with EDA, training, and evaluation
├── README.md                        # Project documentation
└── requirements.txt                  # Python dependencies
```

## 📌 Notes

- Since the original target variable can be multiclass, it was binarized (disease vs. no disease) to enable standard binary classification metrics like the ROC curve and AUC.
- This project is intended for educational purposes and should not be used as a substitute for professional medical diagnosis.
