import pandas as pd
import numpy as np

df = pd.read_csv('./salesmen.csv', index_col=0, parse_dates=True)
df_bob = df[df['Salesman'] == 'Bob']
df_bob['2DayRaise'] = np.log(df_bob['Revenue'] / df_bob['Revenue'].shift(2))
df_bob['2DayAvg'] = df_bob['Revenue'].shift(1).rolling(2).mean()
df_bob['2DayAvgRaise'] = np.log(df_bob['Revenue'] / df_bob['2DayAvg'])

print(df_bob.tail())
