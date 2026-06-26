# 🏠 House Price Prediction

A machine learning project that predicts house prices based on property features such as size, number of bedrooms, and location, using a regression model trained on real estate data.

## 🎯 Objective

To build a regression model that predicts house prices using property characteristics, and evaluate how closely the predicted prices align with actual market prices.

## 📊 Dataset

- **Source:** [House Price Prediction Dataset](https://www.kaggle.com/) (Kaggle)
- **Type:** Tabular real estate data
- **Target Variable:** House sale price

## 🛠️ Project Workflow

1. **Data Preprocessing** – Clean and prepare features such as square footage, number of bedrooms, and location (e.g., encoding categorical location data, handling missing values).
2. **Feature Scaling & Selection** – Scale numerical features and select the most relevant predictors for the model.
3. **Model Training** – Train a regression model (Linear Regression / Gradient Boosting) to predict house prices.
4. **Visualization** – Plot predicted prices against actual prices to visually assess model performance.
5. **Model Evaluation** – Evaluate performance using:
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)

## 🧠 Skills Demonstrated

- Regression modeling
- Feature scaling and selection
- Model evaluation (MAE, RMSE)
- Real estate data understanding

## 📦 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| `pandas`, `numpy` | Data cleaning and manipulation |
| `scikit-learn` | Feature scaling, model training, and evaluation |
| `matplotlib`, `seaborn` | Data visualization |

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
   jupyter notebook house_price_prediction.ipynb
```

## 📈 Sample Output

The model outputs a plot comparing actual vs. predicted house prices, along with MAE and RMSE scores to quantify prediction accuracy.

## 📁 Project Structure
├── house_price_prediction.ipynb   # Main notebook with preprocessing, training, and evaluation

├── README.md                       # Project documentation

└── requirements.txt                 # Python dependencies

## 📌 Notes

- Location was treated as a categorical feature and encoded appropriately before being used in the model.
- This project is intended for educational purposes and should not be used as a substitute for professional real estate valuation.
