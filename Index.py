from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from projectcacu import Ui_MainWindow
import sys
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()

    ui.setupUi(MainWindow)
    MainWindow.show()

#ISTID3A2 DALAT



#true non false
kWILI = True
amine =  None
#***************************************************

#                      بسم الله الرحمان الرحيم
#programe logic

#function
def zero():
    global kWILI
    if kWILI:
        ui.lineEdit.setText(ui.lineEdit.text()+"0")
    if not kWILI:
        ui.lineEdit.setText("0")
    kWILI = True

def wahed():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"1")
    if kWILI == False:
        ui.lineEdit.setText("1")
    kWILI = True
def jouj():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"2")
    if kWILI == False:
        ui.lineEdit.setText("2")
    kWILI = True
def tlata():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"3")
    if kWILI == False:
        ui.lineEdit.setText("3")
    kWILI = True
def rb3aa():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"4")
    if kWILI == False:
        ui.lineEdit.setText("4")
    kWILI = True



def khmsa():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"5")
    if kWILI == False:
        ui.lineEdit.setText("5")
    kWILI = True

def sta():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"6")
    if kWILI == False:
        ui.lineEdit.setText("6")
    kWILI = True


def sb3a():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"7")
    if kWILI == False:
        ui.lineEdit.setText("7")

    kWILI = True



def tmnia():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"8")
    if kWILI == False:
        ui.lineEdit.setText("8")
    kWILI = True

def ts3ud():
    global kWILI
    if kWILI == True:
        ui.lineEdit.setText(ui.lineEdit.text()+"9")
    if kWILI == False:
        ui.lineEdit.setText("9")
    kWILI = True

#specractere
def n9ta():
    global kWILI
    if kWILI:
        ui.lineEdit.setText(ui.lineEdit.text()+".")
    if not kWILI:
        ui.lineEdit.setText(".")
    kWILI = True

def brackitalimnia():
    global kWILI
    if kWILI:
        ui.lineEdit.setText(ui.lineEdit.text()+")")
    if not kWILI:
        ui.lineEdit.setText(")")
    kWILI = True
def brackitalisira():
    global kWILI
    if kWILI:
        ui.lineEdit.setText(ui.lineEdit.text()+"(")
    if not kWILI:
        ui.lineEdit.setText("(")
    kWILI = True

def za2id():
    global kWILI
    ui.lineEdit.setText(ui.lineEdit.text()+"+")
    kWILI = True

def na9is():
    global kWILI
    ui.lineEdit.setText(ui.lineEdit.text()+"-")
    kWILI = True

def dareb():
    global kWILI
    ui.lineEdit.setText(ui.lineEdit.text()+"*")
    kWILI = True

def qisma():
    global kWILI
    ui.lineEdit.setText(ui.lineEdit.text()+"/")
    kWILI = True

def deli():
    global kWILI
    if kWILI:
        ui.lineEdit.setText(ui.lineEdit.text()[0:-1])
    if not kWILI:
        ui.lineEdit.setText("")
    kWILI = True

def AC():
     ui.lineEdit.setText('')

def ANS():
    global amine
    global kWILI
    if amine is not None:
        ui.lineEdit.setText(ui.lineEdit.text()+str(amine))
    if amine is None:
        pass

def equal():
    try:
        global kWILI
        global gg
        global amine
        ui.lineEdit.setText(str(eval(ui.lineEdit.text())))
        amine = ui.lineEdit.text()
        kWILI = False
    except ZeroDivisionError:
        ui.lineEdit.setText("المعذرة لا يمكن القسمة على صفر !!")
        kWILI = False
    except Exception:
        ui.lineEdit.setText("المعدرة هناك خطأ !!")
        kWILI = False



def start():
    global kWILI
    ui.lineEdit.setText("مرحبا بكم في برنامج الالة الحاسبة")
    kWILI = False

#dalat       88888888888888888888888888
start()
#connection
ui.pushButton_4.clicked.connect(zero)
ui.pushButton_2.clicked.connect(wahed)
ui.pushButton_5.clicked.connect(jouj)
ui.pushButton_10.clicked.connect(tlata)
ui.pushButton.clicked.connect(rb3aa)
ui.pushButton_7.clicked.connect(khmsa)
ui.pushButton_6.clicked.connect(sta)
ui.pushButton_8.clicked.connect(sb3a)
ui.pushButton_9.clicked.connect(tmnia)
ui.pushButton_3.clicked.connect(ts3ud)
ui.pushButton_21.clicked.connect(n9ta)
ui.pushButton_18.clicked.connect(za2id)
ui.pushButton_16.clicked.connect(na9is)
ui.pushButton_22.clicked.connect(dareb)
ui.pushButton_17.clicked.connect(qisma)
ui.pushButton_20.clicked.connect(equal)
ui.pushButton_13.clicked.connect(deli)
ui.pushButton_12.clicked.connect(AC)
ui.pushButton_15.clicked.connect(brackitalisira)
ui.pushButton_14.clicked.connect(brackitalimnia)
ui.pushButton_11.clicked.connect(ANS)










sys.exit(app.exec_())

