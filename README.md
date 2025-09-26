
# CANDLESCREENER

## Overview
CANDLESCREENER is a Python tool I built to scan financial markets for candlestick patterns, identifying trading signals in stocks or cryptocurrencies. It analyzes OHLCV (Open, High, Low, Close, Volume) data to detect patterns like Doji, Hammer, or Engulfing, using TA-Lib for accuracy. With support for real-time or historical data, it’s designed for backtesting and live screening, showcasing my skills in algorithmic trading, data analysis, and automation—perfect for fintech portfolios.

**Disclaimer**: For educational use only. Trading carries risks; not financial advice. Test thoroughly before use.

## Features
- **Pattern Detection**: Identifies 20+ candlestick patterns (e.g., Bullish Engulfing, Bearish Harami) via TA-Lib.
- **Data Sources**: Integrates yfinance (stocks) or CCXT (crypto) for market data.
- **Multi-Timeframe**: Scans from 1-minute to daily charts across multiple assets.
- **Visualization**: Plots candlesticks with pattern markers using mplfinance.
- **Alerts**: Configurable notifications (email or console) for detected patterns.
- **CLI & API**: Easy command-line use or programmatic integration with trading bots.

## Tech Stack
- **Language**: Python 3.10+
- **Key Libraries**:
  - `pandas`, `numpy` for data processing.
  - `talib` for technical analysis.
  - `yfinance`, `ccxt` for market data.
  - `mplfinance` for charting.
  - `click` for CLI.
- Lightweight; runs locally with minimal setup.

## Getting Started

### Prerequisites
- Python 3.10+.
- Git for cloning.
- (Optional) API keys for crypto exchanges (e.g., Binance for CCXT).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/abd0o0/CANDLESCREENER.git
   cd CANDLESCREENER
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. (Optional) Configure environment variables (create `.env` in the root):
   ```
   SYMBOLS=AAPL,TSLA,BTCUSDT
   TIMEFRAME=1d
   ALERT_EMAIL=your.email@example.com
   ```

### Usage
1. **CLI Scan**:
   ```bash
   python screener.py scan --symbols AAPL,BTCUSDT --timeframe 1d --patterns doji,hammer
   ```
   Outputs detected patterns (e.g., "BTCUSDT: Doji on 2025-09-25").

2. **Programmatic Use**:
   ```python
   from candlescreener import CandleScreener

   # Initialize screener
   screener = CandleScreener(symbols=['AAPL'], timeframe='1d')

   # Scan for patterns
   results = screener.scan(patterns=['engulfing', 'doji'])
   for symbol, patterns in results.items():
       if patterns:
           print(f"{symbol}: {patterns}")
   ```

3. **Plot Patterns**:
   ```bash
   python screener.py plot --symbol TSLA --pattern engulfing
   ```
   Displays a candlestick chart with pattern highlights.

*See `/examples` for scripts and `/docs` for pattern details.*

