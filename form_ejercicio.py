# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_ejercicio.ui'
#
# Created: Sun Mar 24 10:33:25 2019
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_ejercicio(object):
    def setupUi(self, form_ejercicio):
        form_ejercicio.setObjectName("form_ejercicio")
        form_ejercicio.resize(714, 586)
        form_ejercicio.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_ejercicio)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(form_ejercicio)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(self.tab)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.tw_ejercicio = QtWidgets.QTableWidget(self.tab)
        self.tw_ejercicio.setMinimumSize(QtCore.QSize(200, 0))
        self.tw_ejercicio.setStyleSheet("")
        self.tw_ejercicio.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked)
        self.tw_ejercicio.setObjectName("tw_ejercicio")
        self.tw_ejercicio.setColumnCount(4)
        self.tw_ejercicio.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(149, 175, 197))
        self.tw_ejercicio.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 180, 199))
        self.tw_ejercicio.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 180, 199))
        self.tw_ejercicio.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ejercicio.setHorizontalHeaderItem(3, item)
        self.tw_ejercicio.horizontalHeader().setDefaultSectionSize(250)
        self.gridLayout.addWidget(self.tw_ejercicio, 2, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tw_detalle_ejerc = QtWidgets.QTableWidget(self.tab)
        self.tw_detalle_ejerc.setStyleSheet("")
        self.tw_detalle_ejerc.setObjectName("tw_detalle_ejerc")
        self.tw_detalle_ejerc.setColumnCount(3)
        self.tw_detalle_ejerc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 180, 199))
        self.tw_detalle_ejerc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 180, 199))
        self.tw_detalle_ejerc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(158, 180, 199))
        self.tw_detalle_ejerc.setHorizontalHeaderItem(2, item)
        self.tw_detalle_ejerc.horizontalHeader().setDefaultSectionSize(250)
        self.verticalLayout_3.addWidget(self.tw_detalle_ejerc)
        self.btn_cerrar = QtWidgets.QPushButton(self.tab)
        self.btn_cerrar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_cerrar.setObjectName("btn_cerrar")
        self.verticalLayout_3.addWidget(self.btn_cerrar)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        self.label_15.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(self.tab)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.horizontalLayout_6.addWidget(self.lne_cuit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setMinimumSize(QtCore.QSize(85, 0))
        self.label_16.setMaximumSize(QtCore.QSize(85, 16777215))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_7.addWidget(self.label_16)
        self.ln_nombre = QtWidgets.QLineEdit(self.tab)
        self.ln_nombre.setMinimumSize(QtCore.QSize(350, 0))
        self.ln_nombre.setMaximumSize(QtCore.QSize(350, 16777215))
        self.ln_nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ln_nombre.setObjectName("ln_nombre")
        self.horizontalLayout_7.addWidget(self.ln_nombre)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_buscar = QtWidgets.QPushButton(self.tab)
        self.btn_buscar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_3.addWidget(self.btn_buscar)
        self.btn_actualizar = QtWidgets.QPushButton(self.tab)
        self.btn_actualizar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_actualizar.setObjectName("btn_actualizar")
        self.horizontalLayout_3.addWidget(self.btn_actualizar)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_eliminar = QtWidgets.QPushButton(self.tab)
        self.btn_eliminar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout_4.addWidget(self.btn_eliminar)
        self.btn_nuevo = QtWidgets.QPushButton(self.tab)
        self.btn_nuevo.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.horizontalLayout_4.addWidget(self.btn_nuevo)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.btn_inflacion = QtWidgets.QPushButton(self.tab)
        self.btn_inflacion.setObjectName("btn_inflacion")
        self.gridLayout.addWidget(self.btn_inflacion, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(form_ejercicio)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_ejercicio)
        form_ejercicio.setTabOrder(self.tabWidget, self.lne_cuit)
        form_ejercicio.setTabOrder(self.lne_cuit, self.btn_buscar)
        form_ejercicio.setTabOrder(self.btn_buscar, self.ln_nombre)
        form_ejercicio.setTabOrder(self.ln_nombre, self.btn_eliminar)
        form_ejercicio.setTabOrder(self.btn_eliminar, self.btn_actualizar)
        form_ejercicio.setTabOrder(self.btn_actualizar, self.btn_nuevo)
        form_ejercicio.setTabOrder(self.btn_nuevo, self.tw_ejercicio)
        form_ejercicio.setTabOrder(self.tw_ejercicio, self.tw_detalle_ejerc)
        form_ejercicio.setTabOrder(self.tw_detalle_ejerc, self.btn_cerrar)

    def retranslateUi(self, form_ejercicio):
        _translate = QtCore.QCoreApplication.translate
        form_ejercicio.setWindowTitle(_translate("form_ejercicio", "Buscar Ejercicio"))
        item = self.tw_ejercicio.horizontalHeaderItem(0)
        item.setText(_translate("form_ejercicio", "Año"))
        item = self.tw_ejercicio.horizontalHeaderItem(1)
        item.setText(_translate("form_ejercicio", "Descripción"))
        item = self.tw_ejercicio.horizontalHeaderItem(2)
        item.setText(_translate("form_ejercicio", "Tipo"))
        item = self.tw_ejercicio.horizontalHeaderItem(3)
        item.setText(_translate("form_ejercicio", "ID"))
        item = self.tw_detalle_ejerc.horizontalHeaderItem(0)
        item.setText(_translate("form_ejercicio", "N°"))
        item = self.tw_detalle_ejerc.horizontalHeaderItem(1)
        item.setText(_translate("form_ejercicio", "Mes"))
        item = self.tw_detalle_ejerc.horizontalHeaderItem(2)
        item.setText(_translate("form_ejercicio", "Estado"))
        self.btn_cerrar.setText(_translate("form_ejercicio", "Cerrar"))
        self.label_15.setText(_translate("form_ejercicio", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_ejercicio", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_ejercicio", "Buscar"))
        self.btn_actualizar.setText(_translate("form_ejercicio", "Actualizar"))
        self.btn_eliminar.setText(_translate("form_ejercicio", "Eliminar"))
        self.btn_nuevo.setText(_translate("form_ejercicio", "Nuevo"))
        self.btn_inflacion.setText(_translate("form_ejercicio", "calcular inflacion"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_ejercicio", "Ejercicio"))

