# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 're_design.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 351)
        MainWindow.setMinimumSize(QSize(700, 0))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnInstruction = QPushButton(self.centralwidget)
        self.btnInstruction.setObjectName(u"btnInstruction")
        self.btnInstruction.setMinimumSize(QSize(105, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.btnInstruction.setFont(font1)

        self.verticalLayout.addWidget(self.btnInstruction)

        self.btnAllCommands = QPushButton(self.centralwidget)
        self.btnAllCommands.setObjectName(u"btnAllCommands")
        self.btnAllCommands.setMinimumSize(QSize(105, 30))
        self.btnAllCommands.setFont(font1)
        self.btnAllCommands.setAutoRepeat(False)
        self.btnAllCommands.setAutoDefault(False)
        self.btnAllCommands.setFlat(False)

        self.verticalLayout.addWidget(self.btnAllCommands, 0, Qt.AlignTop)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabExternal = QWidget()
        self.tabExternal.setObjectName(u"tabExternal")
        self.verticalLayout_3 = QVBoxLayout(self.tabExternal)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineNamesAssist = QLineEdit(self.tabExternal)
        self.lineNamesAssist.setObjectName(u"lineNamesAssist")
        self.lineNamesAssist.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.lineNamesAssist.setFont(font2)

        self.verticalLayout_2.addWidget(self.lineNamesAssist)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, -1)
        self.label_2 = QLabel(self.tabExternal)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(16777215, 50))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cmbVoice = QComboBox(self.tabExternal)
        self.cmbVoice.addItem("")
        self.cmbVoice.addItem("")
        self.cmbVoice.addItem("")
        self.cmbVoice.addItem("")
        self.cmbVoice.addItem("")
        self.cmbVoice.setObjectName(u"cmbVoice")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cmbVoice.sizePolicy().hasHeightForWidth())
        self.cmbVoice.setSizePolicy(sizePolicy1)
        self.cmbVoice.setFont(font2)
        self.cmbVoice.setStyleSheet(u"")
        self.cmbVoice.setFrame(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cmbVoice)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.btnSaveExt = QPushButton(self.tabExternal)
        self.btnSaveExt.setObjectName(u"btnSaveExt")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.btnSaveExt.setFont(font3)

        self.verticalLayout_2.addWidget(self.btnSaveExt)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tabExternal, "")
        self.tabAddCommand = QWidget()
        self.tabAddCommand.setObjectName(u"tabAddCommand")
        self.verticalLayout_7 = QVBoxLayout(self.tabAddCommand)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineFile = QLineEdit(self.tabAddCommand)
        self.lineFile.setObjectName(u"lineFile")
        self.lineFile.setFont(font2)

        self.gridLayout.addWidget(self.lineFile, 2, 1, 1, 1)

        self.btnAddHotkey = QPushButton(self.tabAddCommand)
        self.btnAddHotkey.setObjectName(u"btnAddHotkey")
        font4 = QFont()
        font4.setPointSize(10)
        self.btnAddHotkey.setFont(font4)

        self.gridLayout.addWidget(self.btnAddHotkey, 3, 2, 1, 1)

        self.cmbAction = QComboBox(self.tabAddCommand)
        self.cmbAction.addItem("")
        self.cmbAction.addItem("")
        self.cmbAction.addItem("")
        self.cmbAction.addItem("")
        self.cmbAction.setObjectName(u"cmbAction")
        self.cmbAction.setFont(font2)

        self.gridLayout.addWidget(self.cmbAction, 0, 1, 1, 2)

        self.lblFile = QLabel(self.tabAddCommand)
        self.lblFile.setObjectName(u"lblFile")
        self.lblFile.setMinimumSize(QSize(0, 30))
        self.lblFile.setFont(font1)

        self.gridLayout.addWidget(self.lblFile, 2, 0, 1, 1)

        self.lineHotkey = QLineEdit(self.tabAddCommand)
        self.lineHotkey.setObjectName(u"lineHotkey")
        self.lineHotkey.setFont(font2)

        self.gridLayout.addWidget(self.lineHotkey, 3, 1, 1, 1)

        self.label_5 = QLabel(self.tabAddCommand)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 30))
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_4 = QLabel(self.tabAddCommand)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(self.tabAddCommand)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 30))
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.lineCommand = QLineEdit(self.tabAddCommand)
        self.lineCommand.setObjectName(u"lineCommand")
        self.lineCommand.setFont(font2)

        self.gridLayout.addWidget(self.lineCommand, 4, 1, 1, 2)

        self.lblHotkey = QLabel(self.tabAddCommand)
        self.lblHotkey.setObjectName(u"lblHotkey")
        self.lblHotkey.setMinimumSize(QSize(0, 30))
        self.lblHotkey.setFont(font1)

        self.gridLayout.addWidget(self.lblHotkey, 3, 0, 1, 1)

        self.lineAnswer = QLineEdit(self.tabAddCommand)
        self.lineAnswer.setObjectName(u"lineAnswer")
        self.lineAnswer.setFont(font2)

        self.gridLayout.addWidget(self.lineAnswer, 5, 1, 1, 2)

        self.btnChooseFile = QPushButton(self.tabAddCommand)
        self.btnChooseFile.setObjectName(u"btnChooseFile")
        self.btnChooseFile.setFont(font4)

        self.gridLayout.addWidget(self.btnChooseFile, 2, 2, 1, 1)

        self.label_8 = QLabel(self.tabAddCommand)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)

        self.lineNameCmnd = QLineEdit(self.tabAddCommand)
        self.lineNameCmnd.setObjectName(u"lineNameCmnd")
        self.lineNameCmnd.setFont(font2)

        self.gridLayout.addWidget(self.lineNameCmnd, 1, 1, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btnAddCommand = QPushButton(self.tabAddCommand)
        self.btnAddCommand.setObjectName(u"btnAddCommand")
        self.btnAddCommand.setFont(font3)

        self.horizontalLayout_4.addWidget(self.btnAddCommand, 0, Qt.AlignBottom)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)


        self.verticalLayout_7.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tabAddCommand, "")
        self.tabTokens = QWidget()
        self.tabTokens.setObjectName(u"tabTokens")
        self.verticalLayout_5 = QVBoxLayout(self.tabTokens)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(self.tabTokens)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setFont(font1)

        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineWeatherTok = QLineEdit(self.tabTokens)
        self.lineWeatherTok.setObjectName(u"lineWeatherTok")
        self.lineWeatherTok.setFont(font2)

        self.gridLayout_2.addWidget(self.lineWeatherTok, 0, 1, 1, 1)

        self.linetCity = QLineEdit(self.tabTokens)
        self.linetCity.setObjectName(u"linetCity")
        self.linetCity.setFont(font2)

        self.gridLayout_2.addWidget(self.linetCity, 1, 1, 1, 1)

        self.label_9 = QLabel(self.tabTokens)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_7 = QLabel(self.tabTokens)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setFont(font1)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.lineGPTTok = QLineEdit(self.tabTokens)
        self.lineGPTTok.setObjectName(u"lineGPTTok")
        self.lineGPTTok.setFont(font2)

        self.gridLayout_2.addWidget(self.lineGPTTok, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.btnSaveTok = QPushButton(self.tabTokens)
        self.btnSaveTok.setObjectName(u"btnSaveTok")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.btnSaveTok.setFont(font5)

        self.horizontalLayout_6.addWidget(self.btnSaveTok, 0, Qt.AlignBottom)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tabTokens, "")

        self.horizontalLayout_11.addWidget(self.tabWidget)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.btnAllCommands.setDefault(False)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Windows \u0410\u0441\u0441\u0438\u0441\u0442\u0435\u043d\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0444\u0443\u043d\u043a\u0446\u0438\u043e\u043d\u0430\u043b\u0430 \u043f\u043e\u043c\u043e\u0449\u043d\u0438\u043a\u0430", None))
        self.btnInstruction.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.btnAllCommands.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.lineNamesAssist.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0441", None))
        self.cmbVoice.setItemText(0, QCoreApplication.translate("MainWindow", u"aidar", None))
        self.cmbVoice.setItemText(1, QCoreApplication.translate("MainWindow", u"baya", None))
        self.cmbVoice.setItemText(2, QCoreApplication.translate("MainWindow", u"kseniya", None))
        self.cmbVoice.setItemText(3, QCoreApplication.translate("MainWindow", u"xenia", None))
        self.cmbVoice.setItemText(4, QCoreApplication.translate("MainWindow", u"eugene", None))

        self.btnSaveExt.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabExternal), QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0448\u043d\u0438\u0435 \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btnAddHotkey.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043b\u0430\u0432\u0438\u0448\u0443", None))
        self.cmbAction.setItemText(0, QCoreApplication.translate("MainWindow", u"open_url", None))
        self.cmbAction.setItemText(1, QCoreApplication.translate("MainWindow", u"open_file", None))
        self.cmbAction.setItemText(2, QCoreApplication.translate("MainWindow", u"hotkey", None))
        self.cmbAction.setItemText(3, QCoreApplication.translate("MainWindow", u"passive", None))

        self.lblFile.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043b\u043e\u0441. \u043a\u043e\u043c\u0430\u043d\u0434\u0430", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435", None))
        self.lineCommand.setText("")
        self.lblHotkey.setText(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u0442\u043a\u0435\u0439", None))
        self.btnChooseFile.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.btnAddCommand.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAddCommand), QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u043e\u043c\u0430\u043d\u0434\u0443", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.lineWeatherTok.setText("")
        self.linetCity.setText("")
        self.lineNameCmnd.setText('')
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0440\u043e\u0434", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"OpenGPT", None))
        self.lineGPTTok.setText("")
        self.btnSaveTok.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTokens), QCoreApplication.translate("MainWindow", u"\u0422\u043e\u043a\u0435\u043d\u044b", None))
    # retranslateUi

