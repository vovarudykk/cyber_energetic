import datetime
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline, BSpline
import numpy as np
import mplcursors
import random
import copy

from io import BytesIO
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

class BD:
	def __init__(self):
		self.veus = []
		self.bashtas = []
		self.veus.append(Veu("Вітрогенератор 2000", "Вертикальна", 2880000))
		self.veus.append(Veu("Вітер Х", "Горизонтальна", 3000000))
		self.bashtas.append(Bashta("Дон Кіхот", 15, 2500000))
		self.bashtas.append(Bashta("Млин", 20, 2750000))

	def addBashta(self, b):
		self.bashtas.append(b)

	def addVeu(self, v):
		self.veus.append(v)

	def getVeu(self, id):
		return self.veus[id]

	def getBashta(self, id):
		return self.bashtas[id]

	def getveus(self):
		return self.veus

	def getbashtas(self):
		return self.bashtas


class Veu:
	def __init__(self, name, type_veu, cost):
		self.name = name
		self.type_veu = type_veu
		self.cost = cost

	def getName(self):
		return self.name

	def getType(self):
		return self.type_veu

	def getCost(self):
		return self.cost


class Bashta:
	def __init__(self, name, hight, cost):
		self.name = name
		self.hight = hight
		self.cost = cost

	def getName(self):
		return self.name

	def getHight(self):
		return self.hight

	def getCost(self):
		return self.cost


