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
data = pd.DataFrame(data.Close)
ret = data.pct_change()
# Assuming risk-free rate = 0
rf = 0
std = ret.std()
sharpe_ratio = (ret.mean() - rf) / std

#10.
start_date = '2001-01-01'
end_date = '2010-12-31'

SP500 = yf.download('^GSPC', start=start_date, end=end_date)
IBM = yf.download('IBM', start=start_date, end=end_date)
MSFT = yf.download('MSFT', start=start_date, end=end_date)

SP500 = SP500.Close
IBM = IBM.Close
MSFT = MSFT.Close

SP500.columns = ['Close']
IBM.columns = ['Close']
MSFT.columns = ['Close']

SP500['Ret'] = SP500.pct_change()
IBM['Ret'] = IBM.pct_change()
MSFT['Ret'] = MSFT.pct_change()

SP500.dropna(inplace=True)
IBM.dropna(inplace=True)
MSFT.dropna(inplace=True)

years = range(2001, 2011)

def get_annual_beta(year, asset, market):
    cov = asset.loc[str(year), 'Ret'].cov(market.loc[str(year), 'Ret'])
    var = market.loc[str(year), 'Ret'].var()
    return cov / var

betas = pd.DataFrame(index=years)
betas['IBM'] = [get_annual_beta(year, IBM, SP500) for year in years]
betas['MSFT'] = [get_annual_beta(year, MSFT, SP500) for year in years]

#11.
IBM.loc['2006':, 'Ret'].corr(SP500.loc['2006':, 'Ret'])

#12.
IBM.Ret.groupby(IBM.index.weekday).mean()

#13.
import numpy as np
import matplotlib.pyplot as plt
IBM_std = IBM.Ret.groupby(IBM.index.year).std() * np.sqrt(252)
MSFT_std = MSFT.Ret.groupby(MSFT.index.year).std() * np.sqrt(252)

plt.figure(figsize=(10, 6))
IBM_std.plot()
MSFT_std.plot()
plt.show()
# It seems like it's true

#14.
DJI = yf.download('^DJI', start=start_date, end=end_date)
DJI = pd.DataFrame(DJI.Close)
DJI.columns = ['Close']
DJI['Ret'] = DJI.pct_change()
DJI.dropna(inplace=True)
SP500.Ret.corr(DJI.Ret)

#15.
tickers = ['IBM', 'MSFT'] # ...
yf.download(tickers)

#16. I have the task with Python
tickers_file = open("data/tickers.txt", "r")
tickers = [ticker.strip() for ticker in tickers_file.readlines()]
tickers_file.close()

#17.
HSI = yf.download('^HSI', start=start_date, end=end_date)
HSI = pd.DataFrame(HSI.Close)
HSI.columns = ['Close']
HSI['Ret'] = HSI.pct_change()
SP500.Ret.corr(HSI.Ret)

#18.
NIK = yf.download('^N225', start=start_date, end=end_date)
STI = yf.download('^STI', start=start_date, end=end_date)

NIK = pd.DataFrame(NIK.Close)
STI = pd.DataFrame(STI.Close)

NIK.columns = ['Close']
STI.columns = ['Close']

NIK['Ret'] = NIK.pct_change()
STI['Ret'] = STI.pct_change()

NIK.dropna(inplace=True)
STI.dropna(inplace=True)
# Yes it's true

#19.
prices = yf.download(['MSFT', 'IBM'], start=start_date, end=end_date) # ...
prices.to_csv('data/prices.csv')

#20. The first one is simple returns formula which we need to understand the performance,
#the second one is the inverse return which we do not need usually



