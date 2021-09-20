# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_cricket-league.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox     #To Display Message Box
import functions                            #To Import Various functions Used Here
import images_rc                            #To Import Images Used In This Programm



class Ui_MainWindow(object):
    #Initialize Paramenters Displayed On Application Interface
    def __init__(self):
        self.nameOfTeam=None
        self.batsmans=0
        self.bowlers=0
        self.allRounders=0
        self.wicketKeepers=0
        self.availablePoints=1000
        self.usedPoints=0
        self.previousSelectedCategory="No"

    #function Created By QtDesigner Containing Whole Code To Create GUI Inteface
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1316, 941)
        MainWindow.setMinimumSize(QtCore.QSize(1137, 814))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/windowicon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("border-image: url(:/img/cricket-championship-background_23-2147941320.jpg);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("border-image: url;\n"
        "background-color: rgb(0, 255, 0, 100);")
        self.widget.setObjectName("widget")

        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.allRounderImage = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.allRounderImage.setFont(font)
        self.allRounderImage.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 15pt \"Segoe UI Black\";border-image: url(:/img/22829478_859957697500481_6317122602704678758_o-removebg-preview-removebg-preview.png);")
        self.allRounderImage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.allRounderImage.setObjectName("allRounderImage")
        self.gridLayout.addWidget(self.allRounderImage, 0, 6, 2, 1)

        self.batsmanImage = QtWidgets.QLabel(self.widget)
        self.batsmanImage.setStyleSheet("border-image: url(:/img/pngkey.com-cricketer-png-2595812.png);\n"
        "background-color: rgb(0, 255, 127,0);\n"
        "font: 87 17pt \"Segoe UI Black\";")
        self.batsmanImage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.batsmanImage.setObjectName("batsmanImage")
        self.gridLayout.addWidget(self.batsmanImage, 0, 0, 2, 1)

        self.wicketKeeperImage = QtWidgets.QLabel(self.widget)
        self.wicketKeeperImage.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 15pt \"Segoe UI Black\";\n"
        "border-image: url(:/img/564421.jpg);\n"
        "border-bottom-color: rgb(0, 0, 255);\n"
        "border-image: url(:/img/cricket-wicket-keeper-cricket-wicket-keeper-catching-cricket-ball-with-wicket-in-background-eps-vector_csp48181988-removebg-preview.png);")
        self.wicketKeeperImage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.wicketKeeperImage.setObjectName("wicketKeeperImage")
        self.gridLayout.addWidget(self.wicketKeeperImage, 0, 4, 2, 1)

        self.noOfBowler = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.noOfBowler.setFont(font)
        self.noOfBowler.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 24pt \"Segoe UI Black\";\n"
        "font: 72pt \"Snap ITC\";;border-image: url;")
        self.noOfBowler.setAlignment(QtCore.Qt.AlignCenter)
        self.noOfBowler.setObjectName("noOfBowler")
        self.gridLayout.addWidget(self.noOfBowler, 1, 3, 1, 1)

        self.bowlerImage = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.bowlerImage.setFont(font)
        self.bowlerImage.setStyleSheet("background-color: rgb(0, 255, 127,0);\n"
        "border-image: url(:/img/20518809-removebg-preview.png);\n"
        "font: 87 17pt \"Segoe UI Black\";")
        self.bowlerImage.setScaledContents(True)
        self.bowlerImage.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.bowlerImage.setObjectName("bowlerImage")
        self.gridLayout.addWidget(self.bowlerImage, 0, 2, 2, 1)

        self.noOfAllRounders = QtWidgets.QLabel(self.widget)
        self.noOfAllRounders.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 24pt \"Segoe UI Black\";\n"
        "font: 72pt \"Snap ITC\";border-image: url;")
        self.noOfAllRounders.setAlignment(QtCore.Qt.AlignCenter)
        self.noOfAllRounders.setObjectName("noOfAllRounders")
        self.gridLayout.addWidget(self.noOfAllRounders, 1, 7, 1, 1)
        self.noOfWIcketKeeper = QtWidgets.QLabel(self.widget)
        self.noOfWIcketKeeper.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 24pt \"Segoe UI Black\";\n"
        "font: 72pt \"Snap ITC\";border-image: url;")
        self.noOfWIcketKeeper.setAlignment(QtCore.Qt.AlignCenter)
        self.noOfWIcketKeeper.setObjectName("noOfWIcketKeeper")
        self.gridLayout.addWidget(self.noOfWIcketKeeper, 1, 5, 1, 1)

        self.noOfBatsman = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(72)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.noOfBatsman.setFont(font)
        self.noOfBatsman.setStyleSheet("background-color: rgb(0, 255, 127,0);font: 87 24pt \"Segoe UI Black\";\n"
        "font: 72pt \"Snap ITC\";\n"
        "border-image: url;")
        self.noOfBatsman.setAlignment(QtCore.Qt.AlignCenter)
        self.noOfBatsman.setObjectName("noOfBatsman")
        self.gridLayout.addWidget(self.noOfBatsman, 0, 1, 2, 1)
        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("\n"
        "border-image: url;")
        self.widget_2.setObjectName("widget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.pointsAvailable = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pointsAvailable.setFont(font)
        self.pointsAvailable.setStyleSheet("border-image: url;\n"
        "font: 20pt \"Franklin Gothic Demi Cond\";\n"
        "background-color: rgb(227, 227, 227);")
        self.pointsAvailable.setScaledContents(True)
        self.pointsAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.pointsAvailable.setWordWrap(False)
        self.pointsAvailable.setIndent(0)
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.gridLayout_2.addWidget(self.pointsAvailable, 2, 0, 1, 1)

        self.pointsUsed = QtWidgets.QLabel(self.widget_2)
        self.pointsUsed.setMinimumSize(QtCore.QSize(407, 54))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Demi Cond")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pointsUsed.setFont(font)
        self.pointsUsed.setStyleSheet("font: 20pt \"Franklin Gothic Demi Cond\";border-image: url;\n"
        "background-color: rgb(227, 227, 227);")
        self.pointsUsed.setScaledContents(True)
        self.pointsUsed.setAlignment(QtCore.Qt.AlignCenter)
        self.pointsUsed.setWordWrap(False)
        self.pointsUsed.setIndent(0)
        self.pointsUsed.setObjectName("pointsUsed")
        self.gridLayout_2.addWidget(self.pointsUsed, 2, 2, 1, 1)

        self.teamName = QtWidgets.QLabel(self.widget_2)
        self.teamName.setMinimumSize(QtCore.QSize(407, 76))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.teamName.setFont(font)
        self.teamName.setStyleSheet("border-image: url;\n"
        "font: 87 18pt \"Segoe UI Black\";")
        self.teamName.setAlignment(QtCore.Qt.AlignCenter)
        self.teamName.setObjectName("teamName")
        self.gridLayout_2.addWidget(self.teamName, 3, 2, 1, 1)

        self.fantasy_cricket_league_image = QtWidgets.QLabel(self.widget_2)
        self.fantasy_cricket_league_image.setStyleSheet("border-image: url(:/img/Programming with 21511.png);")
        self.fantasy_cricket_league_image.setText("")
        self.fantasy_cricket_league_image.setWordWrap(False)
        self.fantasy_cricket_league_image.setIndent(0)
        self.fantasy_cricket_league_image.setObjectName("fantasy_cricket_league_image")
        self.gridLayout_2.addWidget(self.fantasy_cricket_league_image, 2, 1, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.batsmanCategory = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.batsmanCategory.setFont(font)
        self.batsmanCategory.setStyleSheet("border-image: url;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/clipart-ball-cricket-bat-11.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.batsmanCategory.setIcon(icon1)
        self.batsmanCategory.setIconSize(QtCore.QSize(30, 61))
        self.batsmanCategory.setObjectName("batsmanCategory")
        self.horizontalLayout.addWidget(self.batsmanCategory)

        self.bowlersCategory = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.bowlersCategory.setFont(font)
        self.bowlersCategory.setStyleSheet("border-image: url;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/cricket-clipart-cricket-captain-15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bowlersCategory.setIcon(icon2)
        self.bowlersCategory.setIconSize(QtCore.QSize(38, 38))
        self.bowlersCategory.setObjectName("bowlersCategory")
        self.horizontalLayout.addWidget(self.bowlersCategory)

        self.wicketKeeperCategory = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.wicketKeeperCategory.setFont(font)
        self.wicketKeeperCategory.setStyleSheet("border-image: url;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/clipart-bat-cricket-stump-15.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wicketKeeperCategory.setIcon(icon3)
        self.wicketKeeperCategory.setIconSize(QtCore.QSize(75, 59))
        self.wicketKeeperCategory.setObjectName("wicketKeeperCategory")
        self.horizontalLayout.addWidget(self.wicketKeeperCategory)

        self.allRounderCategory = QtWidgets.QRadioButton(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        self.allRounderCategory.setFont(font)
        self.allRounderCategory.setStyleSheet("border-image: url;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/bat-clipart-boll-19.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.allRounderCategory.setIcon(icon4)
        self.allRounderCategory.setIconSize(QtCore.QSize(56, 76))
        self.allRounderCategory.setObjectName("allRounderCategory")
        self.horizontalLayout.addWidget(self.allRounderCategory)
        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.teamPlayersList = QtWidgets.QListWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(16)
        font.setBold(True)
        self.teamPlayersList.setFont(font)
        self.teamPlayersList.setStyleSheet("background-color: rgb(227, 227, 227);\n"
        "")
        self.teamPlayersList.setIconSize(QtCore.QSize(40, 43))
        self.teamPlayersList.setObjectName("teamPlayersList")
        self.gridLayout_2.addWidget(self.teamPlayersList, 4, 2, 2, 1)

        spacerItem = QtWidgets.QSpacerItem(411, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 1, 1, 1)

        self.availablePlayersList = QtWidgets.QListWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.availablePlayersList.setFont(font)
        self.availablePlayersList.setStyleSheet("\n"
        "background-color: rgb(227, 227, 227);")
        self.availablePlayersList.setIconSize(QtCore.QSize(78, 85))
        self.availablePlayersList.setObjectName("availablePlayersList")
        self.gridLayout_2.addWidget(self.availablePlayersList, 4, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1316, 56))
        self.menubar.setStyleSheet("background-color: rgb(0, 0, 0);\n"
        "font: 87 22pt \"Segoe UI Black\";\n"
        "selection-color: rgb(255, 170, 0);\n"
        "selection-background-color: rgb(0, 85, 255);\n"
        "color: rgb(255, 255, 255);\n"
        "")

        self.menubar.setObjectName("menubar")
        self.menuManage = QtWidgets.QMenu(self.menubar)
        self.menuManage.setObjectName("menuManage")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionEvaluate = QtWidgets.QAction(MainWindow)
        self.actionEvaluate.setObjectName("actionEvaluate")
        self.menuManage.addAction(self.actionNew)
        self.menuManage.addAction(self.actionEdit)
        self.menuManage.addAction(self.actionSave)
        self.menuManage.addAction(self.actionEvaluate)
        self.menuManage.addSeparator()
        self.menubar.addAction(self.menuManage.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


#___________________________________________________________________________________
        #Radio Buttons Event Handler 
        self.batsmanCategory.clicked.connect(self.category)
        self.bowlersCategory.clicked.connect(self.category)
        self.allRounderCategory.clicked.connect(self.category)
        self.wicketKeeperCategory.clicked.connect(self.category)

        #List Widget Event Handler
        self.availablePlayersList.itemDoubleClicked.connect(self.addPlayerToTeam)
        self.teamPlayersList.itemDoubleClicked.connect(self.removePlayerFromTeam)

        #Menu Bar Event Handler
        self.menuManage.triggered[QtWidgets.QAction].connect(self.menu)

        #To Display All Widgets Along With Their Values
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
#________________________________________________________________________________________________________
    #function to perform menu bar option Manage
    def menu(self,action):
        option=action.text()        #Gives text of option clicked

        #if New option is Clicked
        if option=='New Team':           #If option selected is new team that means new team is to be created 
            ok=True                 
            while ok:               #Loop until correct team name is entered
                text, ok=QtWidgets.QInputDialog.getText(MainWindow, "Team", "Enter name of team:")#Dialog Box To Get Team Name
                if ok:
                    teams=functions.getTeams()                                                           #Get all Team Names
                    if text in teams:
                        self.showDialog("Team Name Alredy Exist","Error","Please Enter Another Team Name Or You Can Edit Existing Team")#Error Dialog If Team Name Already Exist
                    elif self.validateName(text)==True:    #Checks if Team Name Entered is correct or not
                        self.__init__()                     #Initialize All Variable For New Team
                        self.clearLists()                  #Clears Both Displayed Lists
                        self.displayAvailablePlayerList(self.radioButtonClickedName())       #Display List 1 Element As Per Category Without Including teamPlayer
                        self.nameOfTeam=text                        #set Team Name to New Team Name
                        self.retranslateUi(MainWindow)      #Display All Elements As per new values
                        break
                

        #if Save Option is Clicked
        if option=='Save Team':

            if self.teamPlayersList.count()==11:     #If 11 Players Are Choosen Then Save 
                self.saveTeam()
            else:
                self.showDialog("Insufficient Players","Error","Total 11 Players Should Be There!!!Add More")

        #if Edit option is choosen
        if option=='Open Team':
            teams = functions.getTeams()        #Get All Team Names To Display in Widget so that user can select which team to delete
            team, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",teams)#Display Item Dialog Widget Box
            if ok:
                self.__init__() 
                self.clearLists()
                self.nameOfTeam=team
                
                teamPlayers=functions.getTeamMembers(team)
                
                for player in teamPlayers:  #Loop To Addd All Team Players To teamPlayerList
                    self.addItem("teamPlayersList",player)
                self.displayAvailablePlayerList(self.radioButtonClickedName())
                self.usedPoints=functions.getTeamValue(team)#Points Used Should Get The Teams Value 
                self.availablePoints=1000-self.usedPoints#Remaining Points Are Subtaracted From Total Points
                
                for i in range(self.teamPlayersList.count()):           #Updating values Of Displayed Variables As Per Their Category And Value
                    player=self.teamPlayersList.item(i).text()
                    ctgr=functions.getPlayerCategory(player)
                    self.updatePlayerCategoryValue(ctgr,'increment')
                self.retranslateUi(MainWindow)

        #if Evaluate Option is Choosen
        if option=='Evaluate Team':
            from evaluate_score import Ui_EvaluateScore
            Dialog = QtWidgets.QDialog()
            ui = Ui_EvaluateScore()
            ui.setupUi(Dialog)
            ret=Dialog.exec()
            
#________________________________________________________________________________________________________
     #function To Convert All Team Player List To String So That It Can Be Stored In Database   
    def convertTeamPlayersListToString(self):
        stringList=""
        for player in range(self.teamPlayersList.count()):
            stringList+=self.teamPlayersList.item(player).text()+","
        return stringList
    
#________________________________________________________________________________________________________
     #function That Stores Team Player String To Database       
    def saveTeam(self):
        player_list=str(self.convertTeamPlayersListToString())
        try:
            functions.insertTeam(self.nameOfTeam,player_list,self.usedPoints)
            self.showDialog("Team Saved Succesfully","Information","")
        except:
            self.showDialog("SQL Error!!!!!!!!","Error","")

#________________________________________________________________________________________________________
    #function to Clear Both Lists     
    def clearLists(self):
        self.availablePlayersList.clear()
        self.teamPlayersList.clear()

#________________________________________________________________________________________________________
    #Returns The Category As Per Radio Button Clicked   
    def radioButtonClickedName(self):
        category="None"
        if self.batsmanCategory.isChecked()==True:category='BAT'
        if self.bowlersCategory.isChecked()==True:category='BWL'
        if self.allRounderCategory.isChecked()==True:category='AR'
        if self.wicketKeeperCategory.isChecked()==True:category='WK'
        return category

#________________________________________________________________________________________________________
    #function That Validates The Team Name Entered Is Correct Or Not
    def validateName(self,name):
        if name==None:
            self.showDialog("No Team Selected","Error","Please Add A New Team Or Open A Existing Team")
            return False
        elif name.isalnum()==False:
            self.showDialog("Invalid Team Name","Error","Team Name Should Cotain Only AlphaNumeric Characters")
        else:
            return True

#________________________________________________________________________________________________________
    #function To Check If Same Previous Radio Button Is Clicked Or Not (Just To Save Execution Time)
    def category(self):
        category=self.radioButtonClickedName()#Get New Clicked Value And Compare To Previous Clicked Button
        if self.previousSelectedCategory==category:
            return
        else:
            self.displayAvailablePlayerList(category)#If New Button Clicked Go To displayAvailablePlayerList Else Nothing

#________________________________________________________________________________________________________
    #function To Get The Appropriate Category Icon
    def getCategoryIcon(self,category):
        icon = QtGui.QIcon()#Set Icon Variable
        if category=="BAT":icon.addPixmap(QtGui.QPixmap(":img/bat - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#Assigning Image To Icon Variable
        if category=="BWL":icon.addPixmap(QtGui.QPixmap(":img/cricket-ball-icon-260nw-753632899-removebg-preview - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if category=="AR":icon.addPixmap(QtGui.QPixmap(":img/cricket-bat-and-ball-icon-simple-style-vector-7899508-removebg-preview - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        if category=="WK":icon.addPixmap(QtGui.QPixmap(":img/clipart-ball-cricket-bat-19 - Copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        return icon#Returns Icon 

#________________________________________________________________________________________________________
    #function To Add Player To Either Of The Lists
    def addItem(self,listWidget,text):
        category=functions.getPlayerCategory(text)#Gets The Category Of Player
        icon=self.getCategoryIcon(category)#Gets The Appropriate Icon For Player
        sur=QtWidgets.QListWidgetItem()#Make A List Element
        sur.setText(str(text))#Set Player Name As Text Of That Element
        if listWidget=="availablePlayersList":self.availablePlayersList.addItem(sur)#Add Item To Appropriate List
        if listWidget=="teamPlayersList":self.teamPlayersList.addItem(sur)
        sur.setIcon(icon)#Set Icon To The Element

#________________________________________________________________________________________________________
    #function To Display List Of Players Remaining As Per Category In avaiablePlayerList
    def displayAvailablePlayerList(self,category):
        self.availablePlayersList.clear()#Clears Available Player List To Create Space For New Category Players
        playerList=functions.getAllPlayerList(category)
        for player in playerList:                           #Loop To Confirm Only Player Which Are Not In teamPlayerList are displyed 
            selectedPlayerList=[]
            for count in range(self.teamPlayersList.count()):selectedPlayerList.append(self.teamPlayersList.item(count).text())
            if player[0] not in selectedPlayerList:self.addItem("availablePlayersList",player[0])
        self.previousSelectedCategory=category#Set Previous Category With New Category

#________________________________________________________________________________________________________
    #function To Remove Element From availablePlayerList To teamPlayerList with Updation
    def addPlayerToTeam(self,item):
        if self.validateName(self.nameOfTeam)==True:#If Correct And Certain Team Is Selected
            ctg=self.radioButtonClickedName()
            if self.validateTeamPlayerList(item,ctg)==True:
                self.addItem("teamPlayersList",item.text())
                self.availablePlayersList.takeItem(self.availablePlayersList.row(item))
                self.retranslateUi(MainWindow)

#________________________________________________________________________________________________________
    #function To Remove Element From teamPlayerList To availablePlayerList with Updation
    def removePlayerFromTeam(self,item):
        self.teamPlayersList.takeItem(self.teamPlayersList.row(item))
        playerValue=functions.getPlayerValue(item.text())#Updating Available Points
        self.availablePoints+=int(playerValue)
        self.usedPoints-=int(playerValue)
        category=functions.getPlayerCategory(item.text())
        if category==self.radioButtonClickedName():self.addItem("availablePlayersList",item.text())#Current Selected Category Displayed At That Instant Only
        self.updatePlayerCategoryValue(category,"decrement")#Decrement values Since Player Removed
        self.retranslateUi(MainWindow)
    
#________________________________________________________________________________________________________
    #function To Update Category Value Based On They Are Added To teamPlayerList Or Removed
    def updatePlayerCategoryValue(self,category,operation):
        if operation=='increment':add=1
        elif operation=='decrement':add=-1
        if category=='BAT':self.batsmans+=add
        if category=='BWL':self.bowlers+=add
        if category=='WK':self.wicketKeepers+=add
        if category=='AR':self.allRounders+=add  

#________________________________________________________________________________________________________
    #function To Validate All The Parameters Displayed Correct Or Not    
    def validateTeamPlayerList(self,item,category):
        msg=''

        #Checking If Number Of Players Getting More Than 11 As Well As Particular Cateogry
        if self.teamPlayersList.count()>=11:msg="Cannot Add More Than 11 Players"
        else:
            if category=='BAT' and self.batsmans>=4:msg="Batsman Not More Than 4"
            if category=='BWL' and self.bowlers>=3:msg="Bowlers Not More Than 3"
            if category=='AR' and self.allRounders>=3:msg="All Rounders Not More Than 3"
            if category=='WK' and self.wicketKeepers>=1:msg="Wicket Keepers Not More Than 1"
        if msg!='':
            self.showDialog(msg,"Error","")
            return False

        #To Check If You Have Sufficient Point To Add A Player Or Not
        playerValue=functions.getPlayerValue(item.text())
        if self.availablePoints-int(playerValue)<0:
            self.showDialog("Insufficient Points","Error","Value Of {} is {} But You Have {} Points Only".format(item.text(),int(playerValue),self.availablePoints))
            return False
        self.updatePlayerCategoryValue(category,'increment')
        self.availablePoints-=int(playerValue)
        self.usedPoints+=int(playerValue)
        return True

    
#________________________________________________________________________________________________________    
    #function to display a dialog box with certain information or error message
    def showDialog(self,message,title,details):
       msg = QtWidgets.QMessageBox()
       if title=="Error":msg.setIcon(QMessageBox.Critical)
       if title=="Information":msg.setIcon(QMessageBox.Information)
       msg.setText(message)
       msg.setWindowTitle("Fantasy Cricket League")
       msg.setDetailedText(details)
       msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
       retval = msg.exec()

#________________________________________________________________________________________________________
#function Containing All Widget Elemets Along With Their Texts (Generated By Qt Designer)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket League"))
        self.allRounderImage.setText(_translate("MainWindow", "All-ROunder"))
        self.batsmanImage.setText(_translate("MainWindow", "Batsman"))
        self.wicketKeeperImage.setText(_translate("MainWindow", "Wicket-Keeper"))
        self.noOfBowler.setText(_translate("MainWindow", "{}".format(self.bowlers)))
        self.bowlerImage.setText(_translate("MainWindow", "Bowler"))
        self.noOfAllRounders.setText(_translate("MainWindow", "{}".format(self.allRounders)))
        self.noOfWIcketKeeper.setText(_translate("MainWindow", "{}".format(self.wicketKeepers)))
        self.noOfBatsman.setText(_translate("MainWindow", "{}".format(self.batsmans)))
        self.pointsAvailable.setText(_translate("MainWindow", "Points Available:-   {}".format(self.availablePoints)))
        self.pointsUsed.setText(_translate("MainWindow", "Points Used:-  {} ".format(self.usedPoints)))
        self.teamName.setText(_translate("MainWindow", "Team Name:-{}".format(self.nameOfTeam)))
        self.batsmanCategory.setText(_translate("MainWindow", "BAT"))
        self.bowlersCategory.setText(_translate("MainWindow", "BWL"))
        self.wicketKeeperCategory.setText(_translate("MainWindow", "WK"))
        self.allRounderCategory.setText(_translate("MainWindow", "AR"))
        self.menuManage.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew.setText(_translate("MainWindow", "New Team"))
        self.actionNew.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionEdit.setText(_translate("MainWindow", "Open Team"))
        self.actionEdit.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionSave.setText(_translate("MainWindow", "Save Team"))
        self.actionSave.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionEvaluate.setText(_translate("MainWindow", "Evaluate Team"))
        self.actionEvaluate.setShortcut(_translate("MainWindow", "Alt+E"))

   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
