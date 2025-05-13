import pandas as pd
import numpy as np

df = pd.read_csv('./finance/tesla.csv')
df.set_index('Date', inplace=True)

# print(pd.concat([df['Close'], df['Close'].shift(2)], axis=1,keys=['Close','2DayShift']))
# print((df['Close'] - df['Close'].shift(2))/df['Close'].shift(2))
df['2DayRaise'] = np.log(df['Close'] / df['Close'].shift(2))
# print(df[['Close','2DayRaise']])
df['2DayAvg'] = df['Close'].shift(1).rolling(2).mean()
# print(df[['Close','2DayRaise','2DayAvg']])
df['2DayAvg'] = np.log(df['Close'] / df['2DayAvg'])

