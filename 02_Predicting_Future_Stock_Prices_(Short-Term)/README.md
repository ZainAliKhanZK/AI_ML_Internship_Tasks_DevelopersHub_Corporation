# 📈 Stock Price Prediction (Short-Term)

A machine learning project that predicts the next-day closing price of a financial asset — stocks or gold — using historical market data fetched directly from Yahoo Finance.

## 🎯 Objective

To use historical price data to predict the next day's closing price based on an asset's daily trading features (Open, High, Low, Volume), and visually compare predicted prices against actual closing prices. This project was tested on both equities (e.g., Apple, Tesla) and the Gold futures ticker (`GC=F`).

## 📊 Dataset

- **Source:** [Yahoo Finance](https://finance.yahoo.com/)
- **Access Method:** [`yfinance`](https://pypi.org/project/yfinance/) Python library
- **Data Type:** Historical daily OHLCV (Open, High, Low, Close, Volume) stock data

## 🛠️ Project Workflow

1. **Asset Selection** – Choose a publicly traded stock (e.g., Apple `AAPL`, Tesla `TSLA`) or a commodity such as Gold (`GC=F`) for analysis.
2. **Data Collection** – Fetch historical stock data using the `yfinance` API.
3. **Feature Engineering** – Use `Open`, `High`, `Low`, and `Volume` as input features to predict the `Close` price.
4. **Train/Test Split** – Split the data chronologically (preserving time order) to avoid lookahead bias.
5. **Model Training** – Train a regression model (Linear Regression / Random Forest) on the training data.
6. **Evaluation & Visualization** – Plot actual vs. predicted closing prices to visually assess model performance.

## 🧠 Skills Demonstrated

- Time series data handling
- Regression modeling (Linear Regression / Random Forest)
- Data fetching using APIs (`yfinance`)
- Data visualization (actual vs. predicted price plots)

## 📦 Tech Stack

| Tool / Library | Purpose |
|---|---|
| Python | Core programming language |
| `yfinance` | Fetching historical stock data |
| `pandas`, `numpy` | Data manipulation and preprocessing |
| `scikit-learn` | Regression modeling |
| `matplotlib` | Data visualization |

## 🚀 Getting Started

### Prerequisites

```bash
pip install yfinance pandas numpy scikit-learn matplotlib
```

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
2. Run the notebook or script:
   ```bash
   jupyter notebook stock_price_prediction.ipynb
   ```
3. Modify the ticker symbol (e.g., `AAPL`, `TSLA`, or `GC=F` for Gold) to predict prices for a different asset.

## 📈 Sample Output

The model outputs a plot comparing the actual closing prices against the predicted closing prices over the test period, allowing for a visual assessment of prediction accuracy.

## 📁 Project Structure

```
├── stock_price_prediction.ipynb   # Main notebook with data fetching, training, and evaluation
├── README.md                      # Project documentation
└── requirements.txt                # Python dependencies
```

## 📌 Notes

- Stock prices are inherently noisy and influenced by external factors not captured in OHLCV data alone; this project is intended for educational purposes and not financial advice.
- A chronological (time-aware) train/test split is used instead of random shuffling, since shuffling time series data can leak future information into training and produce misleadingly optimistic results.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
