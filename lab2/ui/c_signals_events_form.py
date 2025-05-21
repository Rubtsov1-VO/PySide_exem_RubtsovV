# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'c_signals_events_form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(837, 578)
        Form.setMinimumSize(QSize(700, 450))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.LeftUp = QPushButton(self.groupBox_2)
        self.LeftUp.setObjectName(u"LeftUp")
        self.LeftUp.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_6.addWidget(self.LeftUp)

        self.RightUp = QPushButton(self.groupBox_2)
        self.RightUp.setObjectName(u"RightUp")
        self.RightUp.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_6.addWidget(self.RightUp)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.pushButtonCenter = QPushButton(self.groupBox_2)
        self.pushButtonCenter.setObjectName(u"pushButtonCenter")
        self.pushButtonCenter.setMinimumSize(QSize(0, 50))

        self.verticalLayout_3.addWidget(self.pushButtonCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LeftDown = QPushButton(self.groupBox_2)
        self.LeftDown.setObjectName(u"LeftDown")
        self.LeftDown.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.LeftDown)

        self.RightDown = QPushButton(self.groupBox_2)
        self.RightDown.setObjectName(u"RightDown")
        self.RightDown.setMinimumSize(QSize(0, 50))

        self.horizontalLayout_5.addWidget(self.RightDown)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelX = QLabel(self.groupBox_3)
        self.labelX.setObjectName(u"labelX")

        self.horizontalLayout_3.addWidget(self.labelX)

        self.spinBoxX = QSpinBox(self.groupBox_3)
        self.spinBoxX.setObjectName(u"spinBoxX")

        self.horizontalLayout_3.addWidget(self.spinBoxX)

        self.labelY = QLabel(self.groupBox_3)
        self.labelY.setObjectName(u"labelY")

        self.horizontalLayout_3.addWidget(self.labelY)

        self.spinBoxY = QSpinBox(self.groupBox_3)
        self.spinBoxY.setObjectName(u"spinBoxY")

        self.horizontalLayout_3.addWidget(self.spinBoxY)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.Move = QPushButton(self.groupBox_3)
        self.Move.setObjectName(u"Move")

        self.verticalLayout_2.addWidget(self.Move)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.TextUp = QPlainTextEdit(self.groupBox)
        self.TextUp.setObjectName(u"TextUp")
        self.TextUp.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.TextUp)


        self.verticalLayout.addWidget(self.groupBox)

        self.GetdatafromWindow = QPushButton(Form)
        self.GetdatafromWindow.setObjectName(u"GetdatafromWindow")

        self.verticalLayout.addWidget(self.GetdatafromWindow)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u043e\u043a\u043d\u0430:", None))
        self.LeftUp.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.RightUp.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u0412\u0435\u0440\u0445", None))
        self.pushButtonCenter.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.LeftDown.setText(QCoreApplication.translate("Form", u"\u041b\u0435\u0432\u043e/\u041d\u0438\u0437", None))
        self.RightDown.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u0430\u0432\u043e/\u041d\u0438\u0437", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c \u0432 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b:", None))
        self.labelX.setText(QCoreApplication.translate("Form", u"X", None))
        self.labelY.setText(QCoreApplication.translate("Form", u"Y", None))
        self.Move.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0441\u0442\u0438\u0442\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041b\u043e\u0433:", None))
        self.GetdatafromWindow.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u043e\u043a\u043d\u0430", None))
    # retranslateUi

