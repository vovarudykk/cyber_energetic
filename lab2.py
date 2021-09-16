import matplotlib.pyplot as plt
import mplcursors


class getLab2:
	def __init__(self, q, s, t_b, t_s, t_v, t_vhv, p, c_v_s, c_s, c_v_v, c_v, t_i, 
				city, ta_t_e, ta_e_e, co_g, co_v, co_d, co_p, decide, flag):
		self.q = q
		self.s = s
		self.temp_baka = t_b
		self.temp_shower = t_s
		self.temp_vanna = t_v
		self.temp_vhv = t_vhv
		self.people = p
		self.count_vater_shower = c_v_s
		self.count_shower = c_s
		self.count_vater_vanna = c_v_v
		self.count_vanna = c_v

		self.flag = flag
		self.t_in = t_i
		self.dic_t_out = {"Дніпро":-23, "Донецьк":-23, "Івано-Франківськ":-20, "Київ":-22, 
					"Кривий ріг":-23, "Луганськ":-25, "Львів":-19, "Симферополь":-16, "Одеса":-18, "Харків":-23}

		self.t_out = self.dic_t_out[city]

		self.tarif_tepl_energ = ta_t_e*0.00086
		self.tarif_elec_energ = ta_e_e
		self.cost_gas = co_g*0.00086
		self.cost_vugil = co_v/1000
		self.cost_drow = co_d/1000
		self.cost_pelet = co_p/1000

		self.q_shower = self.count_shower * self.count_vater_shower
		self.q_vanna = self.count_vanna * self.count_vater_vanna
		self.q_shower_temp = self.q_shower * (self.temp_shower - self.temp_vhv)/(self.temp_baka - self.temp_vhv)
		self.q_vanna_temp = self.q_vanna * (self.temp_vanna - self.temp_vhv)/(self.temp_baka - self.temp_vhv)	
		self.Q = (self.q_shower_temp + self.q_vanna_temp) / 998.23
		self.Answer = ["Кількість витрат гарячої води: " + str(float(f"{self.Q:.{2}f}")) + "м³/добу"]
		self.Wgar_vod = 1.163*self.Q*(self.temp_baka-self.temp_vhv)
		self.Rgvp = 1
		self.time_nagriv = 1
		if(flag == 2):
			self.Rgvp = decide
			self.time_nagriv = self.Wgar_vod/self.Rgvp
			self.Answer.append("Потужність нагрівача: " + str(float(f"{self.Rgvp:.{2}f}")) + "кВт") 
			self.Answer.append("Тривалість нагріву ємності: " + str(float(f"{self.time_nagriv:.{2}f}")) + "год")

		elif(flag == 1):
			self.time_nagriv == decide
			self.Rgvp = self.Wgar_vod/self.time_nagriv
			self.Answer.append("Потужність нагрівача: " + str(float(f"{self.Rgvp:.{2}f}")) + "кВт") 
			self.Answer.append("Тривалість нагріву ємності: " + str(float(f"{self.time_nagriv:.{2}f}")) + "год")


		self.gas_na1_kvt = 0.1075 #m^3
		self.vugil_na1_kvt = 0.1792 #kg
		self.pelet_na1_kvt = 0.1953 #kg
		self.drow_na1_kvt = 0.287 #kg
		self.elec_na1_kvt = 1.01 #kvt*god

		self.Tarif = [self.cost_gas, self.cost_vugil, self.tarif_elec_energ, self.cost_drow, self.cost_pelet, self.tarif_tepl_energ]
		self.Na1_kvt = [self.tarif_tepl_energ, self.vugil_na1_kvt, self.elec_na1_kvt, self.drow_na1_kvt, self.pelet_na1_kvt, self.tarif_tepl_energ]
		self.Teplovtrata_time = {}

	def getTarif(self):
			return self.Tarif

	def getNa1kVt(self):
			return self.Na1_kvt


	def getTeplovtrata_time(self):
		return self.Teplovtrata_time

	def getR(self):
		return self.Rgvp

	def getQ(self):
		return self.Q

	def getAnswer(self):
		return self.Answer

	# def get_Gisto_lab2():
	# 	dic = {}
	# 	unique = list(set(self.y))
	# 	for i in range(len(unique)):
	# 		dic[unique[i]] = 0

	# 	for i in range(len(self.y)):
	# 		dic[self.y[i]] += 0.5

	# 	fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
	# 	ax.bar(list(dic.keys()), list(dic.values()))
	# 	ax.set_facecolor('seashell')
	# 	fig.set_facecolor('floralwhite')
	# 	plt.title("Тривалість температурних режимів") # заголовок
	# 	plt.xlabel("Температура, ℃") # ось абсцисс
	# 	plt.ylabel("Час, год") # ось ординат
	# 	fig.set_figwidth(12)    #  ширина Figure
	# 	fig.set_figheight(6)    #  высота Figure
	# 	plt.grid(axis = 'y')
	# 	# y.clear()
	# 	# plt.show()
	# 	return fig


	def get_Graph_lab2(self):
		fig, ax = plt.subplots(figsize=(20,10), dpi = 100)
		plt.xlabel("Температура, °С") # ось абсцисс
		plt.ylabel("Тепловтрата, кВт") # ось ординат
		# plt.grid()      # включение отображение сетки
		
		k = (self.q * self.s - 0) / (self.t_out - 20)
		b = 0 - k * 20
		x = range(self.t_out, 21)
		y = []
		for i in x:
			y.append(k*i+b)

		for i in range(len(x)):
			self.Teplovtrata_time = dict(zip(x, y)) 

		p = 'y = '+str(float(f"{k:.{2}f}"))+'x + '+str(float(f"{b:.{2}f}"))
		plt.plot((self.t_out, 20),(self.q*self.s, 0), c='black')
		scat = plt.scatter(x, y, marker = 'o', c = 'red', edgecolors = 'black',alpha = 0.6)

		
		
		plt.title("Залежність тепловтрат будівлі від температурних умов\nАналітична залежність: y = " + str(float(f"{k:.{2}f}")) + "x + " + str(float(f"{b:.{2}f}"))) # заголовок
		for i in range(self.t_out, 21):
			plt.axvline(x=i, color='grey', linewidth=0.1)
			plt.axhline(y=y[i], color='grey', linewidth=0.1)

		if self.t_in != 20:
			y_ = list(range(self.t_out, 21))
			y1 = []

			for i in range(0, len(y_)):
				if self.t_in < 20:
					y_[i] -= (20 - self.t_in)
				else:
					y_[i] += (self.t_in - 20)

			k = (self.q*self.s - 0) / (self.t_out - y_[0])
			b = 0 - k * y_[0]

			for i in y_:
				y1.append(k*i+b)

			scat1 = plt.scatter(y_, y, marker = 'o', c = 'green', edgecolors = 'black',alpha = 0.6)
			plt.plot((y_[0], self.t_in),(self.q*self.s, 0), c='green')


		cursor = mplcursors.cursor(scat, hover=True)
		cursor.connect("add", lambda sel: sel.annotation.set_text(
			'Пряма: {}\n Температура: {}\nТепловтрата:{}'.format(p, sel.target[0], round(sel.target[1], 1))))

		p1 = 'y = '+str(float(f"{k:.{2}f}"))+'x + '+str(float(f"{b:.{2}f}"))
		cursor = mplcursors.cursor(scat1, hover=True)
		cursor.connect("add", lambda sel: sel.annotation.set_text(
			'Пряма: {}\n Температура: {}\nТепловтрата:{}'.format(p1, sel.target[0], round(sel.target[1], 1))))

		# plt.show()
		return fig


def main():
	decide = 3
	flag = 1
	#				q,  s,  t_b,   t_s, t_v, t_vhv, p, c_v_s, c_s, c_v_v, c_v, t_i, 
	Lab2 = getLab2(30, 80, 85,    80,  90,   15,   4,  50,    1,   150,   2,   18,
	#				city,      ta_t_e, ta_e_e,   co_g,     co_v,     co_d,    co_p,    decide, flag 
					"Дніпро",   1.33,    0.9,    2975,    2746.75,   948.75, 4832.64,  decide, flag)
	Lab2.get_Graph_lab2()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
	main()  # то запускаем функцию main())
