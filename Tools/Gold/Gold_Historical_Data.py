import yfinance as yf  # Import yfinance library
import pandas as pd    # Import pandas for DataFrame
from datetime import datetime  # Import datetime module

today = datetime.today().strftime('2025-07-01')  # Set end date manually

# Download gold price data
gold = yf.download('GLD', start='2005-01-01', end=today, interval='1d', auto_adjust=True)

# Download USD to INR rates
usd_inr = yf.download('INR=X', start='2005-01-01', end=today, interval='1d', auto_adjust=True)

# Check for empty downloads
if gold.empty or usd_inr.empty:
    print("Download failed. Try adjusting ticker or date range.")  # Notify if download fails
else:
    data = pd.DataFrame()  # Create empty DataFrame
    data['Gold_USD'] = gold['Close']  # Add gold USD column
    data['USD_INR'] = usd_inr['Close']  # Add USD-INR rate column
    data.dropna(inplace=True)  # Drop missing rows
    data['Gold_INR'] = data['Gold_USD'] * data['USD_INR']  # Calculate gold price INR
    data['Gold_INR_per_gram'] = data['Gold_INR'] / 31.1035  # Convert to INR per gram

    data.to_csv('gold_inr_history.csv')  # Save DataFrame to CSV
    print(f"Saved gold_inr_history.csv with {len(data)} rows.")  # Confirm save success
