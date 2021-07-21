from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from PyQt5.uic import loadUi

import sys
import time

from src.a_star import AStar
from src.puzzle import Puzzle

# Bintang Fajarianto
# 13519138

BLANK = ""
DEFAULT_TEXT_COLOR = "color: rgb(251, 251, 251)"
WARNING_TEXT_COLOR = "color: rgb(255, 0, 0)"
GREEN_TEXT_COLOR = "color: rgb(0, 255, 0)"

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

        self.inputan = []

        # Button
        self.set_button.clicked.connect(self.prepareApp)
        self.start_button.clicked.connect(self.startApp)
        self.reset_button.clicked.connect(self.resetApp)
        self.prev_button.clicked.connect(self.prevPuzzle)
        self.next_button.clicked.connect(self.nextPuzzle)

        self.default_boxes = {
            self.box_1 : 1, self.box_2 : 2, self.box_3 : 3, self.box_4 : 4,
            self.box_5 : 5, self.box_6 : 0, self.box_7 : 6, self.box_8 : 7,
            self.box_9 : 10, self.box_10 : 11, self.box_11 : 12, self.box_12 : 8,
            self.box_13 : 9, self.box_14 : 13, self.box_15 : 14, self.box_16 : 15
            }

        self.labels = [self.info_1, self.info_2, self.info_3]
        self.start_button.setVisible(False)
        self.prev_button.setVisible(False)
        self.next_button.setVisible(False)
        self.get_boxes_from_value(0).setVisible(False)

        self.result = []
        self.step = 0

    def inputan_to_puzzle(self):
        return [self.inputan[:4], self.inputan[4:8], self.inputan[8:12], self.inputan[12:16]]

    def puzzle_to_inputan(self, puzzle):
        return [x for row in puzzle for x in row]

    def set_all_boxes_visible(self):
        for box in self.default_boxes:
            box.setVisible(True)
    
    def set_default_labels_color(self):
        self.solvable.setStyleSheet(DEFAULT_TEXT_COLOR)
        self.not_solvable.setStyleSheet(DEFAULT_TEXT_COLOR)
        
        for label in self.labels:
            label.setStyleSheet(DEFAULT_TEXT_COLOR)

    def set_default_counter(self):
        self.n_steps.setText("0")
        self.n_expanded_nodes.setText("0")

    def set_counter(self):
        self.n_steps.setText(str(self.step))

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
        self.set_default_counter()
        self.inputan = self.input_box.text().replace(" ","").replace("\n","").split(",")

        #validate
        valid = True
        try:
            self.inputan = list(map(int, self.inputan))
        except:
            self.labels[0].setStyleSheet(WARNING_TEXT_COLOR)
            valid = False

        else:
            if len(self.inputan) != 16:
                self.labels[0].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False
            if not all(0<=x<=15 for x in self.inputan):
                self.labels[1].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False
            if any(self.inputan.count(x) > 1 for x in self.inputan):
                self.labels[2].setStyleSheet(WARNING_TEXT_COLOR)
                valid = False

        finally:
            if valid:
                self.set_boxes_value(self.inputan)
                self.start_button.setVisible(True)
            else:
                self.start_button.setVisible(False)

            self.prev_button.setVisible(False)
            self.next_button.setVisible(False)


    def startApp(self):
        puzzle = Puzzle(self.inputan_to_puzzle())
        a_star = AStar(puzzle)
        solvable = a_star.is_puzzle_solvable()

        if solvable:
            self.solvable.setStyleSheet(GREEN_TEXT_COLOR)
            self.next_button.setVisible(True)
            
            a_star.do_algorithm()
            
            self.n_expanded_nodes.setText(str(a_star.n_nodes_expanded))
            self.result = a_star.get_solution()
            print(self.result[0])

        else:
            self.not_solvable.setStyleSheet(WARNING_TEXT_COLOR)

    def resetApp(self):
        self.set_default_labels_color()
        self.set_default_counter()
        self.set_boxes_value([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0])
        self.inputan = []
        self.start_button.setVisible(False)
        self.prev_button.setVisible(False)
        self.next_button.setVisible(False)

    def prevPuzzle(self):
        self.next_button.setVisible(True)
        self.step -= 1
        self.set_boxes_value(self.puzzle_to_inputan(self.result[self.step]))
        self.set_counter()

        if self.step == 0:
            self.prev_button.setVisible(False)

    def nextPuzzle(self):
        self.prev_button.setVisible(True)
        self.step += 1
        self.set_boxes_value(self.puzzle_to_inputan(self.result[self.step]))

        self.set_counter()
        if self.step == len(self.result)-1:
            self.next_button.setVisible(False)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

run = Run()
widget.addWidget(run)
run.setFixedWidth(400)
run.setFixedHeight(300)

widget.show()
app.exec_()