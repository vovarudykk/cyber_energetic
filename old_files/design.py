# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design3.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1127, 849)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_0 = QtWidgets.QWidget()
        self.tab_0.setObjectName("tab_0")
        self.calendarWidget_1 = QtWidgets.QCalendarWidget(self.tab_0)
        self.calendarWidget_1.setGeometry(QtCore.QRect(90, 320, 392, 236))
        self.calendarWidget_1.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.calendarWidget_1.setSelectedDate(QtCore.QDate(2012, 1, 1))
        self.calendarWidget_1.setMinimumDate(QtCore.QDate(2012, 1, 1))
        self.calendarWidget_1.setMaximumDate(QtCore.QDate(2012, 12, 30))
        self.calendarWidget_1.setGridVisible(False)
        self.calendarWidget_1.setNavigationBarVisible(True)
        self.calendarWidget_1.setDateEditEnabled(True)
        self.calendarWidget_1.setObjectName("calendarWidget_1")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(self.tab_0)
        self.calendarWidget_2.setGeometry(QtCore.QRect(610, 320, 392, 236))
        self.calendarWidget_2.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.calendarWidget_2.setSelectedDate(QtCore.QDate(2012, 12, 31))
        self.calendarWidget_2.setMinimumDate(QtCore.QDate(2012, 1, 2))
        self.calendarWidget_2.setMaximumDate(QtCore.QDate(2012, 12, 31))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_0)
        self.comboBox.setGeometry(QtCore.QRect(440, 100, 221, 51))
        self.comboBox.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_1 = QtWidgets.QLabel(self.tab_0)
        self.label_1.setGeometry(QtCore.QRect(90, 230, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.tab_0)
        self.label_2.setGeometry(QtCore.QRect(610, 230, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label_2")
        self.label_0 = QtWidgets.QLabel(self.tab_0)
        self.label_0.setGeometry(QtCore.QRect(440, 40, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_0.setFont(font)
        self.label_0.setAlignment(QtCore.Qt.AlignCenter)
        self.label_0.setWordWrap(False)
        self.label_0.setObjectName("label_0")
        self.pushButtonConfirm = QtWidgets.QPushButton(self.tab_0)
        self.pushButtonConfirm.setGeometry(QtCore.QRect(440, 660, 221, 51))
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.tabWidget.addTab(self.tab_0, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.EnterBD = QtWidgets.QTabWidget(self.tab_1)
        self.EnterBD.setGeometry(QtCore.QRect(0, 0, 1101, 821))
        self.EnterBD.setObjectName("EnterBD")
        self.tab_tem = QtWidgets.QWidget()
        self.tab_tem.setObjectName("tab_tem")
        self.widget = QtWidgets.QWidget(self.tab_tem)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 1101, 731))
        self.widget.setObjectName("widget")
        self.EnterBD_2 = QtWidgets.QTabWidget(self.tab_tem)
        self.EnterBD_2.setGeometry(QtCore.QRect(-10, 0, 1111, 821))
        self.EnterBD_2.setObjectName("EnterBD_2")
        self.tab_tem1 = QtWidgets.QWidget()
        self.tab_tem1.setObjectName("tab_tem1")
        self.widget_tem1 = QtWidgets.QWidget(self.tab_tem1)
        self.widget_tem1.setGeometry(QtCore.QRect(-1, -1, 1101, 731))
        self.widget_tem1.setObjectName("widget_tem1")
        self.EnterBD_2.addTab(self.tab_tem1, "")
        self.tab_tem2 = QtWidgets.QWidget()
        self.tab_tem2.setObjectName("tab_tem2")
        self.widget_tem2 = QtWidgets.QWidget(self.tab_tem2)
        self.widget_tem2.setGeometry(QtCore.QRect(0, 0, 1101, 731))
        self.widget_tem2.setObjectName("widget_tem2")
        self.EnterBD_2.addTab(self.tab_tem2, "")
        self.EnterBD.addTab(self.tab_tem, "")
        self.tab_vit = QtWidgets.QWidget()
        self.tab_vit.setObjectName("tab_vit")
        self.widget_2 = QtWidgets.QWidget(self.tab_vit)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1101, 731))
        self.widget_2.setObjectName("widget_2")
        self.EnterBD_4 = QtWidgets.QTabWidget(self.widget_2)
        self.EnterBD_4.setGeometry(QtCore.QRect(-10, 0, 1121, 831))
        self.EnterBD_4.setObjectName("EnterBD_4")
        self.tab_vit1 = QtWidgets.QWidget()
        self.tab_vit1.setObjectName("tab_vit1")
        self.widget_vit1 = QtWidgets.QWidget(self.tab_vit1)
        self.widget_vit1.setGeometry(QtCore.QRect(-1, 0, 1101, 701))
        self.widget_vit1.setObjectName("widget_vit1")
        self.EnterBD_4.addTab(self.tab_vit1, "")
        self.tab_vit2 = QtWidgets.QWidget()
        self.tab_vit2.setObjectName("tab_vit2")
        self.widget_vit2 = QtWidgets.QWidget(self.tab_vit2)
        self.widget_vit2.setGeometry(QtCore.QRect(0, 0, 1101, 691))
        self.widget_vit2.setObjectName("widget_vit2")
        self.EnterBD_4.addTab(self.tab_vit2, "")
        self.EnterBD.addTab(self.tab_vit, "")
        self.tab_son = QtWidgets.QWidget()
        self.tab_son.setObjectName("tab_son")
        self.widget_3 = QtWidgets.QWidget(self.tab_son)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1101, 731))
        self.widget_3.setObjectName("widget_3")
        self.EnterBD_3 = QtWidgets.QTabWidget(self.widget_3)
        self.EnterBD_3.setGeometry(QtCore.QRect(-10, 0, 1121, 821))
        self.EnterBD_3.setObjectName("EnterBD_3")
        self.tab_son1 = QtWidgets.QWidget()
        self.tab_son1.setObjectName("tab_son1")
        self.widget_son1 = QtWidgets.QWidget(self.tab_son1)
        self.widget_son1.setGeometry(QtCore.QRect(-1, -1, 1101, 721))
        self.widget_son1.setObjectName("widget_son1")
        self.EnterBD_3.addTab(self.tab_son1, "")
        self.tab_son2 = QtWidgets.QWidget()
        self.tab_son2.setObjectName("tab_son2")
        self.widget_son2 = QtWidgets.QWidget(self.tab_son2)
        self.widget_son2.setGeometry(QtCore.QRect(0, 0, 1101, 721))
        self.widget_son2.setObjectName("widget_son2")
        self.EnterBD_3.addTab(self.tab_son2, "")
        self.EnterBD.addTab(self.tab_son, "")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.EnterBD.setCurrentIndex(0)
        self.EnterBD_2.setCurrentIndex(0)
        self.EnterBD_4.setCurrentIndex(0)
        self.EnterBD_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Не обрано"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Дніпро"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Донецьк"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Івано-Франківськ"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Київ"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Кривий ріг"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Луганськ"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Львів"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Симферополь"))
        self.comboBox.setItemText(9, _translate("MainWindow", "Одеса"))
        self.comboBox.setItemText(10, _translate("MainWindow", "Харків"))
        self.label_1.setText(_translate("MainWindow", "Оберіть початкову дату"))
        self.label_2.setText(_translate("MainWindow", "Оберіть кінцеву дату"))
        self.label_0.setText(_translate("MainWindow", "Оберіть місто"))
        self.pushButtonConfirm.setText(_translate("MainWindow", "Підтвердити"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_0), _translate("MainWindow", "Ввід даних"))
        self.EnterBD_2.setTabText(self.EnterBD_2.indexOf(self.tab_tem1), _translate("MainWindow", "Температурні умови"))
        self.EnterBD_2.setTabText(self.EnterBD_2.indexOf(self.tab_tem2), _translate("MainWindow", "Тривалість температурних режимів"))
        self.EnterBD.setTabText(self.EnterBD.indexOf(self.tab_tem), _translate("MainWindow", "Температурна активність"))
        self.EnterBD_4.setTabText(self.EnterBD_4.indexOf(self.tab_vit1), _translate("MainWindow", "Роза вітрів"))
        self.EnterBD_4.setTabText(self.EnterBD_4.indexOf(self.tab_vit2), _translate("MainWindow", "Тривалість режимів вітрової активності"))
        self.EnterBD.setTabText(self.EnterBD.indexOf(self.tab_vit), _translate("MainWindow", "Вітряна активність"))
        self.EnterBD_3.setTabText(self.EnterBD_3.indexOf(self.tab_son1), _translate("MainWindow", "Інтенсивність сонячної інсоляції"))
        self.EnterBD_3.setTabText(self.EnterBD_3.indexOf(self.tab_son2), _translate("MainWindow", "Тривалість режимів сонячної активності"))
        self.EnterBD.setTabText(self.EnterBD.indexOf(self.tab_son), _translate("MainWindow", "Сонячна активність"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Вкладка 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Вкладка 2"))
