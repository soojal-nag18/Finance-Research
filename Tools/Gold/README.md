# Gold INR Historical Data Extractor

This script uses the [`yfinance`](https://github.com/ranaroussi/yfinance) Python library to fetch daily historical gold prices in USD and the USD to INR exchange rate. It then converts the prices to INR, calculates the per-gram gold price, and exports the result as a CSV file.

---

## 📄 Script Name

**`gold_inr_history.py`**

---

## ⚙️ What It Does

- Downloads daily gold price data (`GLD`) from Yahoo Finance.
- Downloads the daily USD/INR exchange rate (`INR=X`).
- Cleans and merges the datasets.
- Calculates:
  - **Gold price in INR** (`Gold_USD` × `USD_INR`)
  - **Gold price per gram in INR** (1 troy ounce ≈ 31.1035 grams)
- Saves the final dataset as `gold_inr_history.csv`.

---

## 📅 Date Range

- **Start Date:** 2005-01-01  
- **End Date:** Default is `today` (can be adjusted in the script).

---

## 🗂️ Output

- **File:** `gold_inr_history.csv`
- **Columns:**
  - `Gold_USD` — Gold price in USD
  - `USD_INR` — USD to INR exchange rate
  - `Gold_INR` — Converted gold price in INR
  - `Gold_INR_per_gram` — Gold price per gram in INR

---

## 📌 Notes

- The script uses the `GLD` ETF as a proxy for spot gold prices.  
  *(Note: GLD closely tracks the price of physical gold but may include slight deviations.)*
- The exchange rate is pulled from Yahoo’s `INR=X` ticker.
- `auto_adjust=True` adjusts for dividends and splits where applicable.

---

## 🔒 License

This script is provided for **educational and research purposes only**.  
Always verify Yahoo Finance’s terms of use when redistributing or publishing derived datasets.

---

**Contact:** For improvements, questions, or suggestions, please open an issue or submit a pull request in this repository.

