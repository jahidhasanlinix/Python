import pandas as pd
import quandl

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]
df['Percentage'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['Percentage_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'Percentage', 'Percentage_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999,)