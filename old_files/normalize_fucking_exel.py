import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

path = 'database/Dnipro/'
files_xlsx = [path + f for f in os.listdir(path) if f[-4:] == 'xlsx']
# s = files_xlsx[0]
# print(s[-11:-5])
df = pd.DataFrame()
for f in files_xlsx:
	if(len(f) == 27):
		data = pd.read_excel(f, f[-11:-5])
		df = df.append(data)

for f in files_xlsx:
	if(len(f) == 28):
		data = pd.read_excel(f, f[-12:-5])
		df = df.append(data)

for f in ['ww', 'N', 'vv', 'U', 'PPP', 'hhh', 'Число месяца', 'UTC']:
	del df[f]

def datetime_range(start, end, step):
	current = start
	while current < end:
		yield current
		current += step

x = list(datetime_range(
	datetime.datetime.strptime('2012.01.01 00:00', '%Y.%m.%d %H:%M'),
	datetime.datetime.strptime('2013.01.01 00:00', '%Y.%m.%d %H:%M'),
	datetime.timedelta(hours=0.5)))

df['date'] = x

df = df[['date', 'T', 'dd', 'FF']]
df.to_excel("Dnipro.xlsx")