import datetime
import time
import pandas as pd
import random
import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
import mplcursors

def randrange_float(start, stop, step):
	return random.randint(0, int((stop - start) / step)) * step + start


class Device:
	def __init__(self, name, force):
		self.name = name
		self.force = force

	def printInfo(self):
		text = "\nName: " + self.name + "\nForce: " + str(self.force)
		print(text)

	def getForce(self):
		return self.force

	def getForceMin(self):
		return (self.force/60)

	def getName(self):
		return self.name

	def getConsume(self, time):
		return self.force*time


class People:
	def __init__(self, name, start_date, end_date, type):
		self.type_people = type
		self.name = name
		self.times = {}
		self.df = pd.DataFrame({"time":pd.date_range(start_date, end_date, freq="T")})

	def getType(self):
		return self.type_people

	def getDf(self):
		return self.df

	def getDays(self):
		return int(self.df.size/1440)

	def randomTime(self, df_copy, time):
		res = []
		ans = []
		t = 30 # количество минут в каждой нарезке
		num = time * 2 # количество нарезок датафрейма
		num = int(num)
		intervals = [[0] * (t+1) for i in range(num)]

		for i in range(num):
			if(time == 24):
				inter = [[0] * 1440]
				smpl = df_copy.iloc[:df_copy.size]
				res.append(smpl['time'].to_list())
				# print(res)
				# print("stop")
				break
			# elif(time == 12):
			# 	temp = random.randint(0,1000)
			# 	smpl = df_copy.iloc[temp:temp+1440]
			# 	res.append(smpl['time'].to_list())
			# 	break
			rnd = df_copy.sample(n=1, random_state=random.randint(2, 2)).index.values[0]
			smpl = df_copy.iloc[rnd-int(t/2):rnd+int(t/2)+1]
			df_copy=pd.concat([df_copy, smpl]).drop_duplicates(keep=False)
			res.append(smpl['time'].to_list())

		if(time == 24):
			for i in range(len(res)):
				for j in range(len(res[i])):
					inter[i][j] = res[i][j].to_pydatetime()
			return inter

		for i in range(len(res)):
			for j in range(len(res[i])):
				intervals[i][j] = res[i][j].to_pydatetime()

		# print(intervals)
		return(intervals)

	def addScedule(self, obj, min_time, max_time):
		s = 0
		e = 1440
		days = int(self.df.size/1440)
		ans = []
		a = []
		for i in range(days):
			df_day = self.df[s:e].reset_index()
			time = randrange_float(min_time, max_time, 0.5)
			# print(time)
			# print("iter = " + str(i) + "   time = " + str(time))
			ans.append(self.randomTime(df_day, time))
			s = e
			e += 1440
			key = obj.getName() + str(df_day.iloc[5][1].strftime('%Y.%m.%d'))
			self.times[key] = ans[0]
			ans.clear()

	def getTimes(self):
		return self.times

	def getIntervals(self, obj):
		text = ""
		for i in range(int(self.df.size/1440)):
			key = obj.getName() + str(self.df.iloc[(1440*(i+1))-100][0].strftime('%Y.%m.%d'))
			lst = self.times[key]
			text += "\nDay# " + str(i+1) + "(" + str(self.df.iloc[(1440*(i+1))-100][0].strftime('%Y.%m.%d')) + ")"
			for i in range(len(lst)):
				start = lst[i][0]
				end = lst[i][len(lst[i])-1]
				if(isinstance(end, int)):
					print(end)
					print(i)
					print(start)
				text += "\nInterval #" + str(i+1) + "\nStart time: " + start.strftime('%Y.%m.%d %H:%M') + "\nEnd time: " + end.strftime('%Y.%m.%d %H:%M') 
		return text

	# def printInfo(self):
	# 	text = "\nName: " + self.name + "\nRaspisanie: "
	# 	for i in 
	# 	print(text)
		

