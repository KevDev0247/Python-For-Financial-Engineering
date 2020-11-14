from matplotlib import style
import pandas as pd

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates = True, index_col = 0)

df['100ma'] = df['Adj Close'].rolling(window = 100).mean()

print(df.head())