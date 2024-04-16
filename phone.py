from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #=========Fixed Size =============
        Form.setFixedSize(300, 350)
        #==========Background=============
        gradient = QtGui.QLinearGradient(0, 0, 0, Form.height())
        gradient.setColorAt(0, QtGui.QColor("#f0f0f0")) 
        gradient.setColorAt(1, QtGui.QColor("#d0d0d0")) 
        Form.setStyleSheet("background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #f0f0f0, stop:1 #d0d0d0);")
        #Labels
        label_style = "QLabel { color: black; padding: 5px; }"
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 110, 60, 25))
        self.label.setObjectName("label")
        self.label.setStyleSheet(label_style)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 60, 25))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet(label_style)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(127, 170, 80, 23))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet(label_style)

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(137, 30, 70, 23))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet(label_style)
        #===========Input Boxes ===================
        self.NameRecieve = QtWidgets.QTextEdit(Form)
        self.NameRecieve.setGeometry(QtCore.QRect(100, 60, 141, 31))
        self.NameRecieve.setObjectName("NameRecieve")

        self.NumberRecieve = QtWidgets.QTextEdit(Form)
        self.NumberRecieve.setGeometry(QtCore.QRect(100, 100, 141, 31))
        self.NumberRecieve.setObjectName("NumberRecieve")

        #======================Styling for buttons============================================================
        button_style = ("QPushButton { color: white; background-color: #4CAF50; border: 2px solid #4CAF50;"
                        " border-radius: 10px; padding: 5px; }"
                        "QPushButton:hover { background-color: #45a049; }")  
        
        self.Save = QtWidgets.QPushButton(Form)
        self.Save.setGeometry(QtCore.QRect(130, 140, 75, 23))
        self.Save.setObjectName("Save")
        self.Save.setStyleSheet(button_style)
        self.Save.clicked.connect(self.Insert)

        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(100, 200, 141, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentTextChanged.connect(self.Show)

        self.NumberReturn = QtWidgets.QTextEdit(Form)
        self.NumberReturn.setGeometry(QtCore.QRect(100, 230, 141, 31))
        self.NumberReturn.setObjectName("NumberReturn")

        self.DeleteButton = QtWidgets.QPushButton(Form)
        self.DeleteButton.setGeometry(QtCore.QRect(130, 270, 75, 23))
        self.DeleteButton.setObjectName("DeleteButton")
        self.DeleteButton.setStyleSheet(button_style)
        self.DeleteButton.clicked.connect(self.Delete)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.ComboData()  # Fill ComboBox with existing data

    # ===========importing============
    def Insert(self):
        try:
            con = sqlite3.connect("h30.db")
            number = self.NumberRecieve.toPlainText().strip()  
            name = self.NameRecieve.toPlainText().strip()  
            if name and number:  # Check if both name and number are non-empty
                data = [name, number]
                con.execute("INSERT INTO daftarche(Name,Number) VALUES(?,?)", data)  
                con.commit()
                self.comboBox.addItem(name)  # Add the inserted name to the ComboBox
                print("Done")
        except Exception as e:
            print("Error:", e)
        finally:
            con.close()

    def ComboData(self):
        self.comboBox.clear()
        try:
            con = sqlite3.connect("h30.db")
            names = con.execute("SELECT Name FROM daftarche")
            for name in names:
                self.comboBox.addItem(str(name[0]))
            print("ComboBox data loaded")
        except Exception as e:
            print("Error:", e)
        finally:
            con.close()

    def Show(self, selected):
        try:
            con = sqlite3.connect("h30.db")
            cursor = con.cursor()
            name = self.comboBox.currentText()  # Get the currently selected name from the ComboBox
            cursor.execute("SELECT Number FROM daftarche WHERE Name=?", (name,))
            number = cursor.fetchone()
            if number:
                self.NumberReturn.setText(str(number[0]))  # Set the number in the NumberReturn QTextEdit
            else:
                self.NumberReturn.clear()  # Clear the QTextEdit if number is not found
            print("Number found:", number)
        except Exception as e:
            print("Error:", e)
        finally:
            con.close()

    def Delete(self):
        try:
            con = sqlite3.connect("h30.db")
            name = self.comboBox.currentText()  # Get the currently selected name from the ComboBox
            con.execute("DELETE FROM daftarche WHERE Name=?", (name,))
            con.commit()
            self.comboBox.removeItem(self.comboBox.currentIndex())  # Remove the selected name from the ComboBox
            print("Deleted:", name)
        except Exception as e:
            print("Error:", e)
        finally:
            con.close()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Number :"))
        self.label_2.setText(_translate("Form", "Name    :"))
        self.label_3.setText(_translate("Form", "---Recieve---"))
        self.label_4.setText(_translate("Form", "----Add----"))
        self.NameRecieve.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.NumberRecieve.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.Save.setText(_translate("Form", "Save"))
        self.DeleteButton.setText(_translate("Form", "Delete"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
