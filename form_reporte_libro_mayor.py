# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_reporte_libro_mayor.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_reporte_libro_mayor(object):
    def setupUi(self, form_reporte_libro_mayor):
        form_reporte_libro_mayor.setObjectName("form_reporte_libro_mayor")
        form_reporte_libro_mayor.resize(755, 180)
        form_reporte_libro_mayor.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout = QtWidgets.QGridLayout(form_reporte_libro_mayor)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_17 = QtWidgets.QLabel(form_reporte_libro_mayor)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_19.addWidget(self.label_17)
        self.lne_cuit_2 = QtWidgets.QLineEdit(form_reporte_libro_mayor)
        self.lne_cuit_2.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit_2.setText("")
        self.lne_cuit_2.setObjectName("lne_cuit_2")
        self.horizontalLayout_19.addWidget(self.lne_cuit_2)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_18 = QtWidgets.QLabel(form_reporte_libro_mayor)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_20.addWidget(self.label_18)
        self.lne_razon_social_2 = QtWidgets.QLineEdit(form_reporte_libro_mayor)
        self.lne_razon_social_2.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social_2.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social_2.setObjectName("lne_razon_social_2")
        self.horizontalLayout_20.addWidget(self.lne_razon_social_2)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_20)
        self.line_2 = QtWidgets.QFrame(form_reporte_libro_mayor)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_18.addWidget(self.line_2)
        self.btn_buscar_2 = QtWidgets.QPushButton(form_reporte_libro_mayor)
        self.btn_buscar_2.setMinimumSize(QtCore.QSize(75, 50))
        self.btn_buscar_2.setMaximumSize(QtCore.QSize(75, 50))
        self.btn_buscar_2.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar_2.setObjectName("btn_buscar_2")
        self.horizontalLayout_18.addWidget(self.btn_buscar_2)
        self.gridLayout.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(form_reporte_libro_mayor)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 6, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 7, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 8, 1, 1)
        self.label_21 = QtWidgets.QLabel(form_reporte_libro_mayor)
        self.label_21.setMinimumSize(QtCore.QSize(60, 0))
        self.label_21.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 9, 1, 1)
        self.cbx_ejercicio = QtWidgets.QComboBox(form_reporte_libro_mayor)
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_ejercicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.gridLayout_4.addWidget(self.cbx_ejercicio, 0, 10, 1, 1)
        self.line_4 = QtWidgets.QFrame(form_reporte_libro_mayor)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 0, 11, 1, 1)
        self.btn_buscar_asiento = QtWidgets.QPushButton(form_reporte_libro_mayor)
        self.btn_buscar_asiento.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar_asiento.setObjectName("btn_buscar_asiento")
        self.gridLayout_4.addWidget(self.btn_buscar_asiento, 0, 12, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.btn_imprimir = QtWidgets.QPushButton(form_reporte_libro_mayor)
        self.btn_imprimir.setStyleSheet("background-color: rgb(144, 169, 191);")
        self.btn_imprimir.setObjectName("btn_imprimir")
        self.gridLayout.addWidget(self.btn_imprimir, 3, 0, 1, 1)

        self.retranslateUi(form_reporte_libro_mayor)
        QtCore.QMetaObject.connectSlotsByName(form_reporte_libro_mayor)
        form_reporte_libro_mayor.setTabOrder(self.lne_cuit_2, self.lne_razon_social_2)
        form_reporte_libro_mayor.setTabOrder(self.lne_razon_social_2, self.btn_buscar_2)
        form_reporte_libro_mayor.setTabOrder(self.btn_buscar_2, self.cbx_ejercicio)
        form_reporte_libro_mayor.setTabOrder(self.cbx_ejercicio, self.btn_buscar_asiento)
        form_reporte_libro_mayor.setTabOrder(self.btn_buscar_asiento, self.btn_imprimir)

    def retranslateUi(self, form_reporte_libro_mayor):
        _translate = QtCore.QCoreApplication.translate
        form_reporte_libro_mayor.setWindowTitle(_translate("form_reporte_libro_mayor", "Reporte de Libro Mayor"))
        self.label_17.setText(_translate("form_reporte_libro_mayor", "CUIT / CUIL: "))
        self.label_18.setText(_translate("form_reporte_libro_mayor", "Razón Social: "))
        self.btn_buscar_2.setText(_translate("form_reporte_libro_mayor", "Buscar"))
        self.label_21.setText(_translate("form_reporte_libro_mayor", "Ejercicio:"))
        self.btn_buscar_asiento.setText(_translate("form_reporte_libro_mayor", "Buscar"))
        self.btn_imprimir.setText(_translate("form_reporte_libro_mayor", "Imprimir "))