class GraphLab3:
	def __init__(self):
		self.spasi_i_sohrahi = []
		self.days = []
		self.x_amin = []
		self.y_amin = []
		self.pik_dob = 0
		self.pik_week = 0
		self.best = 0
		self.check = 0

	def getPikDob(self):
		t = str(float(f"{self.pik_dob/1000:.{2}f}")) + "кВт"
		return t

	def getPikWeek(self):
		t = str(float(f"{self.pik_week:.{2}f}")) + "кВт"
		return t

	def getBest(self):
		if self.best == 1:
			return "однозонним лічильником"
		elif self.best == 2:
			return "двозонним лічильником"
		elif self.best == 3:
			return "тризонним лічильником"
	

	def oneDevice_oneDay(self, interval, df, device):
		y = []
		x = []
		temp_list = []
		for i in interval:
			for j in i:
				temp_list.append(j)

		for date in df['time']:
			if(device.getName() == "Холодильник" and date == df['time'].iloc[0]):
				y.append(0)
				x.append(date.to_pydatetime())
			elif(device.getName() == "Холодильник" and date == df['time'].iloc[df['time'].size-1]):
				y.append(0)
				x.append(date.to_pydatetime())
			elif(date in temp_list):
				y.append(device.getForce())
				x.append(date.to_pydatetime())
			elif(date not in temp_list):
				y.append(0)
				x.append(date.to_pydatetime())
		return [x, y]


	def allDevice_oneGraph(self, devices, week_day, people):
		wday = week_day
		df = people.getDf()
		inter = []
		s = 0
		for i in range(people.getDays()):
			temp = i * 1440
			if(df.iloc[temp+100][0].weekday() == wday):
				s = temp
				break
			else:
				continue

		df_copy = df[s:s+1440].reset_index()
		# fig, axes = plt.subplots(figsize=(20,10), dpi = 100)
		# plt.figure(figsize=(20,10), dpi = 100)
		fig, axes = plt.subplots(figsize=(20,60), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		for i in range(len(devices)):
			plt.subplot(3, 3, i+1)
			# plt.xlim([datetime.time(0,0), datetime.time(23,59)]) 
			plt.ylim([-100,3000]) 
			inter = people.getTimes()[devices[i].getName() + str(df_copy.iloc[1][1].strftime('%Y.%m.%d'))]
			lst = self.oneDevice_oneDay(inter, df_copy, devices[i])
			x = lst[0]
			y = lst[1]

			for x_i in range(len(x)):
				x[x_i] = x[x_i].time()

			plt.title(devices[i].getName()) # заголовок
			plt.xlabel("Час") # ось абсцисс
			if i % 3 == 0:            
				plt.ylabel("Потужність, Вт/год") # ось ординат
			plt.xticks([datetime.time(0,0), datetime.time(6,0), datetime.time(12,0), datetime.time(18,0), datetime.time(23,59)])
			# plt.title(devices[i].getName()) # заголовок
			# plt.xlabel("Час") # ось абсцисс
			# plt.ylabel("Потужність, Вт/год") # ось ординат
			plt.subplots_adjust(hspace = 0.5)
			# plt.xticks(rotation=90)
			# fig.tight_layout()
			plt.plot(x, y)

		# plt.grid()      # включение отображение сетки
		# plt.show()
		return fig


	def allDevice_allWeek(self, devices, people):
		wday = 0
		df = people.getDf()
		s = 0
		for i in range(people.getDays()):
			temp = i * 1440
			if(df.iloc[temp+100][0].weekday() == wday):
				s = temp
				break
			else:
				continue

		df_copy = df[s:s+(1440*7)].reset_index()

		x = [] 
		y = []

		y_sum = 0
		flag = 0
		for device in devices:
			count = 0
			for day in range(7):
				i = day*1440
				df_copy2 = df_copy[i:i+1440]
				inter = people.getTimes()[device.getName() + str(df_copy2.iloc[1][1].strftime('%Y.%m.%d'))]
				lst = self.oneDevice_oneDay(inter, df_copy2, device)
				x_d = lst[0]
				y_d = lst[1]
				y_sum = sum(y_d)
				if flag == 0:
					x += x_d
					y += y_d
					self.spasi_i_sohrahi.append(sum(y_d)/60)
					self.days.append(df_copy2['time'].iloc[1].to_pydatetime().date())
				else:
					for i in range(len(y_d)):
						# print(y[count], y_d[count])
						if(i < 1):
							self.spasi_i_sohrahi[day] += sum(y_d)/60
						y[count] += y_d[i]
						count += 1
			flag = 1
			
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		y_max = max(y)
		self.x_amin = x
		self.y_amin = y
		bars = ax.bar(x, y, width=0.01)
		sk = 0
		self.pik_dob = y_max
		for i in range(len(y)):
			if y[i] == y_max:
				bars[i].set_color('r')
				if(sk == 0):
					bars[i].set_label('Пікове навантаження за добу')
					sk = 1
				bars[i].set_linewidth(0.01)
		ax.legend()
		plt.title("Гістограма електричного навантаження") # заголовок
		plt.xlabel("Дата") # ось абсцисс
		plt.ylabel("Потужність, Вт/год") # ось ординат
		fig.set_figwidth(12)    #  ширина Figure
		fig.set_figheight(6)
		# cursor1 = mplcursors.cursor(bars, hover=True)
		# @cursor1.connect("add")
		# def on_add(sel):
		# 	x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
		# 	sel.annotation.set(text=f"Потужність: {height:.{2}f} кВт/год")
		# 	sel.annotation.xy = (x + width / 2, y + height)

		# print(dev_days)
		# plt.show()
		return fig


	def forceWeek(self):
		x = self.days
		y = []
		for i in self.spasi_i_sohrahi:
			y.append(i/1000)
		# print(x, y)
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()

		y_max = max(y)
		self.pik_week = y_max
		bars = ax.bar(x, y)
		sk = 0
		for i in range(len(y)):
			if y[i] == y_max:
				bars[i].set_color('r')
				if sk == 0:
					bars[i].set_label('Пікове навантаження за тиждень')
					sk = 1
		ax.legend()
		plt.title("Обсяги споживання електричної енергії для кожної доби тижня") # заголовок
		plt.xlabel("Дата") # ось абсцисс
		plt.ylabel("Потужність, кВт/год") # ось ординат
		fig.set_figwidth(12)    #  ширина Figure
		fig.set_figheight(6)
		# cursor2 = mplcursors.cursor(hover=True)
		# @cursor2.connect("add")
		# def on_add(sel):
		# 	x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
		# 	sel.annotation.set(text=f"Потужність: {height:.{2}f} кВт/год")
		# 	sel.annotation.xy = (x + width / 2, y + height)
		# plt.show()
		return fig


	def tarifGistoXY(self, lichilnik, people):
		x = []
		y = []
		suma = (sum(self.spasi_i_sohrahi)/1000)*4
		night = []
		day = []
		pik = []
		pivpik = []
		tarif = {"Для багатодітної сім'ї": 0.9, "Для звичайного населення":1, "Для ЖЕО":1.68, "Для гуртожитків":0.9}
		price = tarif[people.getType()]
		if price == 1:
			if suma > 100:
				price=1.68
			else:
				price=0.9

		if lichilnik == "Однозонний":
			suma*=price
			self.check = suma
			self.best = 1

		elif lichilnik == "Двозонний":
			# x_amin - список с датами за неделю
			# y_amin - список с напряженем в Вт всех приборов за неделю (соответствует x_amin)
			for i in range(len(self.x_amin)):
				if self.x_amin[i].time() >= datetime.time(23,0) or self.x_amin[i].time() < datetime.time(7,0):
					night.append(self.y_amin[i])
				else:
					day.append(self.y_amin[i])
			suma = (((sum(night)/1000/60) *4 * price * 0.5) + ((sum(day)/1000/60) *4 * price * 1))
			if(self.check > suma):
				self.best = 2
		
		else: # Тризонний
			# x_amin - список с датами за неделю
			# y_amin - список с напряженем в Вт всех приборов за неделю (соответствует x_amin)
			for i in range(len(self.x_amin)):
				if self.x_amin[i].time() >= datetime.time(23,0) or self.x_amin[i].time() < datetime.time(7,0):
					night.append(self.y_amin[i])
				elif self.x_amin[i].time() >= datetime.time(7,0) or self.x_amin[i].time() < datetime.time(8,0):
					pivpik.append(self.y_amin[i])
				elif self.x_amin[i].time() >= datetime.time(8,0) or self.x_amin[i].time() < datetime.time(11,0):
					pik.append(self.y_amin[i])
				elif self.x_amin[i].time() >= datetime.time(11,0) or self.x_amin[i].time() < datetime.time(20,0):
					pivpik.append(self.y_amin[i])
				elif self.x_amin[i].time() >= datetime.time(20,0) or self.x_amin[i].time() < datetime.time(22,0):
					pik.append(self.y_amin[i])
				elif self.x_amin[i].time() >= datetime.time(22,0) or self.x_amin[i].time() < datetime.time(23,0):
					pivpik.append(self.y_amin[i])

			suma = ((sum(night)/1000/60) *4 * price * 0.4) + ((sum(pivpik)/1000/60) *4 * price * 1) + ((sum(pik)/1000/60) *4 * price * 1.5)
			if(self.check > suma):
				self.best = 3
		
		return suma


	def tarifHist(self, people):
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		bars = ax.bar(['Однозонний', 'Двозонний', 'Тризонний'], [self.tarifGistoXY("Однозонний", people), self.tarifGistoXY("Двозонний", people),self.tarifGistoXY("Тризонний", people)])
		plt.title("Ціна за електроенергію за різними тарифами") # заголовок
		plt.xlabel("Типи лічильників") # ось абсцисс
		plt.ylabel("Вартість, грн") # ось ординат
		# cursor3 = mplcursors.cursor(hover=True)
		# @cursor3.connect("add")
		# def on_add(sel):
		# 	x, y, width, height = sel.artist[sel.target.index].get_bbox().bounds
		# 	sel.annotation.set(text=f"Вартість: {height:.{2}f} грн")
		# 	sel.annotation.xy = (x + width / 2, y + height)
		# plt.grid()
		# plt.show()
		return fig


def main():
	devices = []
	peoples = []

	fstart = datetime.datetime.strptime('2012.01.01 00:00', '%Y.%m.%d %H:%M')
	fend = datetime.datetime.strptime('2012.01.14 21:30', '%Y.%m.%d %H:%M')
	start = datetime.datetime.combine(fstart, datetime.time(0,0))
	end = datetime.datetime.combine(fend, datetime.time(23, 59))

	Vova = People("Вова", start, end, "Для багатодітної сім'ї")
	Inna = People("Інна", start, end, "Для гуртожитків")
	peoples.append(Vova)
	# peoples.append(Inna)

	device1 = Device("Пилосос", 300)
	device2 = Device("Праска", 500)
	device3 = Device("Мікрохвильова піч", 1200)
	device4 = Device("Холодильник", 450)
	devices.append(device1)
	devices.append(device2)
	devices.append(device3)
	devices.append(device4)

	graph = GraphLab3()
	# devices.printDevices()
	# print(len(devices))
	# print("\n")
	for p in peoples:
		min_time = 0.5
		max_time = 5
		for d in devices:
			if(d.getName() == "Холодильник"):
				min_time = 24
				max_time = 24
			# print("\n")
			# print(d.getName())
			p.addScedule(d, min_time, max_time)
			# print("\n")
			# print(p.getIntervals(d))
		# graph.allDevice_oneGraph(devices, 2, p)
		#ПРАВКИ


	f = graph.allDevice_allWeek(devices, Vova)
	f2 = graph.forceWeek()
	graph.tarifHist(Vova)
	print(graph.getPikWeek(), "   ", graph.getPikDob())
	



if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
	main()  # то запускаем функцию main()
		