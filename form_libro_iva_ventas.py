# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_libro_iva_ventas.ui'
#
# Created: Wed Feb 14 21:25:46 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_libro_iva_ventas(object):
    def setupUi(self, form_libro_iva_ventas):
        form_libro_iva_ventas.setObjectName("form_libro_iva_ventas")
        form_libro_iva_ventas.resize(755, 425)
        form_libro_iva_ventas.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.tabWidget = QtWidgets.QTabWidget(form_libro_iva_ventas)
        self.tabWidget.setGeometry(QtCore.QRect(10, 70, 735, 336))
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lne_nombre = QtWidgets.QLineEdit(self.tab)
        self.lne_nombre.setMinimumSize(QtCore.QSize(250, 0))
        self.lne_nombre.setMaximumSize(QtCore.QSize(250, 16777215))
        self.lne_nombre.setObjectName("lne_nombre")
        self.horizontalLayout.addWidget(self.lne_nombre)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(95, 0))
        self.label_2.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lne_cuit_compras = QtWidgets.QLineEdit(self.tab)
        self.lne_cuit_compras.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit_compras.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit_compras.setText("")
        self.lne_cuit_compras.setObjectName("lne_cuit_compras")
        self.horizontalLayout.addWidget(self.lne_cuit_compras)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.cbx_ejercicio = QtWidgets.QComboBox(self.tab)
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(100, 0))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.horizontalLayout_2.addWidget(self.cbx_ejercicio)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.cbx_mes = QtWidgets.QComboBox(self.tab)
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
        self.horizontalLayout_2.addWidget(self.cbx_mes)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_buscar_compra = QtWidgets.QPushButton(self.tab)
        self.btn_buscar_compra.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_buscar_compra.setMaximumSize(QtCore.QSize(50, 25))
        self.btn_buscar_compra.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar_compra.setObjectName("btn_buscar_compra")
        self.verticalLayout_4.addWidget(self.btn_buscar_compra)
        self.btn_eliminar = QtWidgets.QPushButton(self.tab)
        self.btn_eliminar.setMinimumSize(QtCore.QSize(75, 25))
        self.btn_eliminar.setMaximumSize(QtCore.QSize(75, 25))
        self.btn_eliminar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.verticalLayout_4.addWidget(self.btn_eliminar)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_nuevo = QtWidgets.QPushButton(self.tab)
        self.btn_nuevo.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_nuevo.setObjectName("btn_nuevo")
        self.verticalLayout.addWidget(self.btn_nuevo)
        self.btn_modificar = QtWidgets.QPushButton(self.tab)
        self.btn_modificar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_modificar.setObjectName("btn_modificar")
        self.verticalLayout.addWidget(self.btn_modificar)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tw_ventas = QtWidgets.QTableWidget(self.tab)
        self.tw_ventas.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tw_ventas.setObjectName("tw_ventas")
        self.tw_ventas.setColumnCount(4)
        self.tw_ventas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ventas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ventas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ventas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_ventas.setHorizontalHeaderItem(3, item)
        self.tw_ventas.horizontalHeader().setDefaultSectionSize(175)
        self.gridLayout.addWidget(self.tw_ventas, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lne_resultado_uno = QtWidgets.QLineEdit(self.tab)
        self.lne_resultado_uno.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_resultado_uno.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_resultado_uno.setObjectName("lne_resultado_uno")
        self.horizontalLayout_4.addWidget(self.lne_resultado_uno)
        self.lne_resultado_dos = QtWidgets.QLineEdit(self.tab)
        self.lne_resultado_dos.setMinimumSize(QtCore.QSize(0, 25))
        self.lne_resultado_dos.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lne_resultado_dos.setObjectName("lne_resultado_dos")
        self.horizontalLayout_4.addWidget(self.lne_resultado_dos)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.layoutWidget = QtWidgets.QWidget(form_libro_iva_ventas)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 731, 52))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.lne_cuit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.verticalLayout_2.addWidget(self.lne_cuit)
        self.horizontalLayout_15.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_3.addWidget(self.label_16)
        self.lne_razon_social = QtWidgets.QLineEdit(self.layoutWidget)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_3.addWidget(self.lne_razon_social)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.btn_buscar = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_15.addWidget(self.btn_buscar)

        self.retranslateUi(form_libro_iva_ventas)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_libro_iva_ventas)
        form_libro_iva_ventas.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_libro_iva_ventas.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_libro_iva_ventas.setTabOrder(self.btn_buscar, self.tabWidget)
        form_libro_iva_ventas.setTabOrder(self.tabWidget, self.lne_nombre)
        form_libro_iva_ventas.setTabOrder(self.lne_nombre, self.lne_cuit_compras)
        form_libro_iva_ventas.setTabOrder(self.lne_cuit_compras, self.btn_buscar_compra)
        form_libro_iva_ventas.setTabOrder(self.btn_buscar_compra, self.cbx_ejercicio)
        form_libro_iva_ventas.setTabOrder(self.cbx_ejercicio, self.cbx_mes)
        form_libro_iva_ventas.setTabOrder(self.cbx_mes, self.btn_nuevo)
        form_libro_iva_ventas.setTabOrder(self.btn_nuevo, self.btn_eliminar)
        form_libro_iva_ventas.setTabOrder(self.btn_eliminar, self.btn_modificar)
        form_libro_iva_ventas.setTabOrder(self.btn_modificar, self.tw_ventas)
        form_libro_iva_ventas.setTabOrder(self.tw_ventas, self.lne_resultado_uno)
        form_libro_iva_ventas.setTabOrder(self.lne_resultado_uno, self.lne_resultado_dos)

    def retranslateUi(self, form_libro_iva_ventas):
        _translate = QtCore.QCoreApplication.translate
        form_libro_iva_ventas.setWindowTitle(_translate("form_libro_iva_ventas", "Libro IVA Ventas"))
        self.label.setText(_translate("form_libro_iva_ventas", "Nombre: "))
        self.label_2.setText(_translate("form_libro_iva_ventas", "CUIT / CUIL:"))
        self.label_5.setText(_translate("form_libro_iva_ventas", "Ejercicio:"))
        self.label_6.setText(_translate("form_libro_iva_ventas", "Mes: "))
        self.cbx_mes.setItemText(0, _translate("form_libro_iva_ventas", "Enero"))
        self.cbx_mes.setItemText(1, _translate("form_libro_iva_ventas", "Febrero"))
        self.cbx_mes.setItemText(2, _translate("form_libro_iva_ventas", "Marzo"))
        self.cbx_mes.setItemText(3, _translate("form_libro_iva_ventas", "Abril"))
        self.cbx_mes.setItemText(4, _translate("form_libro_iva_ventas", "Mayo"))
        self.cbx_mes.setItemText(5, _translate("form_libro_iva_ventas", "Junio"))
        self.cbx_mes.setItemText(6, _translate("form_libro_iva_ventas", "Julio"))
        self.cbx_mes.setItemText(7, _translate("form_libro_iva_ventas", "Agosto"))
        self.cbx_mes.setItemText(8, _translate("form_libro_iva_ventas", "Septiembre"))
        self.cbx_mes.setItemText(9, _translate("form_libro_iva_ventas", "Octubre"))
        self.cbx_mes.setItemText(10, _translate("form_libro_iva_ventas", "Noviembre"))
        self.cbx_mes.setItemText(11, _translate("form_libro_iva_ventas", "Diciembre"))
        self.btn_buscar_compra.setText(_translate("form_libro_iva_ventas", "Buscar"))
        self.btn_eliminar.setText(_translate("form_libro_iva_ventas", "Eliminar"))
        self.btn_nuevo.setText(_translate("form_libro_iva_ventas", "Nuevo"))
        self.btn_modificar.setText(_translate("form_libro_iva_ventas", "Actualizar"))
        item = self.tw_ventas.horizontalHeaderItem(0)
        item.setText(_translate("form_libro_iva_ventas", "Fecha"))
        item = self.tw_ventas.horizontalHeaderItem(1)
        item.setText(_translate("form_libro_iva_ventas", "N° Comprobante"))
        item = self.tw_ventas.horizontalHeaderItem(2)
        item.setText(_translate("form_libro_iva_ventas", "Proveedor"))
        item = self.tw_ventas.horizontalHeaderItem(3)
        item.setText(_translate("form_libro_iva_ventas", "Neto"))
        self.label_3.setText(_translate("form_libro_iva_ventas", "Resultado: "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_libro_iva_ventas", "Libro IVA Ventas"))
        self.label_15.setText(_translate("form_libro_iva_ventas", "CUIT / CUIL: "))
        self.label_16.setText(_translate("form_libro_iva_ventas", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_libro_iva_ventas", "Buscar"))
