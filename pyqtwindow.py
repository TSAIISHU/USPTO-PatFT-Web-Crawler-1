# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ASUS\Documents\1st\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1050, 665)
        MainWindow.setMinimumSize(QtCore.QSize(1050, 665))
        MainWindow.setMaximumSize(QtCore.QSize(1050, 665))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 22, 1031, 581))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 448, 441, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.PDFbws = QtWidgets.QToolButton(self.groupBox_8)
        self.PDFbws.setEnabled(True)
        self.PDFbws.setGeometry(QtCore.QRect(390, 58, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDFbws.setFont(font)
        self.PDFbws.setObjectName("PDFbws")
        self.PDFloc = QtWidgets.QLineEdit(self.groupBox_8)
        self.PDFloc.setEnabled(True)
        self.PDFloc.setGeometry(QtCore.QRect(10, 58, 371, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDFloc.setFont(font)
        self.PDFloc.setText("")
        self.PDFloc.setObjectName("PDFloc")
        self.label_19 = QtWidgets.QLabel(self.groupBox_8)
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QtCore.QRect(10, 37, 421, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.PDFfull = QtWidgets.QCheckBox(self.groupBox_8)
        self.PDFfull.setGeometry(QtCore.QRect(11, 18, 119, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDFfull.setFont(font)
        self.PDFfull.setObjectName("PDFfull")
        self.PDFdraw = QtWidgets.QCheckBox(self.groupBox_8)
        self.PDFdraw.setEnabled(True)
        self.PDFdraw.setGeometry(QtCore.QRect(210, 18, 211, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDFdraw.setFont(font)
        self.PDFdraw.setObjectName("PDFdraw")
        self.groupBox_10 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(460, 448, 561, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setObjectName("groupBox_10")
        self.EXPORT = QtWidgets.QPushButton(self.groupBox_10)
        self.EXPORT.setGeometry(QtCore.QRect(376, 53, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.EXPORT.setFont(font)
        self.EXPORT.setObjectName("EXPORT")
        self.FILTER = QtWidgets.QPushButton(self.groupBox_10)
        self.FILTER.setGeometry(QtCore.QRect(198, 19, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.FILTER.setFont(font)
        self.FILTER.setObjectName("FILTER")
        self.PDFD = QtWidgets.QPushButton(self.groupBox_10)
        self.PDFD.setGeometry(QtCore.QRect(19, 53, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDFD.setFont(font)
        self.PDFD.setObjectName("PDFD")
        self.INFO = QtWidgets.QPushButton(self.groupBox_10)
        self.INFO.setGeometry(QtCore.QRect(376, 19, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.INFO.setFont(font)
        self.INFO.setObjectName("INFO")
        self.IMPORT = QtWidgets.QPushButton(self.groupBox_10)
        self.IMPORT.setGeometry(QtCore.QRect(19, 19, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IMPORT.setFont(font)
        self.IMPORT.setObjectName("IMPORT")
        self.STOPLOOP = QtWidgets.QPushButton(self.groupBox_10)
        self.STOPLOOP.setGeometry(QtCore.QRect(198, 53, 170, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.STOPLOOP.setFont(font)
        self.STOPLOOP.setObjectName("STOPLOOP")
        self.groupBox_11 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 6, 441, 97))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setObjectName("groupBox_11")
        self.PNloc = QtWidgets.QLineEdit(self.groupBox_11)
        self.PNloc.setGeometry(QtCore.QRect(10, 65, 381, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PNloc.setFont(font)
        self.PNloc.setText("")
        self.PNloc.setObjectName("PNloc")
        self.PNbws = QtWidgets.QToolButton(self.groupBox_11)
        self.PNbws.setGeometry(QtCore.QRect(400, 65, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PNbws.setFont(font)
        self.PNbws.setObjectName("PNbws")
        self.Querybox = QtWidgets.QPlainTextEdit(self.groupBox_11)
        self.Querybox.setGeometry(QtCore.QRect(10, 46, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Querybox.setFont(font)
        self.Querybox.setObjectName("Querybox")
        self.label_7 = QtWidgets.QLabel(self.groupBox_11)
        self.label_7.setGeometry(QtCore.QRect(10, 35, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.PNbt = QtWidgets.QRadioButton(self.groupBox_11)
        self.PNbt.setGeometry(QtCore.QRect(11, 19, 121, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.PNbt.setFont(font)
        self.PNbt.setObjectName("PNbt")
        self.Querybt = QtWidgets.QRadioButton(self.groupBox_11)
        self.Querybt.setEnabled(True)
        self.Querybt.setGeometry(QtCore.QRect(120, 19, 67, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.Querybt.setFont(font)
        self.Querybt.setWhatsThis("")
        self.Querybt.setObjectName("Querybt")
        self.DB = QtWidgets.QComboBox(self.groupBox_11)
        self.DB.setGeometry(QtCore.QRect(220, 18, 211, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.DB.setFont(font)
        self.DB.setObjectName("DB")
        self.DB.addItem("")
        self.DB.addItem("")
        self.Querybox.raise_()
        self.label_7.raise_()
        self.PNloc.raise_()
        self.PNbws.raise_()
        self.PNbt.raise_()
        self.Querybt.raise_()
        self.DB.raise_()
        self.groupBox_12 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_12.setGeometry(QtCore.QRect(10, 106, 441, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_12.setFont(font)
        self.groupBox_12.setObjectName("groupBox_12")
        self.groupBox_14 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 20, 421, 51))
        self.groupBox_14.setObjectName("groupBox_14")
        self.all = QtWidgets.QCheckBox(self.groupBox_14)
        self.all.setEnabled(True)
        self.all.setGeometry(QtCore.QRect(16, 22, 45, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.all.setFont(font)
        self.all.setObjectName("all")
        self.pp = QtWidgets.QCheckBox(self.groupBox_14)
        self.pp.setEnabled(True)
        self.pp.setGeometry(QtCore.QRect(244, 21, 56, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.pp.setFont(font)
        self.pp.setObjectName("pp")
        self.ut = QtWidgets.QCheckBox(self.groupBox_14)
        self.ut.setEnabled(True)
        self.ut.setGeometry(QtCore.QRect(81, 21, 64, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ut.setFont(font)
        self.ut.setObjectName("ut")
        self.ds = QtWidgets.QCheckBox(self.groupBox_14)
        self.ds.setEnabled(True)
        self.ds.setGeometry(QtCore.QRect(163, 21, 66, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ds.setFont(font)
        self.ds.setObjectName("ds")
        self.ot = QtWidgets.QCheckBox(self.groupBox_14)
        self.ot.setEnabled(True)
        self.ot.setGeometry(QtCore.QRect(326, 21, 59, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ot.setFont(font)
        self.ot.setObjectName("ot")
        self.groupBox_13 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 73, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_13.setFont(font)
        self.groupBox_13.setObjectName("groupBox_13")
        self.label_27 = QtWidgets.QLabel(self.groupBox_13)
        self.label_27.setEnabled(False)
        self.label_27.setGeometry(QtCore.QRect(63, 24, 35, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.APF = QtWidgets.QDateEdit(self.groupBox_13)
        self.APF.setEnabled(False)
        self.APF.setGeometry(QtCore.QRect(110, 23, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.APF.setFont(font)
        self.APF.setAlignment(QtCore.Qt.AlignCenter)
        self.APF.setDate(QtCore.QDate(1976, 1, 1))
        self.APF.setObjectName("APF")
        self.APT = QtWidgets.QDateEdit(self.groupBox_13)
        self.APT.setEnabled(False)
        self.APT.setGeometry(QtCore.QRect(270, 23, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.APT.setFont(font)
        self.APT.setAlignment(QtCore.Qt.AlignCenter)
        self.APT.setDate(QtCore.QDate(2025, 1, 1))
        self.APT.setObjectName("APT")
        self.label_28 = QtWidgets.QLabel(self.groupBox_13)
        self.label_28.setEnabled(False)
        self.label_28.setGeometry(QtCore.QRect(245, 24, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.APDdis = QtWidgets.QCheckBox(self.groupBox_13)
        self.APDdis.setGeometry(QtCore.QRect(16, 24, 31, 19))
        self.APDdis.setText("")
        self.APDdis.setObjectName("APDdis")
        self.groupBox_15 = QtWidgets.QGroupBox(self.groupBox_12)
        self.groupBox_15.setGeometry(QtCore.QRect(10, 126, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.groupBox_15.setFont(font)
        self.groupBox_15.setObjectName("groupBox_15")
        self.label_32 = QtWidgets.QLabel(self.groupBox_15)
        self.label_32.setEnabled(False)
        self.label_32.setGeometry(QtCore.QRect(63, 24, 35, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.IDF = QtWidgets.QDateEdit(self.groupBox_15)
        self.IDF.setEnabled(False)
        self.IDF.setGeometry(QtCore.QRect(110, 23, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IDF.setFont(font)
        self.IDF.setAlignment(QtCore.Qt.AlignCenter)
        self.IDF.setDate(QtCore.QDate(1976, 1, 1))
        self.IDF.setObjectName("IDF")
        self.IDT = QtWidgets.QDateEdit(self.groupBox_15)
        self.IDT.setEnabled(False)
        self.IDT.setGeometry(QtCore.QRect(270, 23, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IDT.setFont(font)
        self.IDT.setAlignment(QtCore.Qt.AlignCenter)
        self.IDT.setDate(QtCore.QDate(2025, 1, 1))
        self.IDT.setObjectName("IDT")
        self.label_33 = QtWidgets.QLabel(self.groupBox_15)
        self.label_33.setEnabled(False)
        self.label_33.setGeometry(QtCore.QRect(245, 24, 20, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.ISDdis = QtWidgets.QCheckBox(self.groupBox_15)
        self.ISDdis.setGeometry(QtCore.QRect(17, 23, 31, 19))
        self.ISDdis.setText("")
        self.ISDdis.setObjectName("ISDdis")
        self.groupBox_9 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_9.setEnabled(True)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 300, 441, 141))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setObjectName("groupBox_9")
        self.REFby = QtWidgets.QCheckBox(self.groupBox_9)
        self.REFby.setEnabled(True)
        self.REFby.setGeometry(QtCore.QRect(331, 50, 97, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.REFby.setFont(font)
        self.REFby.setObjectName("REFby")
        self.ABST = QtWidgets.QCheckBox(self.groupBox_9)
        self.ABST.setEnabled(True)
        self.ABST.setGeometry(QtCore.QRect(224, 50, 74, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ABST.setFont(font)
        self.ABST.setObjectName("ABST")
        self.TTL = QtWidgets.QCheckBox(self.groupBox_9)
        self.TTL.setEnabled(True)
        self.TTL.setGeometry(QtCore.QRect(11, 20, 54, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.TTL.setFont(font)
        self.TTL.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.TTL.setObjectName("TTL")
        self.IPC = QtWidgets.QCheckBox(self.groupBox_9)
        self.IPC.setEnabled(True)
        self.IPC.setGeometry(QtCore.QRect(224, 80, 53, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IPC.setFont(font)
        self.IPC.setObjectName("IPC")
        self.APD = QtWidgets.QCheckBox(self.groupBox_9)
        self.APD.setEnabled(True)
        self.APD.setGeometry(QtCore.QRect(118, 50, 85, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.APD.setFont(font)
        self.APD.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.APD.setObjectName("APD")
        self.CPCs = QtWidgets.QCheckBox(self.groupBox_9)
        self.CPCs.setEnabled(True)
        self.CPCs.setGeometry(QtCore.QRect(118, 80, 83, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CPCs.setFont(font)
        self.CPCs.setObjectName("CPCs")
        self.ISD = QtWidgets.QCheckBox(self.groupBox_9)
        self.ISD.setEnabled(True)
        self.ISD.setGeometry(QtCore.QRect(11, 50, 85, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ISD.setFont(font)
        self.ISD.setObjectName("ISD")
        self.IPCs = QtWidgets.QCheckBox(self.groupBox_9)
        self.IPCs.setEnabled(True)
        self.IPCs.setGeometry(QtCore.QRect(331, 80, 79, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IPCs.setFont(font)
        self.IPCs.setObjectName("IPCs")
        self.CPC = QtWidgets.QCheckBox(self.groupBox_9)
        self.CPC.setEnabled(True)
        self.CPC.setGeometry(QtCore.QRect(11, 80, 57, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.CPC.setFont(font)
        self.CPC.setObjectName("CPC")
        self.FMID = QtWidgets.QCheckBox(self.groupBox_9)
        self.FMID.setEnabled(True)
        self.FMID.setGeometry(QtCore.QRect(11, 110, 86, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.FMID.setFont(font)
        self.FMID.setObjectName("FMID")
        self.AANM = QtWidgets.QCheckBox(self.groupBox_9)
        self.AANM.setEnabled(True)
        self.AANM.setGeometry(QtCore.QRect(224, 20, 82, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.AANM.setFont(font)
        self.AANM.setObjectName("AANM")
        self.ApNo = QtWidgets.QCheckBox(self.groupBox_9)
        self.ApNo.setEnabled(True)
        self.ApNo.setGeometry(QtCore.QRect(118, 110, 91, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.ApNo.setFont(font)
        self.ApNo.setObjectName("ApNo")
        self.IN = QtWidgets.QCheckBox(self.groupBox_9)
        self.IN.setEnabled(True)
        self.IN.setGeometry(QtCore.QRect(118, 20, 75, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.IN.setFont(font)
        self.IN.setObjectName("IN")
        self.AN = QtWidgets.QCheckBox(self.groupBox_9)
        self.AN.setEnabled(True)
        self.AN.setGeometry(QtCore.QRect(331, 20, 77, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.AN.setFont(font)
        self.AN.setObjectName("AN")
        self.PAT = QtWidgets.QCheckBox(self.groupBox_9)
        self.PAT.setEnabled(True)
        self.PAT.setGeometry(QtCore.QRect(224, 110, 93, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PAT.setFont(font)
        self.PAT.setObjectName("PAT")
        self.PDF = QtWidgets.QCheckBox(self.groupBox_9)
        self.PDF.setEnabled(True)
        self.PDF.setGeometry(QtCore.QRect(331, 110, 84, 19))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.PDF.setFont(font)
        self.PDF.setObjectName("PDF")
        self.TABLE = QtWidgets.QTableView(self.tab_3)
        self.TABLE.setGeometry(QtCore.QRect(460, 12, 561, 428))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.TABLE.setFont(font)
        self.TABLE.setObjectName("TABLE")
        self.tabWidget.addTab(self.tab_3, "")
        self.reader = QtWidgets.QWidget()
        self.reader.setObjectName("reader")
        self.PNweb = QtWidgets.QLineEdit(self.reader)
        self.PNweb.setGeometry(QtCore.QRect(110, 17, 141, 22))
        self.PNweb.setObjectName("PNweb")
        self.GL = QtWidgets.QOpenGLWidget(self.reader)
        self.GL.setGeometry(QtCore.QRect(10, 50, 1011, 491))
        self.GL.setObjectName("GL")
        self.web_PAT = QtWidgets.QPushButton(self.reader)
        self.web_PAT.setGeometry(QtCore.QRect(260, 11, 93, 30))
        self.web_PAT.setObjectName("web_PAT")
        self.web_PDF = QtWidgets.QPushButton(self.reader)
        self.web_PDF.setGeometry(QtCore.QRect(360, 11, 141, 30))
        self.web_PDF.setObjectName("web_PDF")
        self.label = QtWidgets.QLabel(self.reader)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.reader, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1050, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menuBar)
        self.actionVisit_Github_Repo = QtWidgets.QAction(MainWindow)
        self.actionVisit_Github_Repo.setObjectName("actionVisit_Github_Repo")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuAbout.addAction(self.actionVisit_Github_Repo)
        self.menuAbout.addAction(self.actionAbout_2)
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.PNbt.clicked['bool'].connect(self.label_7.setVisible)
        self.Querybt.clicked['bool'].connect(self.DB.setVisible)
        self.PNbt.clicked['bool'].connect(self.PNbws.setVisible)
        self.PNbt.clicked['bool'].connect(self.PNloc.setVisible)
        self.Querybt.clicked['bool'].connect(self.label_7.setHidden)
        self.Querybt.clicked['bool'].connect(self.PNloc.setHidden)
        self.Querybt.clicked['bool'].connect(self.PNbws.setHidden)
        self.PNbt.clicked['bool'].connect(self.Querybox.setHidden)
        self.Querybt.clicked['bool'].connect(self.Querybox.setVisible)
        self.PNbt.clicked['bool'].connect(self.DB.setHidden)
        self.all.clicked['bool'].connect(self.ut.setDisabled)
        self.all.clicked['bool'].connect(self.ds.setDisabled)
        self.all.clicked['bool'].connect(self.pp.setDisabled)
        self.all.clicked['bool'].connect(self.ot.setDisabled)
        self.APDdis.clicked['bool'].connect(self.APF.setEnabled)
        self.APDdis.clicked['bool'].connect(self.APT.setEnabled)
        self.groupBox_13.clicked['bool'].connect(self.label_28.setEnabled)
        self.APDdis.clicked['bool'].connect(self.label_27.setEnabled)
        self.ISDdis.clicked['bool'].connect(self.label_32.setEnabled)
        self.ISDdis.clicked['bool'].connect(self.IDF.setEnabled)
        self.ISDdis.clicked['bool'].connect(self.label_33.setEnabled)
        self.ISDdis.clicked['bool'].connect(self.IDT.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "USPTO PatFT Database Crawler"))
        self.groupBox_8.setTitle(_translate("MainWindow", "PDF Download"))
        self.PDFbws.setText(_translate("MainWindow", "..."))
        self.label_19.setText(_translate("MainWindow", "Save at:"))
        self.PDFfull.setText(_translate("MainWindow", "Download PDF "))
        self.PDFdraw.setText(_translate("MainWindow", "Dowload Drawing Section Only "))
        self.groupBox_10.setTitle(_translate("MainWindow", "Execution"))
        self.EXPORT.setText(_translate("MainWindow", "Export CSV"))
        self.FILTER.setText(_translate("MainWindow", "Filtering Data"))
        self.PDFD.setText(_translate("MainWindow", "Download PDF"))
        self.INFO.setText(_translate("MainWindow", "Info Crawling"))
        self.IMPORT.setText(_translate("MainWindow", "Import Target"))
        self.STOPLOOP.setText(_translate("MainWindow", "Stop"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Fetching Target Insertion:"))
        self.PNbws.setText(_translate("MainWindow", "..."))
        self.Querybox.setPlainText(_translate("MainWindow", "((CPC/A62B$ OR CPC/B65H$) AND brak$ AND \"safety line\")"))
        self.label_7.setText(_translate("MainWindow", "Please select a CSV file containing Patent No. (9 digits) in the 1st column."))
        self.PNbt.setText(_translate("MainWindow", "PN List"))
        self.Querybt.setText(_translate("MainWindow", "Query"))
        self.DB.setItemText(0, _translate("MainWindow", "1976 to present [full-text]"))
        self.DB.setItemText(1, _translate("MainWindow", "1790 to present [entire database]"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Filtering Data"))
        self.groupBox_14.setTitle(_translate("MainWindow", "Patent Type"))
        self.all.setText(_translate("MainWindow", "All"))
        self.pp.setText(_translate("MainWindow", "Plant"))
        self.ut.setText(_translate("MainWindow", "Utility"))
        self.ds.setText(_translate("MainWindow", "Design"))
        self.ot.setText(_translate("MainWindow", "Other"))
        self.groupBox_13.setTitle(_translate("MainWindow", "App. Date (Examined if listed)"))
        self.label_27.setText(_translate("MainWindow", "From:"))
        self.label_28.setText(_translate("MainWindow", "To:"))
        self.groupBox_15.setTitle(_translate("MainWindow", "Issue Date"))
        self.label_32.setText(_translate("MainWindow", "From:"))
        self.label_33.setText(_translate("MainWindow", "To:"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Info. Crawler"))
        self.REFby.setText(_translate("MainWindow", "#Referenced"))
        self.ABST.setText(_translate("MainWindow", "Abstract"))
        self.TTL.setText(_translate("MainWindow", "Title"))
        self.IPC.setText(_translate("MainWindow", "IPC "))
        self.APD.setText(_translate("MainWindow", "Appl. Date"))
        self.CPCs.setText(_translate("MainWindow", "CPC Sub."))
        self.ISD.setText(_translate("MainWindow", "Issue Date"))
        self.IPCs.setText(_translate("MainWindow", "IPC Sub."))
        self.CPC.setText(_translate("MainWindow", "CPC "))
        self.FMID.setText(_translate("MainWindow", "Family ID"))
        self.AANM.setText(_translate("MainWindow", "Applicant"))
        self.ApNo.setText(_translate("MainWindow", "Appl. No."))
        self.IN.setText(_translate("MainWindow", "Inventor"))
        self.AN.setText(_translate("MainWindow", "Assignee"))
        self.PAT.setText(_translate("MainWindow", "PatFT Link"))
        self.PDF.setText(_translate("MainWindow", "PDF Link"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Patent Fetcher"))
        self.PNweb.setText(_translate("MainWindow", "9532164"))
        self.web_PAT.setText(_translate("MainWindow", "PatFT"))
        self.web_PDF.setText(_translate("MainWindow", "PDF (external)"))
        self.label.setText(_translate("MainWindow", "Patent No.:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reader), _translate("MainWindow", "Browser"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionVisit_Github_Repo.setText(_translate("MainWindow", "Visit Github Repo."))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

