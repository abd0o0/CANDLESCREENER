import os, csv
import talib
import yfinance as yf
import pandas as pd
from flask import Flask, request, render_template
from patterns import candlestick_patterns

app = Flask(__name__)

@app.route('/snapshot')
def snapshot():
    with open('datasets/symbols.csv') as f:
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start="2025-01-01", end="2025-02-06")
            data.to_csv('datasets/daily/{}.csv'.format(symbol))

    return {
        "code": "success"
    }

@app.route('/')
def index():
    pattern = request.args.get('pattern', False)
    stocks = {}

    with open('datasets/symbols.csv') as f:
        for row in csv.reader(f):
            stocks[row[0]] = {'company': row[1]}

    if pattern:
        print(f"Pattern selected: {pattern}")
        for filename in os.listdir('datasets/daily'):
            df = pd.read_csv(f'datasets/daily/{filename}', skiprows=3)  # Skip the first 3 rows
            df = df.dropna()  # Drop rows with missing values
            df['Open'] = pd.to_numeric(df['Open'], errors='coerce')
            df['High'] = pd.to_numeric(df['High'], errors='coerce')
            df['Low'] = pd.to_numeric(df['Low'], errors='coerce')
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
            df = df.dropna()  # Drop rows with non-numeric values
            pattern_function = getattr(talib, pattern)
            symbol = filename.split('.')[0]

            try:
                results = pattern_function(df['Open'].values, df['High'].values, df['Low'].values, df['Close'].values)
                last = results[-1]
                print(f"Symbol: {symbol}, Last pattern result: {last}")

                if last > 0:
                    stocks[symbol][pattern] = 'bullish'
                elif last < 0:
                    stocks[symbol][pattern] = 'bearish'
                else:
                    stocks[symbol][pattern] = None
            except Exception as e:
                print(f"Error processing {symbol}: {e}")

    print(f"Stocks: {stocks}")

    return render_template('index.html', pattern=pattern, stocks=stocks, candlestick_patterns=candlestick_patterns)

if __name__ == '__main__':
    app.run(debug=True)
