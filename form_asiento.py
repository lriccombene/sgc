# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_asiento.ui'
#
# Created: Sat Mar 23 18:49:07 2019
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_asiento(object):
    def setupUi(self, form_asiento):
        form_asiento.setObjectName("form_asiento")
        form_asiento.resize(610, 285)
        form_asiento.setMinimumSize(QtCore.QSize(610, 265))
        form_asiento.setMaximumSize(QtCore.QSize(610, 285))
        form_asiento.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_asiento)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.cbx_primer_asiento = QtWidgets.QComboBox(form_asiento)
        self.cbx_primer_asiento.setObjectName("cbx_primer_asiento")
        self.cbx_primer_asiento.addItem("")
        self.cbx_primer_asiento.addItem("")
        self.gridLayout_2.addWidget(self.cbx_primer_asiento, 4, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(form_asiento)
        self.label_15.setMinimumSize(QtCore.QSize(75, 25))
        self.label_15.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)
        self.lne_cuit = QtWidgets.QLineEdit(form_asiento)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.gridLayout_4.addWidget(self.lne_cuit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 6, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 9, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 10, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem9, 0, 11, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem10, 0, 12, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem11, 0, 13, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem12, 0, 14, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem13, 0, 15, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_16 = QtWidgets.QLabel(form_asiento)
        self.label_16.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_8.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(form_asiento)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.horizontalLayout_8.addWidget(self.lne_razon_social)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem15)
        self.gridLayout_3.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)
        self.horizontalLayout_9.addLayout(self.gridLayout_3)
        self.line_2 = QtWidgets.QFrame(form_asiento)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_9.addWidget(self.line_2)
        self.btn_buscar = QtWidgets.QPushButton(form_asiento)
        self.btn_buscar.setMinimumSize(QtCore.QSize(75, 50))
        self.btn_buscar.setMaximumSize(QtCore.QSize(75, 50))
        self.btn_buscar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_9.addWidget(self.btn_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(form_asiento)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.btn_guardar = QtWidgets.QPushButton(form_asiento)
        self.btn_guardar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_guardar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_guardar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_guardar.setObjectName("btn_guardar")
        self.gridLayout_2.addWidget(self.btn_guardar, 5, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_asiento)
        self.tabWidget.setStyleSheet("QTabWidget{\n"
"background-color: rgb(123, 121, 143);\n"
"}\n"
"QLineEdit {\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.cbx_ejercicio = QtWidgets.QComboBox(self.tab)
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(250, 25))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(250, 25))
        self.cbx_ejercicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.horizontalLayout_2.addWidget(self.cbx_ejercicio)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.cbx_mes = QtWidgets.QComboBox(self.tab)
        self.cbx_mes.setMinimumSize(QtCore.QSize(150, 25))
        self.cbx_mes.setMaximumSize(QtCore.QSize(150, 25))
        self.cbx_mes.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_mes.setObjectName("cbx_mes")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.cbx_mes.addItem("")
        self.horizontalLayout_5.addWidget(self.cbx_mes)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMinimumSize(QtCore.QSize(53, 25))
        self.label_5.setMaximumSize(QtCore.QSize(53, 25))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.dte_fecha = QtWidgets.QDateEdit(self.tab)
        self.dte_fecha.setMinimumSize(QtCore.QSize(100, 25))
        self.dte_fecha.setMaximumSize(QtCore.QSize(100, 25))
        self.dte_fecha.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dte_fecha.setCalendarPopup(True)
        self.dte_fecha.setObjectName("dte_fecha")
        self.horizontalLayout_4.addWidget(self.dte_fecha)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(75, 25))
        self.label_2.setMaximumSize(QtCore.QSize(75, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lne_descripcion = QtWidgets.QLineEdit(self.tab)
        self.lne_descripcion.setMinimumSize(QtCore.QSize(310, 25))
        self.lne_descripcion.setMaximumSize(QtCore.QSize(310, 25))
        self.lne_descripcion.setText("")
        self.lne_descripcion.setObjectName("lne_descripcion")
        self.horizontalLayout_3.addWidget(self.lne_descripcion)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(form_asiento)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)

        self.retranslateUi(form_asiento)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_asiento)
        form_asiento.setTabOrder(self.lne_cuit, self.btn_buscar)
        form_asiento.setTabOrder(self.btn_buscar, self.lne_razon_social)
        form_asiento.setTabOrder(self.lne_razon_social, self.tabWidget)
        form_asiento.setTabOrder(self.tabWidget, self.cbx_ejercicio)
        form_asiento.setTabOrder(self.cbx_ejercicio, self.cbx_mes)
        form_asiento.setTabOrder(self.cbx_mes, self.dte_fecha)
        form_asiento.setTabOrder(self.dte_fecha, self.lne_descripcion)
        form_asiento.setTabOrder(self.lne_descripcion, self.btn_guardar)

    def retranslateUi(self, form_asiento):
        _translate = QtCore.QCoreApplication.translate
        form_asiento.setWindowTitle(_translate("form_asiento", "Nuevo Asiento"))
        self.cbx_primer_asiento.setItemText(0, _translate("form_asiento", "False"))
        self.cbx_primer_asiento.setItemText(1, _translate("form_asiento", "True"))
        self.label_15.setText(_translate("form_asiento", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_asiento", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_asiento", "Buscar"))
        self.btn_guardar.setText(_translate("form_asiento", "Guardar"))
        self.label_3.setText(_translate("form_asiento", "Ejercicio:"))
        self.label_4.setText(_translate("form_asiento", "Mes: "))
        self.cbx_mes.setItemText(0, _translate("form_asiento", "Enero"))
        self.cbx_mes.setItemText(1, _translate("form_asiento", "Febrero"))
        self.cbx_mes.setItemText(2, _translate("form_asiento", "Marzo"))
        self.cbx_mes.setItemText(3, _translate("form_asiento", "Abril"))
        self.cbx_mes.setItemText(4, _translate("form_asiento", "Mayo"))
        self.cbx_mes.setItemText(5, _translate("form_asiento", "Junio"))
        self.cbx_mes.setItemText(6, _translate("form_asiento", "Julio"))
        self.cbx_mes.setItemText(7, _translate("form_asiento", "Agosto"))
        self.cbx_mes.setItemText(8, _translate("form_asiento", "Septiembre"))
        self.cbx_mes.setItemText(9, _translate("form_asiento", "Octubre"))
        self.cbx_mes.setItemText(10, _translate("form_asiento", "Nombiembre"))
        self.cbx_mes.setItemText(11, _translate("form_asiento", "Diciembre"))
        self.label_5.setText(_translate("form_asiento", "Fecha:"))
        self.dte_fecha.setDisplayFormat(_translate("form_asiento", "dd/MM/yyyy"))
        self.label_2.setText(_translate("form_asiento", "Descripción:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_asiento", "Asiento"))
        self.label.setText(_translate("form_asiento", "Primer asiento: "))

