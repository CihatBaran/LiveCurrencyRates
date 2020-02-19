from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
import requests
from bs4 import BeautifulSoup



class Ui_Dialog(object):

    def __init__(self,dialog):
        timer = QtCore.QTimer(dialog)
        timer.timeout.connect(self.change_values)
        timer.start(1000)
        super(Ui_Dialog, self).__init__()


    def change_values(self):
        self.url = "https://www.doviz.com/"
        self.response = requests.get(self.url)

        self.html_content = self.response.content
        self.soup = BeautifulSoup(self.html_content,"html.parser")
        
      
        tempList = []
        temp = self.soup.findAll("span",{"class":"value"})
                   
        for i in temp:
            i = i.text
            i = i.strip()
            i = i.strip("\n")
            tempList.append(i)
        tempList = tempList[:6]
        new_list = []
        for index in tempList:
            myString=""
            counter = 0
            for i in index:
                if(i.isdigit()):
                    myString+=i
                elif(i == ","):
                    if (counter == 0):
                        i="."
                    else:
                        i=""
                    myString+=i
                    counter +=1
                    
                        
            new_list.append(myString)
        
        last_list =[]
        for i in new_list:
            i = float(i)
            last_list.append(i)
            
        
        self.tl_gr_gold = last_list[0]
        self.tl_dolar = last_list[1]
        self.tl_euro = last_list[2]
        self.tl_sterlin = last_list[3]
        self.tl_interest = last_list[5]

        if (self.comboBox_3.currentText() == "TL"):
            x = 1
        elif(self.comboBox_3.currentText() == "USD"):
            x = 1 / self.tl_dolar
        elif(self.comboBox_3.currentText() == "STERLIN"):
            x = 1 / self.tl_sterlin
        elif (self.comboBox_3.currentText() == "GR GOLD"):
            x = 1 / self.tl_gr_gold
        elif (self.comboBox_3.currentText() == "EURO"):
            x = 1 / self.tl_euro
        elif(self.comboBox_3.currentText() == "INTEREST"):
            self.textEdit.setText("CANNOT CONVERT INTEREST RATE")
            self.textEdit_2.setText("CANNOT CONVERT INTEREST RATE")
            self.textEdit_3.setText("CANNOT CONVERT INTEREST RATE")
            self.textEdit_4.setText("CANNOT CONVERT INTEREST RATE")
            self.textEdit_5.setText("CANNOT CONVERT INTEREST RATE")
            
        if (self.comboBox_3.currentText != "INTEREST"):
            self.textEdit.setText(str(x*self.tl_gr_gold))
            self.textEdit_2.setText(str(self.tl_interest))
            self.textEdit_3.setText(str(x*self.tl_sterlin))
            self.textEdit_4.setText(str(x*self.tl_dolar))
            self.textEdit_5.setText(str(x*self.tl_euro))

        
    def convert_IT(self):
        if (self.comboBox.currentText() == "USD"):
            y = self.tl_dolar
        elif(self.comboBox.currentText() == "INTEREST"):
            y = self.tl_interest
        elif(self.comboBox.currentText() == "STERLIN"):
            y = self.tl_sterlin
        elif (self.comboBox.currentText() == "GR GOLD"):
            y = self.tl_gr_gold
        elif (self.comboBox.currentText() == "EURO"):
            y = self.tl_euro


        if (self.comboBox_2.currentText() == "USD"):
            x = self.tl_dolar
        elif(self.comboBox_2.currentText() == "INTEREST"):
            x = self.tl_interest
        elif(self.comboBox_2.currentText() == "STERLIN"):
            x = self.tl_sterlin
        elif (self.comboBox_2.currentText() == "GR GOLD"):
            x = self.tl_gr_gold
        elif (self.comboBox_2.currentText() == "EURO"):
            x = self.tl_euro


        if (self.comboBox.currentText() == "INTEREST" or self.comboBox_2.currentText()=="INTEREST" ):
            self.plainTextEdit.setPlainText("THIS IS INTEREST CANNOT BE CONVERTED")
        else:
            self.plainTextEdit.setPlainText("1.00 {} equels to {} {}".format(
                self.comboBox.currentText(),(y/x), self.comboBox_2.currentText()
                
            ))

        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1060, 542)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 0, 371, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(350, 420, 55, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 110, 181, 321))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(190, 110, 70, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 110, 51, 31))
        self.pushButton.setObjectName("pushButton")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(310, 110, 70, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 140, 191, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.convert_IT)

        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 170, 191, 261))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(400, 10, 70, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 50, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(490, 50, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(580, 50, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 50, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(760, 50, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(400, 80, 451, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(400, 100, 91, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(490, 100, 91, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(580, 100, 91, 41))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(670, 100, 91, 41))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(760, 100, 91, 41))
        self.textEdit_5.setObjectName("textEdit_5")
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(400, 160, 451, 271))
        self.calendarWidget.setObjectName("calendarWidget")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setText(_translate("Dialog", "CURRENT CURRENCY RATES"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "GR GOLD"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "INTEREST"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "USD"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "STERLIN"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "EURO"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("Dialog", "USD"))
        self.comboBox.setItemText(1, _translate("Dialog", "INTEREST"))
        self.comboBox.setItemText(2, _translate("Dialog", "STERLIN"))
        self.comboBox.setItemText(3, _translate("Dialog", "GR GOLD"))
        self.comboBox.setItemText(4, _translate("Dialog", "EURO"))
        self.pushButton.setText(_translate("Dialog", "To"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "USD"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "INTEREST"))
        self.comboBox_2.setItemText(2, _translate("Dialog", "STERLIN"))
        self.comboBox_2.setItemText(3, _translate("Dialog", "GR GOLD"))
        self.comboBox_2.setItemText(4, _translate("Dialog", "EURO"))
        self.pushButton_2.setText(_translate("Dialog", "CONVERT"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "TL"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "USD"))
        self.comboBox_3.setItemText(2, _translate("Dialog", "INTEREST"))
        self.comboBox_3.setItemText(3, _translate("Dialog", "STERLIN"))
        self.comboBox_3.setItemText(4, _translate("Dialog", "GR GOLD"))
        self.comboBox_3.setItemText(5, _translate("Dialog", "EURO"))
        self.pushButton_3.setText(_translate("Dialog", "GR GOLD"))
        self.pushButton_4.setText(_translate("Dialog", "INTEREST"))
        self.pushButton_5.setText(_translate("Dialog", "STERLIN"))
        self.pushButton_6.setText(_translate("Dialog", "USD"))
        self.pushButton_7.setText(_translate("Dialog", "EURO"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())

