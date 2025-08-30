# Data case #1
import pandas as pd
import yfinance as yf

ff_daily_url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_Factors_daily_CSV.zip"
ffDaily = pd.read_csv(ff_daily_url, skiprows=3, index_col=0)
ffDaily = ffDaily.iloc[:-1]
ffDaily.index = pd.to_datetime(ffDaily.index, format='%Y%m%d')
ffDaily.to_pickle("datasets/ffDaily.pkl")

ff_monthly5_url = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip"
ffMonthly5 = pd.read_csv(ff_monthly5_url, skiprows=2, index_col=0)
ffMonthly5 = ffMonthly5.iloc[:-1]
ffMonthly5.index = pd.to_datetime(ffMonthly5.index, format='%Y%m')
ffMonthly5.to_pickle("datasets/ffMonthly5.pkl")

gdp_url = "https://www.bea.gov/sites/default/files/2025-08/gdp2q25-2nd.xlsx"
gdp = pd.read_excel(gdp_url, sheet_name='Table 1', skiprows=2)
gdp = gdp.drop(['Line', 'Unnamed: 1'], axis=1)
gdp = gdp.iloc[2]
usGDPannual = gdp.copy()
usGDPannual = usGDPannual.index.astype(str).str.split('.').str[0]
usGDPannual = gdp.groupby(gdp.index).last()
usGDPannual.index = pd.to_datetime(usGDPannual.index)
usGDPannual = usGDPannual.to_period()
usGDPannual.to_pickle("datasets/usGDPannual.pkl")

usGDPquarterly = gdp.copy()
new_index = list(gdp.index)
new_index[:2] = ['2021.3', '2021.4']
new_index[-2:] = ['2025.1', '2025.2']
usGDPquarterly.index = new_index
usGDPquarterly.to_pickle('datasets/usGDPquarterly.pkl')

dollarIndex = yf.download('DX-Y.NYB')
dollarIndex = dollarIndex.Close
dollarIndex.columns = ['Close']
dollarIndex.to_pickle('datasets/dollarIndex.pkl')

goldPriceDaily = yf.download('DX-Y.NYB', start='2024-01-01', end='2024-12-31')
goldPriceDaily = goldPriceDaily.Close
goldPriceDaily.columns = ['Close']
goldPriceDaily.to_pickle('datasets/goldPriceDaily.pkl')

goldPriceMonthly = goldPriceDaily.resample('ME').last().to_period()
goldPriceMonthly.to_pickle('datasets/goldPriceMonthly.pkl')

spread_AAA_url = "https://fred.stlouisfed.org/graph/fredgraph.csv?bgcolor=%23ebf3fb&chart_type=line&drp=0&fo=open%20sans&graph_bgcolor=%23ffffff&height=450&mode=fred&recession_bars=on&txtcolor=%23444444&ts=12&tts=12&width=752&nt=0&thu=0&trc=0&show_legend=yes&show_axis_titles=yes&show_tooltip=yes&id=AAA&scale=left&cosd=1919-01-01&coed=2025-07-01&line_color=%230073e6&link_values=false&line_style=solid&mark_type=none&mw=3&lw=3&ost=-99999&oet=99999&mma=0&fml=a&fq=Monthly&fam=avg&fgst=lin&fgsnd=2020-02-01&line_index=1&transformation=lin&vintage_date=2025-08-30&revision_date=2025-08-30&nd=1919-01-01"
spreadAAA = pd.read_csv(spread_AAA_url, index_col=0, parse_dates=[0])
spreadAAA.to_pickle('datasets/spreadAAA.pkl')

