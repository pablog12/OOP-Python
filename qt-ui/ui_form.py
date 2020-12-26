# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainUI(object):
    def setupUi(self, MainUI):
        if not MainUI.objectName():
            MainUI.setObjectName(u"MainUI")
        MainUI.resize(258, 230)
        self.centralwidget = QWidget(MainUI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(255)

        self.gridLayout_2.addWidget(self.spinBox, 1, 0, 1, 1)

        self.verticalSlider = QSlider(self.centralwidget)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setMaximum(255)
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.spinBox_3 = QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMaximum(255)

        self.gridLayout_3.addWidget(self.spinBox_3, 1, 0, 1, 1)

        self.verticalSlider_3 = QSlider(self.centralwidget)
        self.verticalSlider_3.setObjectName(u"verticalSlider_3")
        self.verticalSlider_3.setMaximum(255)
        self.verticalSlider_3.setOrientation(Qt.Vertical)

        self.gridLayout_3.addWidget(self.verticalSlider_3, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(255)

        self.gridLayout_4.addWidget(self.spinBox_2, 1, 0, 1, 1)

        self.verticalSlider_2 = QSlider(self.centralwidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setMaximum(255)
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.gridLayout_4.addWidget(self.verticalSlider_2, 2, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_4)

        MainUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 258, 21))
        MainUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainUI)
        self.statusbar.setObjectName(u"statusbar")
        MainUI.setStatusBar(self.statusbar)

        self.retranslateUi(MainUI)
        self.verticalSlider.valueChanged.connect(self.spinBox.setValue)
        self.verticalSlider_3.valueChanged.connect(self.spinBox_3.setValue)
        self.verticalSlider_2.valueChanged.connect(self.spinBox_2.setValue)
        self.spinBox.valueChanged.connect(self.verticalSlider.setValue)
        self.spinBox_3.valueChanged.connect(self.verticalSlider_3.setValue)
        self.spinBox_2.valueChanged.connect(self.verticalSlider_2.setValue)

        QMetaObject.connectSlotsByName(MainUI)
    # setupUi

    def retranslateUi(self, MainUI):
        MainUI.setWindowTitle(QCoreApplication.translate("MainUI", u"MainUI", None))
        self.label.setText(QCoreApplication.translate("MainUI", u"RED", None))
        self.label_3.setText(QCoreApplication.translate("MainUI", u"BLUE", None))
        self.label_2.setText(QCoreApplication.translate("MainUI", u"GREEN", None))
    # retranslateUi

