from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

import sys

# Bintang Fajarianto
# 13519138

BLANK = ""
DEFAULT_TEXT_COLOR = "color: rgb(251, 251, 251)"
WARNING_TEXT_COLOR = "color: rgb(255, 0, 0)"

class Run(QDialog):
    def __init__(self):
        super(Run,self).__init__()
        loadUi("./ui/run.ui",self)

        # Button
        self.start_button.clicked.connect(self.goToApp)

    def goToApp(self):
        main = MainWindow()
        main.setFixedWidth(800)
        main.setFixedHeight(500)

        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("./ui/main.ui",self)

        # Button
        self.set_button.clicked.connect(self.prepareApp)
        self.start_button.clicked.connect(self.startApp)
        self.reset_button.clicked.connect(self.resetApp)

        self.default_boxes = {
            self.box_1 : 1, self.box_2 : 2, self.box_3 : 3, self.box_4 : 4,
            self.box_5 : 5, self.box_6 : 0, self.box_7 : 6, self.box_8 : 7,
            self.box_9 : 10, self.box_10 : 11, self.box_11 : 12, self.box_12 : 8,
            self.box_13 : 9, self.box_14 : 13, self.box_15 : 14, self.box_16 : 15
            }

        self.labels = [self.info_1, self.info_2, self.info_3]
        self.get_boxes_from_value(0).setVisible(False)

    def set_all_boxes_visible(self):
        for box in self.default_boxes:
            box.setVisible(True)
    
    def set_default_labels_color(self):
        self.start_button.setVisible(True)
        for label in self.labels:
            label.setStyleSheet(DEFAULT_TEXT_COLOR)

    def get_boxes_from_value(self,value):
        for key, val in self.default_boxes.items():
            if val == value:
                return key
    
    def set_boxes_value(self, values):
        i = 0
        for box in self.default_boxes.keys():
            self.default_boxes[box] = values[i]
            box.setText(str(values[i]))
            i += 1
        
        self.set_all_boxes_visible()
        self.get_boxes_from_value(0).setVisible(False)
    
    def prepareApp(self):
        self.set_default_labels_color()
        inputan = self.input_box.text().replace(" ","").replace("\n","").split(",")

        #validate
        valid = True
        try:
            inputan = list(map(int, inputan))
        except:
            self.labels[0].setStyleSheet(WARNING_TEXT_COLOR)
            valid = False

        else:
            if len(inputan) != 16:
                self.labels[0].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False
            if not all(0<=x<=15 for x in inputan):
                self.labels[1].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False
            if any(inputan.count(x) > 1 for x in inputan):
                self.labels[2].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False

        finally:
            if valid:
                self.set_boxes_value(inputan)
            else:
                self.start_button.setVisible(False)


    def startApp(self):
        app.closeAllWindows()

    def resetApp(self):
        self.set_default_labels_color()
        self.set_boxes_value([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

run = Run()
widget.addWidget(run)
run.setFixedWidth(400)
run.setFixedHeight(300)

widget.show()
app.exec_()