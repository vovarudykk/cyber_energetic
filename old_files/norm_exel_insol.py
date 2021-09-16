import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

path = 'NY.xlsx'
df = pd.DataFrame()
data = pd.read_excel(path)
df = df.append(data)

print(df)

# for f in ['ww', 'N', 'vv', 'U', 'PPP', 'hhh', 'Число месяца', 'UTC']:
# 	del df[f]
df.drop(df.columns[[0]], axis='columns', inplace=True)
df.drop(df.columns[[0]], axis='columns', inplace=True)
print(list(df))

def datetime_range(start, end, step):
	current = start
	while current < end:
		yield current
		current += step

x = list(datetime_range(
	datetime.datetime.strptime('2012.01.01 00:00', '%Y.%m.%d %H:%M'),
	datetime.datetime.strptime('2013.01.01 00:00', '%Y.%m.%d %H:%M'),
	datetime.timedelta(hours=1)))

df['date'] = x
print(list(df))
df.rename(columns={'ETRN (W/m^2)': 'ETRN'}, inplace=True)
df = df[['date', 'ETRN']]
print(df)


print(df.iloc[0][0])
print(type(df.iloc[0][0]))
df.to_excel("NY_.xlsx")