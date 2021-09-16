import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, QtCore, QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import design4_1  # Это наш конвертированный файл дизайна
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QMessageBox, QWidget, QDesktopWidget
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from lab1 import getGraph
from lab2 import getLab2
from PyQt5.QtGui import QIcon
from lab3 import Device
from lab3 import People
from lab3 import GraphLab3
from lab4 import BD
from lab4 import Lab4
from lab4 import Veu
from lab4 import Bashta
import datetime
import numpy as np


class MyMplCanvas(FigureCanvas):
	def __init__(self, fig, parent=None):
		self.fig = fig
		FigureCanvas.__init__(self, self.fig)
		FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
		FigureCanvas.updateGeometry(self)


class Window(QtWidgets.QMainWindow, design4_1.Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setGeometry(300, 300, 300, 600)
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('logo.png'))
		self.setupUi(self)  # Это нужно для инициализации нашего дизайна
		self.pushButtonConfirm.clicked.connect(self.doLab1)
		self.pushButtonConfirm_2.clicked.connect(self.doLab2)
		self.pushButtonConfirm_3.clicked.connect(self.doLab3)
		self.pushButtonAddDevice.clicked.connect(self.inputAddDevice)
		self.pushButtonConfirm_4.clicked.connect(self.doLab4)
		self.pushButtonAddVeu.clicked.connect(self.lab4AddVeu)
		self.pushButtonAddBasht.clicked.connect(self.lab4AddBashta)
		self.lab4_download_zvit.clicked.connect(self.getReportLab4)
		self.city = self.getCity()
		self.istart = self.calendarWidget_1.selectedDate()
		self.iend = self.calendarWidget_2.selectedDate()
		self.devices = []
		self.cash = []
		self.WindowDownloadEnd = QMessageBox()
		self.db = BD()
		self.veu_id = 0
		self.basht_id = 0
		self.lab4ShowBD(self.db)
		self.laba4 = None


	def onClicked(self):
		radioButton = self.sender()
		if radioButton.isChecked():
			self.veu_id = radioButton.id
			print(self.veu_id)

	def onClicked2(self):
		radioButton = self.sender()
		if radioButton.isChecked():
			self.basht_id = radioButton.id
			print(self.basht_id)
			
	def getReportLab4(self):
		self.laba4.getReport()


	def lab4ShowBD(self, db):
		for veu in db.getveus():
			temp = veu.getName() + " (" + "тип: "+ veu.getType().lower() + "; ціна: " + str(veu.getCost()) + ")"
			self.radioButton1_ = QtWidgets.QRadioButton(temp)
			self.radioButton1_.id = self.veu_id
			self.veu_id += 1
			self.radioButton1_.toggled.connect(self.onClicked)
			self.verticalLayout.addWidget(self.radioButton1_)
			self.setLayout(self.verticalLayout)
			

		for bashta in db.getbashtas():
			temp = bashta.getName() + " (" + "висота: "+ str(bashta.getHight()) + "; ціна: " + str(bashta.getCost()) + ")"
			self.radioButton2_ = QtWidgets.QRadioButton(temp)
			self.radioButton2_.id = self.basht_id
			self.basht_id += 1
			self.radioButton2_.toggled.connect(self.onClicked2)
			self.verticalLayout_2.addWidget(self.radioButton2_)
			self.setLayout(self.verticalLayout_2)
			


	def lab4AddVeu(self):
		name = self.lab4_veu_name.text()
		type_veu = self.lab4_veu_type.currentText()
		cost = float(self.lab4_veu_cost.text())
		lst = []
		lst.append(name)
		lst.append(type_veu)
		lst.append(cost)

		self.db.addVeu(Veu(lst[0], lst[1], lst[2]))

		temp = lst[0] + " (" + "тип: "+ lst[1].lower() + "; ціна: " + str(lst[2]) + ")"
		self.radioButton1_ = QtWidgets.QRadioButton(temp)
		self.radioButton1_.id = self.veu_id
		self.veu_id += 1
		self.radioButton1_.toggled.connect(self.onClicked)
		self.verticalLayout.addWidget(self.radioButton1_)
		self.setLayout(self.verticalLayout)
		

	def lab4AddBashta(self):
		name = self.lab4_bashta_name.text()
		hight = float(self.lab4_bashta_hight.text())
		cost = float(self.lab4_bashta_cost.text())
		lst = []
		lst.append(name)
		lst.append(hight)
		lst.append(cost)

		self.db.addBashta(Bashta(lst[0], lst[1], lst[2]))

		temp = lst[0] + " (" + "висота: "+ str(lst[1]) + "; ціна: " + str(lst[2]) + ")"
		self.radioButton2_ = QtWidgets.QRadioButton(temp)
		self.radioButton2_.id = self.basht_id
		self.basht_id += 1
		self.radioButton2_.toggled.connect(self.onClicked2)
		self.verticalLayout_2.addWidget(self.radioButton2_)
		self.setLayout(self.verticalLayout_2)
		

	def doLab4(self):
		self.istart = (self.calendarWidget_1.selectedDate()).toPyDate()
		self.iend = (self.calendarWidget_2.selectedDate()).toPyDate()
		laba4 = self.inputLab4()
		self.laba4 = laba4
		self.getGraphLab4(laba4.Graph())
		self.lab4_count.setText(str(f"{laba4.getCountEnergy():.{2}f}") + "кВт")
		self.lab4_co2.setText(str(f"{laba4.getCO2():.{2}f}") + "т")
		self.lab4_dohid_zelen.setText(str(f"{laba4.getDohod():.{2}f}") + "грн")
		self.lab4_dohid_co2.setText(str(f"{laba4.getDohodCO2():.{2}f}") + "грн")
		self.lab4_dohid_all.setText(str(f"{laba4.getFullDohod():.{2}f}") + "грн")
		self.showMesaggeD()


	def inputLab4(self):
		speed = np.array([float(self.lab4_speed1.text()),
			float(self.lab4_speed2.text()),
			float(self.lab4_speed3.text()),
			float(self.lab4_speed4.text()),
			float(self.lab4_speed5.text()),
			float(self.lab4_speed6.text()),
			float(self.lab4_speed7.text()),
			float(self.lab4_speed8.text()),
			float(self.lab4_speed9.text()),
			float(self.lab4_speed10.text())])

		force = np.array([float(self.lab4_force1.text()),
			float(self.lab4_force2.text()),
			float(self.lab4_force3.text()),
			float(self.lab4_force4.text()),
			float(self.lab4_force5.text()),
			float(self.lab4_force6.text()),
			float(self.lab4_force7.text()),
			float(self.lab4_force8.text()),
			float(self.lab4_force9.text()),
			float(self.lab4_force10.text())])

		v_id = 1
		b_id = 1
		laba4 = Lab4(self.istart, self.iend, self.getCity(), 
			speed, force, self.db.getVeu(self.veu_id), self.db.getBashta(self.basht_id))
		return laba4


	def getGraphLab4(self, fig):
		self.fig = fig
		self.lab4_energ_harac_graph = QtWidgets.QVBoxLayout(self.lab4_energ_harac_graph)
		self.canavas4 = MyMplCanvas(self.fig)
		self.lab4_energ_harac_graph.addWidget(self.canavas4)
		self.toolbar = NavigationToolbar(self.canavas4, self)
		self.lab4_energ_harac_graph.addWidget(self.toolbar)


	def doLab3(self):
		User = self.inputLab3()
		graph = GraphLab3()
		
		self.get3First_1(graph.allDevice_oneGraph(self.devices, 0, User))
		self.get3First_2(graph.allDevice_oneGraph(self.devices, 1, User))
		self.get3First_3(graph.allDevice_oneGraph(self.devices, 2, User))
		self.get3First_4(graph.allDevice_oneGraph(self.devices, 3, User))
		self.get3First_5(graph.allDevice_oneGraph(self.devices, 4, User))
		self.get3First_6(graph.allDevice_oneGraph(self.devices, 5, User))
		self.get3First_7(graph.allDevice_oneGraph(self.devices, 6, User))
		self.get3Second(graph.allDevice_allWeek(self.devices, User))
		self.get3Third(graph.forceWeek())
		self.get3Fourth(graph.tarifHist(User))

		self.Input_pik_day.setText(graph.getPikDob())
		self.Input_pik_week.setText(graph.getPikWeek())
		self.Input_recomend_tarif.setText(graph.getBest())
		self.showMesaggeD()


	def get3First_1(self, fig):
		self.fig = fig
		self.widget_ener1_1 = QtWidgets.QVBoxLayout(self.widget_ener1_1)
		self.canavas3_1_1 = MyMplCanvas(self.fig)
		self.widget_ener1_1.addWidget(self.canavas3_1_1)
		self.toolbar = NavigationToolbar(self.canavas3_1_1, self)
		self.widget_ener1_1.addWidget(self.toolbar)
	

	def get3First_2(self, fig):
		self.fig = fig
		self.widget_ener1_2 = QtWidgets.QVBoxLayout(self.widget_ener1_2)
		self.canavas3_1_2 = MyMplCanvas(self.fig)
		self.widget_ener1_2.addWidget(self.canavas3_1_2)
		self.toolbar = NavigationToolbar(self.canavas3_1_2, self)
		self.widget_ener1_2.addWidget(self.toolbar)
	

	def get3First_3(self, fig):
		self.fig = fig
		self.widget_ener1_3 = QtWidgets.QVBoxLayout(self.widget_ener1_3)
		self.canavas3_1_3 = MyMplCanvas(self.fig)
		self.widget_ener1_3.addWidget(self.canavas3_1_3)
		self.toolbar = NavigationToolbar(self.canavas3_1_3, self)
		self.widget_ener1_3.addWidget(self.toolbar)
	

	def get3First_4(self, fig):
		self.fig = fig
		self.widget_ener1_4 = QtWidgets.QVBoxLayout(self.widget_ener1_4)
		self.canavas3_1_4 = MyMplCanvas(self.fig)
		self.widget_ener1_4.addWidget(self.canavas3_1_4)
		self.toolbar = NavigationToolbar(self.canavas3_1_4, self)
		self.widget_ener1_4.addWidget(self.toolbar)


	def get3First_5(self, fig):
		self.fig = fig
		self.widget_ener1_5 = QtWidgets.QVBoxLayout(self.widget_ener1_5)
		self.canavas3_1_5 = MyMplCanvas(self.fig)
		self.widget_ener1_5.addWidget(self.canavas3_1_5)
		self.toolbar = NavigationToolbar(self.canavas3_1_5, self)
		self.widget_ener1_5.addWidget(self.toolbar)
	

	def get3First_6(self, fig):
		self.fig = fig
		self.widget_ener1_6 = QtWidgets.QVBoxLayout(self.widget_ener1_6)
		self.canavas3_1_6 = MyMplCanvas(self.fig)
		self.widget_ener1_6.addWidget(self.canavas3_1_6)
		self.toolbar = NavigationToolbar(self.canavas3_1_6, self)
		self.widget_ener1_6.addWidget(self.toolbar)
	

	def get3First_7(self, fig):
		self.fig = fig
		self.widget_ener1_7 = QtWidgets.QVBoxLayout(self.widget_ener1_7)
		self.canavas3_1_7 = MyMplCanvas(self.fig)
		self.widget_ener1_7.addWidget(self.canavas3_1_7)
		self.toolbar = NavigationToolbar(self.canavas3_1_7, self)
		self.widget_ener1_7.addWidget(self.toolbar)


	def get3Second(self, fig):
		self.fig = fig
		self.widget_ener2 = QtWidgets.QVBoxLayout(self.widget_ener2)
		self.canavas3_2 = MyMplCanvas(self.fig)
		self.widget_ener2.addWidget(self.canavas3_2)
		self.toolbar = NavigationToolbar(self.canavas3_2, self)
		self.widget_ener2.addWidget(self.toolbar)


	def get3Third(self, fig):
		self.fig = fig
		self.widget_ener3 = QtWidgets.QVBoxLayout(self.widget_ener3)
		self.canavas3_3 = MyMplCanvas(self.fig)
		self.widget_ener3.addWidget(self.canavas3_3)
		self.toolbar = NavigationToolbar(self.canavas3_3, self)
		self.widget_ener3.addWidget(self.toolbar)


	def get3Fourth(self, fig):
		self.fig = fig
		self.widget_ener4 = QtWidgets.QVBoxLayout(self.widget_ener4)
		self.canavas3_4 = MyMplCanvas(self.fig)
		self.widget_ener4.addWidget(self.canavas3_4)
		self.toolbar = NavigationToolbar(self.canavas3_4, self)
		self.widget_ener4.addWidget(self.toolbar)


	def inputLab3(self):
		self.istart = (self.calendarWidget_1.selectedDate()).toPyDate()
		self.iend = (self.calendarWidget_2.selectedDate()).toPyDate()

		name = str(self.Input_username.text())
		tarif = str(self.comboBox_tarif.currentText())
		User = People(name, self.istart, self.iend, tarif)

		dev_name1 = str(self.Input_name1.text())
		dev_force1 = int(self.Input_force1.text())
		dev_time_vid1 = float(self.Input_time_vid1.text())
		dev_time_do1 = float(self.Input_time_do1.text())

		dev_name2 = str(self.Input_name2.text())
		dev_force2 = int(self.Input_force2.text())
		dev_time_vid2 = float(self.Input_time_vid2.text())
		dev_time_do2 = float(self.Input_time_do2.text())

		dev_name3 = str(self.Input_name3.text())
		dev_force3 = int(self.Input_force3.text())
		dev_time_vid3 = float(self.Input_time_vid3.text())
		dev_time_do3 = float(self.Input_time_do3.text())

		dev_name4 = str(self.Input_name4.text())
		dev_force4 = int(self.Input_force4.text())
		dev_time_vid4 = float(self.Input_time_vid4.text())
		dev_time_do4 = float(self.Input_time_do4.text())

		dev_name5 = str(self.Input_name5.text())
		dev_force5 = int(self.Input_force5.text())
		dev_time_vid5 = float(self.Input_time_vid5.text())
		dev_time_do5 = float(self.Input_time_do5.text())

		dev_name6 = str(self.Input_name6.text())
		dev_force6 = int(self.Input_force6.text())
		dev_time_vid6 = float(self.Input_time_vid6.text())
		dev_time_do6 = float(self.Input_time_do6.text())

		self.devices.append(Device(dev_name1, dev_force1))
		self.devices.append(Device(dev_name2, dev_force2))
		self.devices.append(Device(dev_name3, dev_force3))
		self.devices.append(Device(dev_name4, dev_force4))
		self.devices.append(Device(dev_name5, dev_force5))
		self.devices.append(Device(dev_name6, dev_force6))

		User.addScedule(self.devices[0], dev_time_vid1, dev_time_do1)
		User.addScedule(self.devices[1], dev_time_vid2, dev_time_do2)
		User.addScedule(self.devices[2], dev_time_vid3, dev_time_do3)
		User.addScedule(self.devices[3], dev_time_vid4, dev_time_do4)
		User.addScedule(self.devices[4], dev_time_vid5, dev_time_do5)
		User.addScedule(self.devices[5], dev_time_vid6, dev_time_do6)

		if(len(self.cash) != 0):
			for dev in self.cash:
				self.devices.append(Device(dev[0], dev[1]))
				User.addScedule(self.devices[len(self.devices)-1], dev[2], dev[3])

		return User


	def inputAddDevice(self):
		dev_name_new = str(self.Input_name_new.text())
		dev_force_new = int(self.Input_force_new.text())
		dev_time_vid_new = float(self.Input_time_vid_new.text())
		dev_time_do_new = float(self.Input_time_do_new.text())
		lst = []
		lst.append(dev_name_new)
		lst.append(dev_force_new)
		lst.append(dev_time_vid_new)
		lst.append(dev_time_do_new)
		print("Device saved")
		self.cash.append(lst)


	def doLab2(self):
		self.city = self.getCity()
		self.istart = (self.calendarWidget_1.selectedDate()).toPyDate()
		self.iend = (self.calendarWidget_2.selectedDate()).toPyDate()
		Graph = self.doLab1()
		Lab2 = self.inputLab2()
		self.get2First(Lab2)
		Answer = Lab2.getAnswer()
		Answer.append("Витрати енергії на опалення: " + str(self.calculateW(Lab2, Graph)) + "кВт*год")
		self.printAnswer(Answer)
		W = self.calculateW(Lab2, Graph)
		Tarif = Lab2.getTarif()
		Na1_kVt = Lab2.getNa1kVt()
		R = Lab2.getR()
		count_days = Graph.getDayPromizok()
		x = range(6)
		y = []
		for i in x:
			if(i != 0):
				y.append((R*count_days+W)*Tarif[i]*Na1_kVt[i])
			else:
				y.append(((R*count_days+W)*Tarif[i]*Na1_kVt[i])/4)
		self.get2Second(x, y)


	def printAnswer(self, Answer):
		self.lineEdit.setText(Answer[0])
		self.lineEdit_2.setText(Answer[1])
		self.lineEdit_23.setText(Answer[2])
		self.lineEdit_24.setText(Answer[3])


	def calculateW(self, Lab2, Graph):
		W = 0
		dic = Graph.getTempRegim()
		teplovtrata = Lab2.getTeplovtrata_time()
		for key1 in dic.keys():
			for key2 in teplovtrata.keys():
				if(key1 == key2):
					W += dic[key1]*(teplovtrata[key2]/1000)
		return float(f"{W:.{2}f}")


	def inputLab2(self):
		flag = 0
		decide = 0
		q = float(self.Input_q.text())
		s = float(self.Input_s.text())
		t_b = float(self.Input_temp_baka.text())
		t_s = float(self.Input_temp_shower.text())
		t_v = float(self.Input_temp_vanna.text())
		t_vhv = float(self.Input_temp_vhv.text())
		p = float(self.Input_people.text())
		c_s = float(self.Input_count_shower.text())
		c_v_v = float(self.Input_count_vater_vanna.text())
		c_v = float(self.Input_count_vanna.text())
		c_v_s = float(self.Input_count_vater_shower.text())
		t_i = float(self.Input_t_in.text())
		city = self.city
		if(float(self.Input_time_nagriv.text()) != 0):
			decide = float(self.Input_time_nagriv.text())
			flag = 1
		elif(float(self.Input_time_nagriv.text()) == 0):
			decide = float(self.Input_force_nagrivacha.text())
			flag = 2
		ta_t_e = float(self.Input_tarif_tepl_energ.text())
		ta_e_e = float(self.Input_tarif_elec_energ.text())
		co_v = float(self.Input_cost_vugil.text())
		co_d = float(self.Input_cost_drow.text())
		co_g = float(self.Input_cost_gas.text())
		co_p = float(self.Input_cost_pelet.text())
		return getLab2(q, s, t_b, t_s, t_v, t_vhv, p, c_v_s, c_s, c_v_v, c_v, t_i, 
						city, ta_t_e, ta_e_e, co_g, co_v, co_d, co_p, decide, flag)


	def get2First(self, Lab2):
		self.fig = Lab2.get_Graph_lab2()
		self.widget_lab2_3 = QtWidgets.QVBoxLayout(self.widget_lab2_3)
		self.canavas2_1 = MyMplCanvas(self.fig)
		self.widget_lab2_3.addWidget(self.canavas2_1)
		self.toolbar = NavigationToolbar(self.canavas2_1, self)
		self.widget_lab2_3.addWidget(self.toolbar)


	def get2Second(self, x, y):
		print("get2s")
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		ax.bar(x, y)
		ax.set_xticks(x)
		ax.set_xticklabels(['Газовий\nкотел', 'Вугільний\nкотел', 'Електричний\nкотел', "Дров'яний\nкотел", 'Крикетний\nкотел', "Централізоване\nопалення"])
		ax.set_facecolor('seashell')
		fig.set_facecolor('floralwhite')
		plt.title("Гістограма витрат на опалення для різних систем теплозабезпечення")
		plt.xlabel("Вартість за період, грн")
		plt.ylabel("Вид опалення")
		fig.set_figwidth(3)
		fig.set_figheight(2)
		self.fig = fig
		self.widget_lab2_2 = QtWidgets.QVBoxLayout(self.widget_lab2_2)
		self.canavas2_2 = MyMplCanvas(self.fig)
		self.widget_lab2_2.addWidget(self.canavas2_2)
		self.toolbar = NavigationToolbar(self.canavas2_2, self)
		self.widget_lab2_2.addWidget(self.toolbar)    


	def doLab1(self):
		self.city = self.getCity()
		self.istart = (self.calendarWidget_1.selectedDate()).toPyDate()
		self.iend = (self.calendarWidget_2.selectedDate()).toPyDate()
		Graph = getGraph(self.city, self.istart, self.iend)
		self.getFirst(Graph)
		self.getSecond(Graph)
		self.getThird(Graph)
		self.getFourth(Graph)
		self.getFifth(Graph)  
		self.getSixth(Graph)
		return Graph


	def getCity(self):
		city = self.comboBox.currentText()
		if(city == "Кривий ріг"):
			return "Кривий_ріг"
		else:
			return city


	def location_on_the_screen(self):
		ag = QDesktopWidget().availableGeometry.center()
		sg = QDesktopWidget().screenGeometry()
		widget = self.geometry()
		x = ag.width() - widget.width()
		y = 2 * ag.height() - sg.height() - widget.height()
		self.move(x, y)


	def showMesaggeD(self):
		self.WindowDownloadEnd.setIcon(QMessageBox.Information)
		self.WindowDownloadEnd.setWindowTitle("Повідомлення!")
		self.WindowDownloadEnd.setText("Вітаємо! Дані опрацьовано")
		self.WindowDownloadEnd.setStandardButtons(QMessageBox.Ok)
		self.WindowDownloadEnd.show()


	# def getFileName(self):
	#     wb_path = QtWidgets.QFileDialog.getOpenFileName(self, "Оберіть базу даних")
	#     self.wb_path = wb_path[0]


	def getFirst(self, Graph):
		self.fig = Graph.printGraphFirst()
		self.widget_tem1 = QtWidgets.QVBoxLayout(self.widget_tem1)
		self.canavas = MyMplCanvas(self.fig)
		self.widget_tem1.addWidget(self.canavas)
		self.toolbar = NavigationToolbar(self.canavas, self)
		self.widget_tem1.addWidget(self.toolbar)       


	def getSecond(self, Graph):
		self.fig = Graph.printGraphSecond()
		self.widget_tem2 = QtWidgets.QVBoxLayout(self.widget_tem2)
		self.canavas_2 = MyMplCanvas(self.fig)
		self.widget_tem2.addWidget(self.canavas_2)
		self.toolbar = NavigationToolbar(self.canavas_2, self)
		self.widget_tem2.addWidget(self.toolbar)


	def getThird(self, Graph):
		self.fig = Graph.printGraphThird()
		self.widget_vit1 = QtWidgets.QVBoxLayout(self.widget_vit1)
		self.canavas_3 = MyMplCanvas(self.fig)
		self.widget_vit1.addWidget(self.canavas_3)
		self.toolbar = NavigationToolbar(self.canavas_3, self)
		self.widget_vit1.addWidget(self.toolbar)


	def getFourth(self, Graph):
		self.fig = Graph.printGraphFourth()
		self.widget_vit2 = QtWidgets.QVBoxLayout(self.widget_vit2)
		self.canavas_4 = MyMplCanvas(self.fig)
		self.widget_vit2.addWidget(self.canavas_4)
		self.toolbar = NavigationToolbar(self.canavas_4, self)
		self.widget_vit2.addWidget(self.toolbar)

	def getFifth(self, Graph):
		self.fig = Graph.printInsolFirst()
		self.widget_son1 = QtWidgets.QVBoxLayout(self.widget_son1)
		self.canavas_5 = MyMplCanvas(self.fig)
		self.widget_son1.addWidget(self.canavas_5)
		self.toolbar = NavigationToolbar(self.canavas_5, self)
		self.widget_son1.addWidget(self.toolbar)


	def getSixth(self, Graph):
		self.fig = Graph.printInsolSecond()
		self.widget_son2 = QtWidgets.QVBoxLayout(self.widget_son2)
		self.canavas_6 = MyMplCanvas(self.fig)
		self.widget_son2.addWidget(self.canavas_6)
		self.toolbar = NavigationToolbar(self.canavas_6, self)
		self.widget_son2.addWidget(self.toolbar)


	def center_window(self):
		qtRectangle = self.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		self.move(qtRectangle.topLeft())


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	window.center_window()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()