class Lab4:
	def __init__(self, start, end, city, speed, force, veu, bashta):
		self.veu = veu
		self.bashta = bashta
		self.path  = 'database/' + city + '.xlsx'
		start_ = datetime.datetime.combine(start, datetime.time(0,0))
		end_ = datetime.datetime.combine(end, datetime.time(23, 00))

		df = pd.DataFrame()
		df = df.append(pd.read_excel(self.path))
		df.drop(df.columns[[0]], axis='columns', inplace=True)
		df.drop(['T', 'dd'], axis='columns', inplace=True)
		df["date"] = pd.to_datetime(df["date"], errors="coerce")
		temp = df.query("date in [@start_, @end_]").index
		self.df = df.iloc[temp[0]:temp[1]]

		self.count_energy = 0
		self.co2 = 0
		self.dohod = 0
		self.dohod_co2 = 0
		self.dohod_full = 0

		self.speed = copy.copy(speed)
		self.force = copy.copy(force)

		self.calculate()
		self.fig = None

	
	def getReport(self):
		time = datetime.datetime.now().strftime("%d.%m.%Y_%H%M%S")
		filename = "reports/lab4_report_" + time + ".pdf"
		pdf = Canvas(filename, pagesize=A4)
		pdfmetrics.registerFont(TTFont('Oswald', 'Oswald-Regular.ttf'))
		pdf.setFont('Oswald', 16)
		pdf.setTitle("Звіт до виконання ЛР4")
		pdf.drawCentredString(300, 790, "Звіт для змодельованої ситуації")
		pdf.line(10, 785, 585, 785)

		pdf.drawString(40, 760, "Вітроенергетична установка: " + self.veu.getName())
		pdf.setFont('Oswald', 14)
		pdf.drawString(70, 745, "Тип: " + str(self.veu.getType()).lower())
		pdf.drawString(70, 730, "Вартість: " + str(self.veu.getCost()) + "грн")

		pdf.setFont('Oswald', 16)
		pdf.drawString(40, 700, "Башта: " + self.bashta.getName())
		pdf.setFont('Oswald', 14)
		pdf.drawString(70, 685, "Висота: " + str(self.bashta.getHight()) + "м")
		pdf.drawString(70, 670, "Вартість: " + str(self.bashta.getCost()) + "грн") 

		pdf.setFont('Oswald', 16)
		pdf.drawCentredString(300, 645, "Таблиця енергетичної залежності ")
		pdf.line(10, 642, 585, 642)
		pdf.setFont('Oswald', 12)
		pdf.drawString(170, 630, "Швидкість, м/с")
		pdf.drawString(370, 630, "Потужність, кВт")
		pdf.line(10, 627, 585, 627)
		x1 = 200
		x2 = 400
		y = 615
		for i in range(10):
			pdf.drawString(x1, y, str(self.speed[i]))
			pdf.drawString(x2, y, str(self.force[i]))
			y -= 15
		pdf.line(10, 475, 585, 475)

		self.fig.set_size_inches(6, 3)
		imgdata = BytesIO()
		self.fig.savefig(imgdata, format='svg')
		imgdata.seek(0)  # rewind the data

		drawing=svg2rlg(imgdata)
		renderPDF.draw(drawing, pdf, 40, 200)

		pdf.setFont('Oswald', 14)
		pdf.drawString(40, 170, "Загальна вартість установки та башти: " + str(f"{self.bashta.getCost() + self.veu.getCost():.{2}f}") + "грн")
		pdf.drawString(40, 150, "Обрана установка за визначений період згенерує в середньому: " + str(f"{self.getCountEnergy():.{2}f}") + "кВт")
		pdf.drawString(40, 130, "Викиди CO2 скоротяться на: " + str(f"{self.getCO2():.{2}f}") + "т")
		pdf.drawString(40, 110, "Дохід від продажу енергії за зеленим тарифом: " + str(f"{self.getDohod():.{2}f}") + "грн")
		pdf.drawString(40, 90, "Дохід від продажу одиниць скорочення викидів СО2: " + str(f"{self.getDohodCO2():.{2}f}")+ "грн")
		pdf.drawString(40, 70, "Загальний дохід становить: " + str(f"{self.getFullDohod():.{2}f}")+ "грн")

		pdf.showPage()
		pdf.save()


	def getCountEnergy(self):
		return self.count_energy

	def getCO2(self):
		return self.co2

	def getDohod(self):
		return self.dohod

	def getDohodCO2(self):
		return self.dohod_co2

	def getFullDohod(self):
		return self.dohod_full

	def calculate(self):
		dic = {}

		y = self.df["FF"].values.tolist()
		unique = list(set(y))
		for i in range(len(unique)):
			dic[unique[i]] = 0
		for i in range(len(y)):
			dic[y[i]] += 0.5
		
		speed = self.findV(self.bashta.getHight(), copy.copy(self.speed))

		force = [random.randint(0, 50) for i in range(len(dic.keys()))]

		keys = list(dic.keys())
		values = list(dic.values())
		for i in range(len(force)):
			self.count_energy += force[i]*keys[i]*values[i]

		self.count_energy /= 20
		self.co2 = self.count_energy*0.943/1000
		self.dohod = self.count_energy*5.5
		self.dohod_co2 = 340*self.co2
		self.dohod_full = self.dohod_co2+self.dohod


	def findV(self, hight, speed):
		for i in range(len(speed)):
			speed[i] = speed[i]*pow(hight/10, 0.14)
		return speed

	def Graph(self):
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		pd.plotting.register_matplotlib_converters()
		plt.title("Енергетична характеристика")
		plt.xlabel("Швидкість вітру, м/с")
		plt.ylabel("Потужність, кВт")
		plt.grid() 

		x = np.linspace(self.speed.min(), self.speed.max(), 300)
		spl = make_interp_spline(self.speed, self.force, k=3)
		y = spl(x)

		plt.plot(x, y)

		scat = plt.scatter(self.speed, self.force, marker = 'o', c = 'red', edgecolors = 'black', alpha = 0.6)

		cursor = mplcursors.cursor(scat, hover=True)

		cursor.connect("add", lambda sel: sel.annotation.set_text('Швидкість: {}м/с\n Потужність: {}кВт'
			.format(f"{sel.target[0]:.{2}f}", round(sel.target[1]))))

		# for i in range(0, int(np.amax(self.speed))):
		# 	plt.axvline(x=i, color='grey', linewidth=0.1)
		# 	if(i < len(self.force)):
		# 		plt.axhline(y=self.force[i], color='grey', linewidth=0.2)

		# plt.show()

		self.fig = copy.copy(fig)
		return fig


if __name__ == '__main__':
	start = datetime.datetime.strptime('2012.01.01 00:00', '%Y.%m.%d %H:%M')
	end = datetime.datetime.strptime('2012.01.14 23:30', '%Y.%m.%d %H:%M') 
	city = 'Дніпро'

	veu1 = Veu("Veu1", "Горизонтальна", 3000001)
	bashta1 = Bashta("Bashta1'", 23, 2500001)

	datbas = BD()

	force = np.array([0, 3, 20, 70, 96, 110, 65, 30, 5, 0])
	speed = np.array([0, 1, 3.5, 8, 12, 15, 16, 25, 30, 35])

	vid = 1
	bid = 0

	test = Lab4(start, end, city, speed, force, datbas.getVeu(vid), datbas.getBashta(bid))
	test.Graph()
	test.getReport()
	# attrs = vars(test)
	# print(', '.join("%s: %s" % item for item in attrs.items()))


	# test2 = Lab4(start, end, city, speed, force, datbas.getVeu(vid), datbas.getBashta(bid))
	# test2.Graph()
	# datbas.addVeu(veu1)
	# datbas.addBashta(bashta1)
	# attrs = vars(test2)
	# print(', '.join("%s: %s" % item for item in attrs.items()))