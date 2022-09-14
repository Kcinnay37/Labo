# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Text = QLabel(self.centralwidget)
        self.Text.setObjectName(u"Text")
        self.Text.setGeometry(QRect(290, 70, 241, 41))
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Text.sizePolicy().hasHeightForWidth())
        self.Text.setSizePolicy(sizePolicy)
        self.Text.setLayoutDirection(Qt.LeftToRight)
        self.Text.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(290, 110, 241, 271))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Modulo = QPushButton(self.widget)
        self.Modulo.setObjectName(u"Modulo")
        sizePolicy.setHeightForWidth(self.Modulo.sizePolicy().hasHeightForWidth())
        self.Modulo.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Modulo, 0, 0, 1, 1)

        self.ResetCurr = QPushButton(self.widget)
        self.ResetCurr.setObjectName(u"ResetCurr")
        sizePolicy.setHeightForWidth(self.ResetCurr.sizePolicy().hasHeightForWidth())
        self.ResetCurr.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.ResetCurr, 0, 1, 1, 1)

        self.Reset = QPushButton(self.widget)
        self.Reset.setObjectName(u"Reset")
        sizePolicy.setHeightForWidth(self.Reset.sizePolicy().hasHeightForWidth())
        self.Reset.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Reset, 0, 2, 1, 1)

        self.Erase = QPushButton(self.widget)
        self.Erase.setObjectName(u"Erase")
        sizePolicy.setHeightForWidth(self.Erase.sizePolicy().hasHeightForWidth())
        self.Erase.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Erase, 0, 3, 1, 1)

        self.OneX = QPushButton(self.widget)
        self.OneX.setObjectName(u"OneX")
        sizePolicy.setHeightForWidth(self.OneX.sizePolicy().hasHeightForWidth())
        self.OneX.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.OneX, 1, 0, 1, 1)

        self.Square = QPushButton(self.widget)
        self.Square.setObjectName(u"Square")
        sizePolicy.setHeightForWidth(self.Square.sizePolicy().hasHeightForWidth())
        self.Square.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Square, 1, 1, 1, 1)

        self.SquareRoot = QPushButton(self.widget)
        self.SquareRoot.setObjectName(u"SquareRoot")
        sizePolicy.setHeightForWidth(self.SquareRoot.sizePolicy().hasHeightForWidth())
        self.SquareRoot.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.SquareRoot, 1, 2, 1, 1)

        self.Division = QPushButton(self.widget)
        self.Division.setObjectName(u"Division")
        sizePolicy.setHeightForWidth(self.Division.sizePolicy().hasHeightForWidth())
        self.Division.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Division, 1, 3, 1, 1)

        self.Num_7 = QPushButton(self.widget)
        self.Num_7.setObjectName(u"Num_7")
        sizePolicy.setHeightForWidth(self.Num_7.sizePolicy().hasHeightForWidth())
        self.Num_7.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_7, 2, 0, 1, 1)

        self.Num_8 = QPushButton(self.widget)
        self.Num_8.setObjectName(u"Num_8")
        sizePolicy.setHeightForWidth(self.Num_8.sizePolicy().hasHeightForWidth())
        self.Num_8.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_8, 2, 1, 1, 1)

        self.Num_9 = QPushButton(self.widget)
        self.Num_9.setObjectName(u"Num_9")
        sizePolicy.setHeightForWidth(self.Num_9.sizePolicy().hasHeightForWidth())
        self.Num_9.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_9, 2, 2, 1, 1)

        self.Multiplication = QPushButton(self.widget)
        self.Multiplication.setObjectName(u"Multiplication")
        sizePolicy.setHeightForWidth(self.Multiplication.sizePolicy().hasHeightForWidth())
        self.Multiplication.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Multiplication, 2, 3, 1, 1)

        self.Num_4 = QPushButton(self.widget)
        self.Num_4.setObjectName(u"Num_4")
        sizePolicy.setHeightForWidth(self.Num_4.sizePolicy().hasHeightForWidth())
        self.Num_4.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_4, 3, 0, 1, 1)

        self.Num_5 = QPushButton(self.widget)
        self.Num_5.setObjectName(u"Num_5")
        sizePolicy.setHeightForWidth(self.Num_5.sizePolicy().hasHeightForWidth())
        self.Num_5.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_5, 3, 1, 1, 1)

        self.Num_6 = QPushButton(self.widget)
        self.Num_6.setObjectName(u"Num_6")
        sizePolicy.setHeightForWidth(self.Num_6.sizePolicy().hasHeightForWidth())
        self.Num_6.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_6, 3, 2, 1, 1)

        self.Minus = QPushButton(self.widget)
        self.Minus.setObjectName(u"Minus")
        sizePolicy.setHeightForWidth(self.Minus.sizePolicy().hasHeightForWidth())
        self.Minus.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Minus, 3, 3, 1, 1)

        self.Num_1 = QPushButton(self.widget)
        self.Num_1.setObjectName(u"Num_1")
        sizePolicy.setHeightForWidth(self.Num_1.sizePolicy().hasHeightForWidth())
        self.Num_1.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_1, 4, 0, 1, 1)

        self.Num_2 = QPushButton(self.widget)
        self.Num_2.setObjectName(u"Num_2")
        sizePolicy.setHeightForWidth(self.Num_2.sizePolicy().hasHeightForWidth())
        self.Num_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_2, 4, 1, 1, 1)

        self.Num_3 = QPushButton(self.widget)
        self.Num_3.setObjectName(u"Num_3")
        sizePolicy.setHeightForWidth(self.Num_3.sizePolicy().hasHeightForWidth())
        self.Num_3.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_3, 4, 2, 1, 1)

        self.Plus = QPushButton(self.widget)
        self.Plus.setObjectName(u"Plus")
        sizePolicy.setHeightForWidth(self.Plus.sizePolicy().hasHeightForWidth())
        self.Plus.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Plus, 4, 3, 1, 1)

        self.PlusOrMinus = QPushButton(self.widget)
        self.PlusOrMinus.setObjectName(u"PlusOrMinus")
        sizePolicy.setHeightForWidth(self.PlusOrMinus.sizePolicy().hasHeightForWidth())
        self.PlusOrMinus.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.PlusOrMinus, 5, 0, 1, 1)

        self.Num_0 = QPushButton(self.widget)
        self.Num_0.setObjectName(u"Num_0")
        sizePolicy.setHeightForWidth(self.Num_0.sizePolicy().hasHeightForWidth())
        self.Num_0.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Num_0, 5, 1, 1, 1)

        self.Comma = QPushButton(self.widget)
        self.Comma.setObjectName(u"Comma")
        sizePolicy.setHeightForWidth(self.Comma.sizePolicy().hasHeightForWidth())
        self.Comma.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Comma, 5, 2, 1, 1)

        self.Equal = QPushButton(self.widget)
        self.Equal.setObjectName(u"Equal")
        sizePolicy.setHeightForWidth(self.Equal.sizePolicy().hasHeightForWidth())
        self.Equal.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.Equal, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Text.setText("")
        self.Modulo.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.ResetCurr.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.Reset.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.Erase.setText(QCoreApplication.translate("MainWindow", u"\u2190", None))
        self.OneX.setText(QCoreApplication.translate("MainWindow", u"1/x", None))
        self.Square.setText(QCoreApplication.translate("MainWindow", u"x2", None))
        self.SquareRoot.setText(QCoreApplication.translate("MainWindow", u"2\u221ax ", None))
        self.Division.setText(QCoreApplication.translate("MainWindow", u"\u00f7", None))
        self.Num_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.Num_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.Num_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.Multiplication.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.Num_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.Num_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.Num_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.Minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.Num_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.Num_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.Num_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.Plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.PlusOrMinus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.Num_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.Comma.setText(QCoreApplication.translate("MainWindow", u",", None))
        self.Equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

