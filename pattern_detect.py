import talib
import yfinance as yf

data = yf.download("SPY", start="2020-01-01", end="2020-08-01")

# Convert DataFrame columns to 1-dimensional numpy arrays
open_prices = data['Open'].values.flatten()
high_prices = data['High'].values.flatten()
low_prices = data['Low'].values.flatten()
close_prices = data['Close'].values.flatten()

morning_star = talib.CDLMORNINGSTAR(open_prices, high_prices, low_prices, close_prices)
engulfing = talib.CDLENGULFING(open_prices, high_prices, low_prices, close_prices)

data['Morning Star'] = morning_star
data['Engulfing'] = engulfing

engulfing_days = data[data['Engulfing'] != 0]

print(engulfing_days)