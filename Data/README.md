# Gold Data

This folder contains historical gold price data focused on the Indian market, retrieved and processed using the **[`yfinance`](https://github.com/ranaroussi/yfinance)** Python library.

---

## 📁 Contents

- **`gold_inr_history.csv`**  
  Daily gold price data from **January 1, 2005** to **July 1, 2025**, including:
  - Spot gold prices in USD (`Gold_USD`)
  - Daily USD to INR exchange rate (`USD_INR`)
  - Converted gold price in INR (`Gold_INR`)
  - Gold price in INR per gram (`Gold_INR_per_gram`)

---

## 📊 Source

The data was fetched programmatically from **Yahoo Finance** using `yfinance`.  
Conversion to INR was calculated using daily USD-INR exchange rates for consistency and local relevance.

---

## 📌 Purpose

This folder provides a reliable, structured dataset for:
- Analyzing gold price trends in USD and INR.
- Studying the impact of exchange rate fluctuations.
- Building forecasting models for gold in the Indian context.
- Supporting broader financial research within this project.
