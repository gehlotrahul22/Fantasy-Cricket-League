# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate_score.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import functions                                     #Contains All Functions Used
import images_rc                                #Contains All Images Used

class Ui_EvaluateScore(object):
    def setupUi(self, EvaluateScore):
        EvaluateScore.setObjectName("EvaluateScore")
        EvaluateScore.resize(1161, 950)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/windowicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        EvaluateScore.setWindowIcon(icon)
        EvaluateScore.setStyleSheet("border-image: url(:/img/564421.jpg);")
        self.gridLayout = QtWidgets.QGridLayout(EvaluateScore)
        self.gridLayout.setObjectName("gridLayout")
        self.calculateScoreButton = QtWidgets.QPushButton(EvaluateScore)
        self.calculateScoreButton.setStyleSheet("font: 87 72pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 0, 0,100);\n"
"color: rgb(255, 255, 255);border-image: url;")
        self.calculateScoreButton.setDefault(False)
        self.calculateScoreButton.setFlat(False)
        self.calculateScoreButton.setObjectName("calculateScoreButton")
        self.gridLayout.addWidget(self.calculateScoreButton, 4, 0, 1, 3)
        self.finalScore = QtWidgets.QLabel(EvaluateScore)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.finalScore.sizePolicy().hasHeightForWidth())
        self.finalScore.setSizePolicy(sizePolicy)
        self.finalScore.setMinimumSize(QtCore.QSize(500, 0))
        self.finalScore.setMaximumSize(QtCore.QSize(16777215, 500))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(97)
        self.finalScore.setFont(font)
        self.finalScore.setStyleSheet("border-image: url(:/img/92-924018_moon-atmosphere-desktop-wallpaper-png-moon-removebg-preview.png);")
        self.finalScore.setScaledContents(True)
        self.finalScore.setAlignment(QtCore.Qt.AlignCenter)
        self.finalScore.setObjectName("finalScore")
        self.gridLayout.addWidget(self.finalScore, 3, 1, 1, 1)
        self.matchSelectComboBox = QtWidgets.QComboBox(EvaluateScore)
        self.matchSelectComboBox.setStyleSheet("font: 87 26pt \"Segoe UI Black\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);border-image: url;")
        self.matchSelectComboBox.setObjectName("matchSelectComboBox")
        self.gridLayout.addWidget(self.matchSelectComboBox, 0, 2, 1, 1)
        self.playersList = QtWidgets.QListWidget(EvaluateScore)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(21)
        self.playersList.setFont(font)
        self.playersList.setStyleSheet("background-color: rgb(0, 0, 0,75);\n"
"color: rgb(255, 255, 255);border-image: url;")
        self.playersList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playersList.setObjectName("playersList")
        self.gridLayout.addWidget(self.playersList, 3, 0, 1, 1)
        self.teamSelectComboBox = QtWidgets.QComboBox(EvaluateScore)
        self.teamSelectComboBox.setStyleSheet("font: 87 26pt \"Segoe UI Black\";\n"
"border-image: url;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.teamSelectComboBox.setIconSize(QtCore.QSize(42, 37))
        self.teamSelectComboBox.setObjectName("teamSelectComboBox")
        self.gridLayout.addWidget(self.teamSelectComboBox, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(EvaluateScore)
        self.line.setMinimumSize(QtCore.QSize(0, 30))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url;\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 1, 0, 1, 3)
        self.playerScoreList = QtWidgets.QListWidget(EvaluateScore)
        self.playerScoreList.setMinimumSize(QtCore.QSize(0, 20))
        self.playerScoreList.setStyleSheet("background-color: rgb(0, 0, 0,75);\n"
"color: rgb(255, 255, 255);border-image: url;")
        self.playerScoreList.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playerScoreList.setObjectName("playerScoreList")
        self.playerScoreList.setFont(font)
        self.gridLayout.addWidget(self.playerScoreList, 3, 2, 1, 1)
        self.PlayerLabel = QtWidgets.QLabel(EvaluateScore)
        self.PlayerLabel.setStyleSheet("font: 87 26pt \"Segoe UI Black\";\n"
"border-image: url;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.PlayerLabel.setObjectName("PlayerLabel")
        self.gridLayout.addWidget(self.PlayerLabel, 2, 0, 1, 1)
        self.ScoreLabel = QtWidgets.QLabel(EvaluateScore)
        self.ScoreLabel.setStyleSheet("font: 87 26pt \"Segoe UI Black\";\n"
"border-image: url;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ScoreLabel.setObjectName("ScoreLabel")
        self.gridLayout.addWidget(self.ScoreLabel, 2, 2, 1, 1)

        self.retranslateUi(EvaluateScore)
        QtCore.QMetaObject.connectSlotsByName(EvaluateScore)

        #Event Handler Function For Calculate Score Button

        self.calculateScoreButton.clicked.connect(self.__getScore)

        #To Get All Teams Names And Display In Combo Box

        teams=functions.getTeams()                      #To Get All Team Names
        self.teamSelectComboBox.addItems(teams)     #Adding All Team Names To Combo Box

        #To Display Matches List In Combo Box

        matches=["Match1","Match2","Match3"]        #Making List Of Matches
        self.matchSelectComboBox.addItems(matches)  #Adding Matches List To Combo Box
#________________________________________________________________________________________________        
    #Function To Get And Display Final Score Of Selected Team In Selected Match
    def __getScore(self):
        totalScore=0
        self.__clearLists()                                               #Clearing Both Lists

        match=self.matchSelectComboBox.currentText()                    #To Get Match Selected By User
        team=self.teamSelectComboBox.currentText()                      #To Get Team Selected By User
        teamPlayersList=functions.getTeamMembers(team)                       # To Get Team Members
        self.playersList.addItems(teamPlayersList)                      #Show Team Players In List

        for player in teamPlayersList:              
            playerScore=functions.calculatePlayerScore(player,match)         #To Calculate Score Of Each Individual Player
            self.playerScoreList.addItem(str(playerScore))              #To Display Players Score
            totalScore=totalScore+playerScore                           #Adding All Players Individual Score To Get Final Score

        self.finalScore.setText(str(totalScore))                        #To Display Final Score

        
#_________________________________________________________________________________________________
    #Clearing Both Lists
    def __clearLists(self):
        self.playerScoreList.clear()
        self.playersList.clear()


    def retranslateUi(self, EvaluateScore):
        _translate = QtCore.QCoreApplication.translate
        EvaluateScore.setWindowTitle(_translate("EvaluateScore", "Evaluate Score"))
        self.calculateScoreButton.setText(_translate("EvaluateScore", "Calculate Score"))
        self.finalScore.setText(_translate("EvaluateScore", "00"))
        self.PlayerLabel.setText(_translate("EvaluateScore", "Players"))
        self.ScoreLabel.setText(_translate("EvaluateScore", "Score"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EvaluateScore = QtWidgets.QWidget()
    ui = Ui_EvaluateScore()
    ui.setupUi(EvaluateScore)
    EvaluateScore.show()
    sys.exit(app.exec_())
