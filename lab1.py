import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time
import matplotlib.dates as mdates
from windrose import WindroseAxes
from datetime import date

# pathToFile = r'C:/lab1/2012-12.xlsx'
# workbook = pd.ExcelFile(pathToFile)
# dataframe = workbook.parse(workbook.sheet_names)
# sheet_names = str(workbook.sheet_names)
# sheet_names = sheet_names[2:9]

class getGraph:
	def __init__(self, name, fstart, fend):
		self.start_time = time.time()
		self.path  = 'database/' + name + '.xlsx'
		start = datetime.datetime.combine(fstart, datetime.time(0,0))
		end = datetime.datetime.combine(fend, datetime.time(23, 00))
		self.start_day = start
		self.end_day = end
		self.df = pd.DataFrame()
		data = pd.read_excel(self.path)
		self.df = self.df.append(data)
		self.df.drop(self.df.columns[[0]], axis='columns', inplace=True)
		self.df["date"] = pd.to_datetime(self.df["date"], errors="coerce")
		temp = self.df.query("date in [@start, @end]").index
		self.istart = temp[0]
		self.iend = temp[1]

		# start_insol = datetime.datetime.strptime('2013.01.01 00:00', '%Y.%m.%d %H:%M')
		# end_insol = datetime.datetime.strptime('2013.12.31 23:00', '%Y.%m.%d %H:%M') 
		path_insol = 'NY_.xlsx'
		self.df_insol = pd.DataFrame()
		data_insol = pd.read_excel(path_insol)
		self.df_insol = self.df_insol.append(data_insol)
		self.df_insol.drop(self.df_insol.columns[[0]], axis='columns', inplace=True)
		self.df_insol["date"] = pd.to_datetime(self.df_insol["date"], errors="coerce")
		temp_insol = self.df_insol.query("date in [@start, @end]").index
		self.istart_insol = temp_insol[0]
		self.iend_insol = temp_insol[1]
		self.y = []
		self.ws = self.df['FF'][self.istart:self.iend+1]
		self.all_time = 0
		self.temp_time = time.time() - self.start_time
		print("Init " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.y_insol = []
		self.dicTempRegim = {}
		self.start_time = time.time()

	def getDayPromizok(self):
		temp = ""
		for letter in str(self.end_day - self.start_day):
			if(letter != " "):
				temp += letter
			elif(letter == " "):
				break

		return int(temp)

	def getTempRegim(self):
		return self.dicTempRegim

	def getDataFrame(self):
		return self.df

	def getStart(self):
		return self.istart

	def getEnd(self):
		return self.iend

	def getDataFrameInsol(self):
		return self.df_insol

	def getStartInsol(self):
		return self.istart_insol

	def getEndInsol(self):
		return self.iend_insol


	def printGraphFirst(self):
		x = []

		for i in range(self.istart, self.iend):
			x.append(self.df.iloc[i][0])
			if np.isnan(self.df.iloc[i][1]):
				self.y.append(self.y[len(self.y)-1])
			else:
				self.y.append(int(self.df.iloc[i][1]))

		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		plt.title("Температурні умови") # заголовок
		plt.xlabel("Дата") # ось абсцисс
		plt.ylabel("Температура, ℃") # ось ординат
		plt.grid()      # включение отображение сетки
		plt.plot(x, self.y)
		# plt.gcf().autofmt_xdate(rotation = 90)
		# x.clear()
		# y.clear()
		# plt.show()
		
		self.temp_time = time.time() - self.start_time
		print("1 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()

		return fig
		

	def printGraphSecond(self):

		dic = {}

		unique = list(set(self.y))

		for i in range(len(unique)):
			dic[unique[i]] = 0


		for i in range(len(self.y)):
			dic[self.y[i]] += 0.5


		self.dicTempRegim = dic

		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		ax.bar(list(dic.keys()), list(dic.values()))
		ax.set_facecolor('seashell')
		fig.set_facecolor('floralwhite')
		plt.title("Тривалість температурних режимів") # заголовок
		plt.xlabel("Температура, ℃") # ось абсцисс
		plt.ylabel("Час, год") # ось ординат
		fig.set_figwidth(12)    #  ширина Figure
		fig.set_figheight(6)    #  высота Figure
		plt.grid(axis = 'y')
		# y.clear()
		# plt.show()

		self.temp_time = time.time() - self.start_time
		print("2 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()

		return fig
	

	def printGraphThird(self):
		dd = self.df['dd'][self.istart:self.iend+1]
		wd = []
		for i in dd:
			if(str(i) == 'Северный'):
				wd.append(360)
			elif(str(i) == 'С-В'):
				wd.append(45)
			elif(str(i) == 'Восточный'):
				wd.append(90)
			elif(str(i) == 'Ю-В'):
				wd.append(135)
			elif(str(i) == 'Южный'):
				wd.append(180)
			elif(str(i) == 'Ю-З'):
				wd.append(225)
			elif(str(i) == 'Западный'):
				wd.append(270)
			elif(str(i) == 'С-З'):
				wd.append(315)
			elif(str(i) == 'Переменный' or str(i) == 'nan'):
				wd.append(0)


		fig = plt.figure()
		plt.rcParams.update({'font.size': 12})
		rect=[0.1, 0.1, 0.8, 0.8] 
		ax=WindroseAxes(fig, rect)
		fig.add_axes(ax)
		ax.bar(wd, self.ws, normed=True, opening=1.5, edgecolor='white')
		ax.set_legend()
		plt.title("Троянда вітрів") # заголовок
		# plt.show()
		# ws.clear()
		# wd.clear()
		
		self.temp_time = time.time() - self.start_time
		print("3 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()
		
		return fig


	def printGraphFourth(self):

		y = []

		dic = {}

		y = [i for i in self.ws if (not np.isnan(i) and i >= 0)]

		# for i in range(self.istart, self.iend+1):
		# 	if np.isnan(self.df.iloc[i][3]):
		# 		y.append(y[len(y)-1][3])
		# 	else:
		# 		y.append(int(self.df.iloc[i][3]))

		unique = list(set(y))

		for i in range(len(unique)):
			dic[unique[i]] = 0


		for i in range(len(y)):
			dic[y[i]] += 0.5


		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		ax.bar(list(dic.keys()), list(dic.values()))
		ax.set_facecolor('seashell')
		fig.set_facecolor('floralwhite')
		plt.title("Тривалість вітрової активності") # заголовок
		plt.xlabel("Температура, ℃") # ось абсцисс
		plt.ylabel("Час, год") # ось ординат
		fig.set_figwidth(12)    #  ширина Figure
		fig.set_figheight(6)    #  высота Figure
		plt.grid(axis = 'y')
		# y.clear()
		# plt.show()
		
		self.temp_time = time.time() - self.start_time
		print("4 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()

		return fig


	def printInsolFirst(self):
		df = self.df_insol
		# x = []

		self.y_insol = [i for i in df["ETRN"][self.istart_insol:self.iend_insol+1] if not np.isnan(i)]
		x = [i for i in df["date"][self.istart_insol:self.iend_insol+1] if (j for j in df["ETRN"][self.istart_insol:self.iend_insol+1] if not np.isnan(j))]

		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		plt.title("Інтенсивність сонячної інсоляції") # заголовок
		plt.xlabel("Дата (характерний рік)") # ось абсцисс
		plt.ylabel("Вт/м^2") # ось ординат
		plt.grid()      # включение отображение сетки
		ax.bar(x, self.y_insol, width = 0.05)
		plt.gcf().autofmt_xdate(rotation = 90)
		# x.clear()
		# y.clear()
		# plt.show()

		self.temp_time = time.time() - self.start_time
		print("5 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()

		return fig


	def printInsolSecond(self):
		istart = getGraph.getStartInsol(self)
		iend = getGraph.getEndInsol(self)
		df = getGraph.getDataFrameInsol(self)
		dic = {}

		y = [i for i in self.y_insol if i != 0]

		# for i in range(istart, iend+1):
		# 	if(df.iloc[i][1] != 0):
		# 		y.append(df.iloc[i][1])

		unique = list(set(y))

		for i in range(len(unique)):
			dic[unique[i]] = 0


		for i in range(len(y)):
			dic[y[i]] += 1

		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		ax.bar(list(dic.keys()), list(dic.values()))
		ax.set_facecolor('seashell')
		fig.set_facecolor('floralwhite')
		plt.title("Тривалість режимів сонячної активності") # заголовок
		plt.xlabel("Вт/м^2") # ось абсцисс
		plt.ylabel("Час, год") # ось ординат
		fig.set_figwidth(12)    #  ширина Figure
		fig.set_figheight(6)    #  высота Figure
		plt.grid(axis = 'y')
		# plt.show()
		# y.clear()

		self.temp_time = time.time() - self.start_time
		print("6 " + str(self.temp_time) + " seconds")
		self.all_time += self.temp_time
		self.start_time = time.time()
		print("Full time " + str(self.all_time) + " seconds")

		return fig

def main():
	start = datetime.datetime.strptime('2012.01.01 00:00', '%Y.%m.%d %H:%M')
	end = datetime.datetime.strptime('2012.12.31 23:30', '%Y.%m.%d %H:%M') 
	name = 'Дніпро'
	Graph = getGraph(name, start, end)
	# Graph.printGraphFirst()
	# Graph.printGraphSecond()
	# Graph.printGraphThird()
	# Graph.printGraphFourth()
	# Graph.printInsolFirst()
	# Graph.printInsolSecond()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
