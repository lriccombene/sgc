# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_cuentas.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_cuentas(object):
    def setupUi(self, form_cuentas):
        form_cuentas.setObjectName("form_cuentas")
        form_cuentas.resize(767, 571)
        form_cuentas.setStyleSheet("font: 10pt \"Liberation Sans\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(156, 156, 156);\n"
"selection-background-color: rgb(164, 190, 221);\n"
"selection-color: rgb(0, 0, 0);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_cuentas)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(form_cuentas)
        self.label_15.setMinimumSize(QtCore.QSize(80, 0))
        self.label_15.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(form_cuentas)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.horizontalLayout_15.addWidget(self.lne_cuit)
        self.gridLayout_3.addLayout(self.horizontalLayout_15, 0, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(form_cuentas)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(form_cuentas)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.horizontalLayout_16.addWidget(self.lne_razon_social)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(form_cuentas)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 0, 2, 1, 1)
        self.btn_buscar = QtWidgets.QPushButton(form_cuentas)
        self.btn_buscar.setMinimumSize(QtCore.QSize(75, 50))
        self.btn_buscar.setMaximumSize(QtCore.QSize(75, 50))
        self.btn_buscar.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.gridLayout_3.addWidget(self.btn_buscar, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.line_2 = QtWidgets.QFrame(form_cuentas)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 6, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 7, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 0, 8, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 0, 9, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem8, 0, 10, 1, 1)
        self.label_21 = QtWidgets.QLabel(form_cuentas)
        self.label_21.setMinimumSize(QtCore.QSize(60, 0))
        self.label_21.setMaximumSize(QtCore.QSize(75, 16777215))
        self.label_21.setObjectName("label_21")
        self.gridLayout_4.addWidget(self.label_21, 0, 11, 1, 1)
        self.cbx_ejercicio = QtWidgets.QComboBox(form_cuentas)
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_ejercicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.gridLayout_4.addWidget(self.cbx_ejercicio, 0, 12, 1, 1)
        self.line_4 = QtWidgets.QFrame(form_cuentas)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_4.addWidget(self.line_4, 0, 13, 1, 1)
        self.btn_buscar_asiento = QtWidgets.QPushButton(form_cuentas)
        self.btn_buscar_asiento.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_buscar_asiento.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_buscar_asiento.setObjectName("btn_buscar_asiento")
        self.gridLayout_4.addWidget(self.btn_buscar_asiento, 0, 14, 1, 1)
        self.btn_eliminar = QtWidgets.QPushButton(form_cuentas)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.gridLayout_4.addWidget(self.btn_eliminar, 0, 0, 1, 1)
        self.btn_eliminar_cuenta = QtWidgets.QPushButton(form_cuentas)
        self.btn_eliminar_cuenta.setObjectName("btn_eliminar_cuenta")
        self.gridLayout_4.addWidget(self.btn_eliminar_cuenta, 0, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(form_cuentas)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_cuentas)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tw_asiento = QtWidgets.QTableWidget(self.tab)
        self.tw_asiento.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_asiento.setObjectName("tw_asiento")
        self.tw_asiento.setColumnCount(2)
        self.tw_asiento.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(151, 177, 199))
        self.tw_asiento.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(164, 184, 199))
        self.tw_asiento.setHorizontalHeaderItem(1, item)
        self.tw_asiento.horizontalHeader().setDefaultSectionSize(375)
        self.gridLayout_5.addWidget(self.tw_asiento, 0, 0, 1, 1)
        self.tw_cuentas = QtWidgets.QTableWidget(self.tab)
        self.tw_cuentas.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tw_cuentas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_cuentas.setObjectName("tw_cuentas")
        self.tw_cuentas.setColumnCount(5)
        self.tw_cuentas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(164, 185, 200))
        self.tw_cuentas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(164, 185, 200))
        self.tw_cuentas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(164, 185, 200))
        self.tw_cuentas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(164, 185, 200))
        self.tw_cuentas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_cuentas.setHorizontalHeaderItem(4, item)
        self.tw_cuentas.horizontalHeader().setDefaultSectionSize(200)
        self.gridLayout_5.addWidget(self.tw_cuentas, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.btn_nueva_cuenta = QtWidgets.QPushButton(self.tab)
        self.btn_nueva_cuenta.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_nueva_cuenta.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_nueva_cuenta.setStyleSheet("background-color: rgb(119, 149, 177);")
        self.btn_nueva_cuenta.setObjectName("btn_nueva_cuenta")
        self.gridLayout.addWidget(self.btn_nueva_cuenta, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 1)

        self.retranslateUi(form_cuentas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_cuentas)
        form_cuentas.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_cuentas.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_cuentas.setTabOrder(self.btn_buscar, self.cbx_ejercicio)
        form_cuentas.setTabOrder(self.cbx_ejercicio, self.btn_buscar_asiento)
        form_cuentas.setTabOrder(self.btn_buscar_asiento, self.tabWidget)
        form_cuentas.setTabOrder(self.tabWidget, self.tw_asiento)
        form_cuentas.setTabOrder(self.tw_asiento, self.tw_cuentas)
        form_cuentas.setTabOrder(self.tw_cuentas, self.btn_nueva_cuenta)

    def retranslateUi(self, form_cuentas):
        _translate = QtCore.QCoreApplication.translate
        form_cuentas.setWindowTitle(_translate("form_cuentas", "Buscar Cuenta"))
        self.label_15.setText(_translate("form_cuentas", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_cuentas", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_cuentas", "Buscar"))
        self.label_21.setText(_translate("form_cuentas", "Ejercicio:"))
        self.btn_buscar_asiento.setText(_translate("form_cuentas", "Buscar"))
        self.btn_eliminar.setText(_translate("form_cuentas", "Eliminar"))
        self.btn_eliminar_cuenta.setText(_translate("form_cuentas", "Eliminar Cuenta"))
        item = self.tw_asiento.horizontalHeaderItem(0)
        item.setText(_translate("form_cuentas", "Fecha"))
        item = self.tw_asiento.horizontalHeaderItem(1)
        item.setText(_translate("form_cuentas", "Descripción"))
        item = self.tw_cuentas.horizontalHeaderItem(0)
        item.setText(_translate("form_cuentas", "Código"))
        item = self.tw_cuentas.horizontalHeaderItem(1)
        item.setText(_translate("form_cuentas", "Descripción"))
        item = self.tw_cuentas.horizontalHeaderItem(2)
        item.setText(_translate("form_cuentas", "Debe"))
        item = self.tw_cuentas.horizontalHeaderItem(3)
        item.setText(_translate("form_cuentas", "Haber"))
        item = self.tw_cuentas.horizontalHeaderItem(4)
        item.setText(_translate("form_cuentas", "ID"))
        self.btn_nueva_cuenta.setText(_translate("form_cuentas", "Nueva Cuenta"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_cuentas", "Asiento"))

