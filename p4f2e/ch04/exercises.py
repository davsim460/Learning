#1. From yahoo finance

#2. No we can download the prices and calculate the returns. But sometimes we may get the simple returns.

#3. pass

#4.
import yfinance as yf
data = yf.download("C")
data.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
ret = data.Close / data.Close.shift() - 1

#5.
data = yf.download("C", start='2024-01-01')
data.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
# Convert monthly prices to monthly returns
month_agg = data.Close.resample('ME').last().to_period()
mret = month_agg / month_agg.shift() - 1
# Convert daily returns to monthly returns
dret = data.Close / data.Close.shift() - 1
(1+dret).resample('ME').prod() - 1
# Yes there are same.

#6. No there is a mistake in the second formula it should be ... / p.aclose[:-1]

#7. Public - easy access but low data frequency. Private - Data accuracy, intraday data but higher costs

#8. It's not publicly disclosed but regarding Compustat the ChatGPT brings 15000-20000 USD

#9.
data = yf.download("IBM", start='2000-01-01', end='2004-12-31')
data.columns = ['Close', 'High', 'Low', 'Open', 'Volume']
data = data.Close
ret = data.pct_change()
# Assuming risk-free rate = 0
rf = 0
std = ret.std()
sharpe_ratio = (ret.mean() - rf) / std

#10.
