# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_libro_iva_ventas_nuevo.ui'
#
# Created: Wed Feb 14 21:25:35 2018
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_libro_iva_ventas_nuevo(object):
    def setupUi(self, form_libro_iva_ventas_nuevo):
        form_libro_iva_ventas_nuevo.setObjectName("form_libro_iva_ventas_nuevo")
        form_libro_iva_ventas_nuevo.resize(663, 498)
        form_libro_iva_ventas_nuevo.setStyleSheet("color: rgb(3, 3, 3);\n"
"background-color: rgb(44, 43, 58);\n"
"font: 10pt \"Liberation Sans\";\n"
"color: rgb(252, 252, 252);\n"
"selection-background-color: rgb(155, 155, 185);")
        self.gridLayout_2 = QtWidgets.QGridLayout(form_libro_iva_ventas_nuevo)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_19 = QtWidgets.QLabel(form_libro_iva_ventas_nuevo)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.label_19)
        self.lne_cuit = QtWidgets.QLineEdit(form_libro_iva_ventas_nuevo)
        self.lne_cuit.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_cuit.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_cuit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_cuit.setText("")
        self.lne_cuit.setObjectName("lne_cuit")
        self.verticalLayout_5.addWidget(self.lne_cuit)
        self.horizontalLayout_20.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_20 = QtWidgets.QLabel(form_libro_iva_ventas_nuevo)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.lne_razon_social = QtWidgets.QLineEdit(form_libro_iva_ventas_nuevo)
        self.lne_razon_social.setMinimumSize(QtCore.QSize(350, 0))
        self.lne_razon_social.setMaximumSize(QtCore.QSize(350, 16777215))
        self.lne_razon_social.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lne_razon_social.setObjectName("lne_razon_social")
        self.verticalLayout_6.addWidget(self.lne_razon_social)
        self.horizontalLayout_20.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem)
        self.btn_buscar = QtWidgets.QPushButton(form_libro_iva_ventas_nuevo)
        self.btn_buscar.setMinimumSize(QtCore.QSize(0, 25))
        self.btn_buscar.setMaximumSize(QtCore.QSize(16777215, 25))
        self.btn_buscar.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_buscar.setObjectName("btn_buscar")
        self.horizontalLayout_20.addWidget(self.btn_buscar)
        self.gridLayout_2.addLayout(self.horizontalLayout_20, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(form_libro_iva_ventas_nuevo)
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
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.dte_fec_nuevo = QtWidgets.QDateEdit(self.tab)
        self.dte_fec_nuevo.setMinimumSize(QtCore.QSize(110, 25))
        self.dte_fec_nuevo.setMaximumSize(QtCore.QSize(110, 25))
        self.dte_fec_nuevo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.dte_fec_nuevo.setObjectName("dte_fec_nuevo")
        self.horizontalLayout.addWidget(self.dte_fec_nuevo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.lne_comprbante = QtWidgets.QLineEdit(self.tab)
        self.lne_comprbante.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_comprbante.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_comprbante.setText("")
        self.lne_comprbante.setObjectName("lne_comprbante")
        self.horizontalLayout_2.addWidget(self.lne_comprbante)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.cbx_tipo = QtWidgets.QComboBox(self.tab)
        self.cbx_tipo.setMinimumSize(QtCore.QSize(50, 25))
        self.cbx_tipo.setMaximumSize(QtCore.QSize(50, 25))
        self.cbx_tipo.setObjectName("cbx_tipo")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.cbx_tipo.addItem("")
        self.horizontalLayout_3.addWidget(self.cbx_tipo)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMinimumSize(QtCore.QSize(95, 0))
        self.label_2.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.cbx_proveedor = QtWidgets.QComboBox(self.tab)
        self.cbx_proveedor.setObjectName("cbx_proveedor")
        self.horizontalLayout_4.addWidget(self.cbx_proveedor)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_21.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.cbx_ejercicio = QtWidgets.QComboBox(self.tab)
        self.cbx_ejercicio.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_ejercicio.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_ejercicio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_ejercicio.setObjectName("cbx_ejercicio")
        self.horizontalLayout_8.addWidget(self.cbx_ejercicio)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.cbx_asiento = QtWidgets.QComboBox(self.tab)
        self.cbx_asiento.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_asiento.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_asiento.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_asiento.setObjectName("cbx_asiento")
        self.horizontalLayout_5.addWidget(self.cbx_asiento)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.cbx_cuenta = QtWidgets.QComboBox(self.tab)
        self.cbx_cuenta.setMinimumSize(QtCore.QSize(110, 0))
        self.cbx_cuenta.setMaximumSize(QtCore.QSize(110, 16777215))
        self.cbx_cuenta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cbx_cuenta.setObjectName("cbx_cuenta")
        self.horizontalLayout_6.addWidget(self.cbx_cuenta)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setMinimumSize(QtCore.QSize(95, 0))
        self.label_7.setMaximumSize(QtCore.QSize(95, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.lne_ref = QtWidgets.QLineEdit(self.tab)
        self.lne_ref.setMinimumSize(QtCore.QSize(110, 0))
        self.lne_ref.setMaximumSize(QtCore.QSize(110, 16777215))
        self.lne_ref.setText("")
        self.lne_ref.setObjectName("lne_ref")
        self.horizontalLayout_7.addWidget(self.lne_ref)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_21.addLayout(self.verticalLayout_2)
        self.btn_crear = QtWidgets.QPushButton(self.tab)
        self.btn_crear.setMinimumSize(QtCore.QSize(100, 25))
        self.btn_crear.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_crear.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.btn_crear.setObjectName("btn_crear")
        self.horizontalLayout_21.addWidget(self.btn_crear)
        self.gridLayout.addLayout(self.horizontalLayout_21, 0, 0, 1, 1)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.lne_neto = QtWidgets.QLineEdit(self.tab)
        self.lne_neto.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_neto.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_neto.setText("")
        self.lne_neto.setObjectName("lne_neto")
        self.horizontalLayout_9.addWidget(self.lne_neto)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.lne_10_5 = QtWidgets.QLineEdit(self.tab)
        self.lne_10_5.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_10_5.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_10_5.setText("")
        self.lne_10_5.setObjectName("lne_10_5")
        self.horizontalLayout_10.addWidget(self.lne_10_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.lne_21 = QtWidgets.QLineEdit(self.tab)
        self.lne_21.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_21.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_21.setText("")
        self.lne_21.setObjectName("lne_21")
        self.horizontalLayout_11.addWidget(self.lne_21)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.lne_monotrib = QtWidgets.QLineEdit(self.tab)
        self.lne_monotrib.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_monotrib.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_monotrib.setText("")
        self.lne_monotrib.setObjectName("lne_monotrib")
        self.horizontalLayout_12.addWidget(self.lne_monotrib)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_13.addWidget(self.label_15)
        self.lne_no_grav = QtWidgets.QLineEdit(self.tab)
        self.lne_no_grav.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_no_grav.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_no_grav.setText("")
        self.lne_no_grav.setObjectName("lne_no_grav")
        self.horizontalLayout_13.addWidget(self.lne_no_grav)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_16 = QtWidgets.QLabel(self.tab)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_14.addWidget(self.label_16)
        self.lne_iibb = QtWidgets.QLineEdit(self.tab)
        self.lne_iibb.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_iibb.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_iibb.setText("")
        self.lne_iibb.setObjectName("lne_iibb")
        self.horizontalLayout_14.addWidget(self.lne_iibb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_22.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.lne_27 = QtWidgets.QLineEdit(self.tab)
        self.lne_27.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_27.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_27.setText("")
        self.lne_27.setObjectName("lne_27")
        self.horizontalLayout_15.addWidget(self.lne_27)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13)
        self.lne_iva = QtWidgets.QLineEdit(self.tab)
        self.lne_iva.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_iva.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_iva.setText("")
        self.lne_iva.setObjectName("lne_iva")
        self.horizontalLayout_16.addWidget(self.lne_iva)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.lne_otros = QtWidgets.QLineEdit(self.tab)
        self.lne_otros.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_otros.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_otros.setText("")
        self.lne_otros.setObjectName("lne_otros")
        self.horizontalLayout_17.addWidget(self.lne_otros)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_17 = QtWidgets.QLabel(self.tab)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_18.addWidget(self.label_17)
        self.lne_percepcion_iva = QtWidgets.QLineEdit(self.tab)
        self.lne_percepcion_iva.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_percepcion_iva.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_percepcion_iva.setText("")
        self.lne_percepcion_iva.setObjectName("lne_percepcion_iva")
        self.horizontalLayout_18.addWidget(self.lne_percepcion_iva)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_19.addWidget(self.label_18)
        self.lne_resultado = QtWidgets.QLineEdit(self.tab)
        self.lne_resultado.setMinimumSize(QtCore.QSize(110, 25))
        self.lne_resultado.setMaximumSize(QtCore.QSize(110, 25))
        self.lne_resultado.setText("")
        self.lne_resultado.setObjectName("lne_resultado")
        self.horizontalLayout_19.addWidget(self.lne_resultado)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_22.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(form_libro_iva_ventas_nuevo)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(100, 25))
        self.pushButton_2.setStyleSheet("background-color: rgb(64, 63, 78);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 2, 0, 1, 1, QtCore.Qt.AlignRight)

        self.retranslateUi(form_libro_iva_ventas_nuevo)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form_libro_iva_ventas_nuevo)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_cuit, self.lne_razon_social)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_razon_social, self.btn_buscar)
        form_libro_iva_ventas_nuevo.setTabOrder(self.btn_buscar, self.tabWidget)
        form_libro_iva_ventas_nuevo.setTabOrder(self.tabWidget, self.dte_fec_nuevo)
        form_libro_iva_ventas_nuevo.setTabOrder(self.dte_fec_nuevo, self.cbx_ejercicio)
        form_libro_iva_ventas_nuevo.setTabOrder(self.cbx_ejercicio, self.lne_comprbante)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_comprbante, self.cbx_asiento)
        form_libro_iva_ventas_nuevo.setTabOrder(self.cbx_asiento, self.cbx_tipo)
        form_libro_iva_ventas_nuevo.setTabOrder(self.cbx_tipo, self.cbx_cuenta)
        form_libro_iva_ventas_nuevo.setTabOrder(self.cbx_cuenta, self.cbx_proveedor)
        form_libro_iva_ventas_nuevo.setTabOrder(self.cbx_proveedor, self.lne_ref)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_ref, self.btn_crear)
        form_libro_iva_ventas_nuevo.setTabOrder(self.btn_crear, self.lne_neto)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_neto, self.lne_10_5)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_10_5, self.lne_21)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_21, self.lne_monotrib)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_monotrib, self.lne_no_grav)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_no_grav, self.lne_iibb)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_iibb, self.lne_27)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_27, self.lne_iva)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_iva, self.lne_otros)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_otros, self.lne_percepcion_iva)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_percepcion_iva, self.lne_resultado)
        form_libro_iva_ventas_nuevo.setTabOrder(self.lne_resultado, self.pushButton_2)

    def retranslateUi(self, form_libro_iva_ventas_nuevo):
        _translate = QtCore.QCoreApplication.translate
        form_libro_iva_ventas_nuevo.setWindowTitle(_translate("form_libro_iva_ventas_nuevo", "Libro IVA Ventas Nuevo"))
        self.label_19.setText(_translate("form_libro_iva_ventas_nuevo", "CUIT / CUIL: "))
        self.label_20.setText(_translate("form_libro_iva_ventas_nuevo", "Razón Social: "))
        self.btn_buscar.setText(_translate("form_libro_iva_ventas_nuevo", "Buscar"))
        self.label.setText(_translate("form_libro_iva_ventas_nuevo", "Fecha: "))
        self.dte_fec_nuevo.setDisplayFormat(_translate("form_libro_iva_ventas_nuevo", "dd/MM/yyyy"))
        self.label_5.setText(_translate("form_libro_iva_ventas_nuevo", "N° Comprobante: "))
        self.label_6.setText(_translate("form_libro_iva_ventas_nuevo", "Tipo :"))
        self.cbx_tipo.setItemText(0, _translate("form_libro_iva_ventas_nuevo", "FA"))
        self.cbx_tipo.setItemText(1, _translate("form_libro_iva_ventas_nuevo", "TFA"))
        self.cbx_tipo.setItemText(2, _translate("form_libro_iva_ventas_nuevo", "FB"))
        self.cbx_tipo.setItemText(3, _translate("form_libro_iva_ventas_nuevo", "TFB "))
        self.cbx_tipo.setItemText(4, _translate("form_libro_iva_ventas_nuevo", "FC "))
        self.cbx_tipo.setItemText(5, _translate("form_libro_iva_ventas_nuevo", "NDA "))
        self.cbx_tipo.setItemText(6, _translate("form_libro_iva_ventas_nuevo", "NDB "))
        self.cbx_tipo.setItemText(7, _translate("form_libro_iva_ventas_nuevo", "NDC"))
        self.cbx_tipo.setItemText(8, _translate("form_libro_iva_ventas_nuevo", "NCA "))
        self.cbx_tipo.setItemText(9, _translate("form_libro_iva_ventas_nuevo", "NCC "))
        self.cbx_tipo.setItemText(10, _translate("form_libro_iva_ventas_nuevo", "NCB"))
        self.label_2.setText(_translate("form_libro_iva_ventas_nuevo", "Proveedor: "))
        self.label_21.setText(_translate("form_libro_iva_ventas_nuevo", "Ejercicio:"))
        self.label_3.setText(_translate("form_libro_iva_ventas_nuevo", "Asiento: "))
        self.label_4.setText(_translate("form_libro_iva_ventas_nuevo", "Cuenta: "))
        self.label_7.setText(_translate("form_libro_iva_ventas_nuevo", "Referencia: "))
        self.btn_crear.setText(_translate("form_libro_iva_ventas_nuevo", "Crear Asiento"))
        self.label_8.setText(_translate("form_libro_iva_ventas_nuevo", "Neto:"))
        self.label_9.setText(_translate("form_libro_iva_ventas_nuevo", "10,5 %"))
        self.label_10.setText(_translate("form_libro_iva_ventas_nuevo", "21 %"))
        self.label_12.setText(_translate("form_libro_iva_ventas_nuevo", "Monotributo:"))
        self.label_15.setText(_translate("form_libro_iva_ventas_nuevo", "No Gravado / Exento"))
        self.label_16.setText(_translate("form_libro_iva_ventas_nuevo", "Percepción / IIBB"))
        self.label_11.setText(_translate("form_libro_iva_ventas_nuevo", "27% "))
        self.label_13.setText(_translate("form_libro_iva_ventas_nuevo", "IVA"))
        self.label_14.setText(_translate("form_libro_iva_ventas_nuevo", "Otros Impuestos "))
        self.label_17.setText(_translate("form_libro_iva_ventas_nuevo", "Percepción IVA"))
        self.label_18.setText(_translate("form_libro_iva_ventas_nuevo", "Resultado "))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("form_libro_iva_ventas_nuevo", "Libro IVA Ventas - Nuevo Registro"))
        self.pushButton_2.setText(_translate("form_libro_iva_ventas_nuevo", "Guardar"))

