#This File Contains Most Of The Common Functions Used In Fantasy Cricket League Project(Final Assignment Project Of Internshala Programming With Python Training)
#____________________________________________________________________________________
#Establishing Connection To Database
import sqlite3
db=sqlite3.connect('data.db')
cur=db.cursor()
#_____________________________________________________________________________________
#Function To Get List Of All Team Names

def getTeams():
    cur.execute("select name from teams")    #SQL Query
    teams=cur.fetchall()                     #Get List Of All Tuples Of Team Names
    teams_list=[]                            #Empty List
    for team in teams:
        teams_list.append(team[0])           #Add First Element Of Each Tuple To List
    return teams_list                        #List of All Team Names
#____________________________________________________________________________________
#Function To Get List Of All Team Members Of Given Team

def getTeamMembers(team):
    cur.execute("select players from teams where name='"+team+"';")     #SQL Query
    teamPlayers=cur.fetchone()                                          #Get All Player Names Seperated By A Comma(,)
    teamPlayersList=teamPlayers[0].split(',')                            #Splitting All Names Individually To Make List
    teamPlayersList.remove("")                                          #To Remove The Last Element Which Is Empty (Nothiing After ,)
    return teamPlayersList                                              #List Of All Team Members Of Team
#____________________________________________________________________________________ 
#Function To Get Score Of A Player Based On Criteria In Problem Statment    

def calculatePlayerScore(player,match):

    #To Get Players Records In Given Match

    cur.execute("select * from "+match+" where player='"+player+"';")   #SQL Query
    playerRecord=cur.fetchone()                                         #Getting Players Records

    #Calculating Batting Score Of Player Based On Criteia In Problem Statment

    batScore=int(playerRecord[1]/2)                                     # playerRecord[1]=Runs Scored By Player
    if batScore>=50: batScore+=5
    if batScore>=100: batScore+=10
    if playerRecord[1]>0:
        strikeRate=playerRecord[1]/playerRecord[2]                      #playerRecord[2]=Balls Faced By Player
        if strikeRate>=80 and strikeRate<100: batScore+=2
        if strikeRate>=100:batScore+=4
    batScore=batScore+playerRecord[3]                                   #playerRecord[3]=Fours (Boundary)
    batScore=batScore+2*playerRecord[4]                                 #playerRecord[4]=Sixes (Boundary)

    #Calculating Bowling Score Of Player Based On Criteia In Problem Statment
    bowlScore=playerRecord[8]*10                                        #playerRecord[8]=Wickets Taken By Bowler
    if playerRecord[8]>=3: bowlScore=bowlScore+5
    if playerRecord[8]>=5: bowlScore=bowlScore=bowlScore+10
    if playerRecord[7]>0:                                               #playerRecord[7]=Runs Given By Bowler
        economyRate=6*playerRecord[7]/playerRecord[5]                   #playerRecord[5]=Balls Bowled By Bowler
        if economyRate<=2: bowlScore=bowlScore+10
        if economyRate>2 and economyRate<=3.5: bowlScore=bowlScore+7
        if economyRate>3.5 and economyRate<=4.5: bowlScore=bowlScore+4

    #Calculating Fielding Score Of Player Based On Criteia In Problem Statment
    fieldScore=(playerRecord[9]+playerRecord[10]+playerRecord[11])*10   #Catches+Stumpings+Run Outs Respectively         

    #Adding Up Above Scores To Get Final Score
    totalScore=batScore+bowlScore+fieldScore
    return totalScore
            
#____________________________________________________________________________________ 
#Function To Get Players Value 
def getPlayerValue(player):
    cur.execute("select value from stats where player='"+player+"';")
    playerValue=cur.fetchone()
    return playerValue[0]

#____________________________________________________________________________________
#Function To Get Whole team Value
def getTeamValue(team):
    cur.execute("select value from teams where name='"+team+"';")
    teamValue=cur.fetchone()
    return teamValue[0]

#____________________________________________________________________________________
#Function To Get All Players List Of Certain Category
def getAllPlayerList(category):
    cur.execute("select player from stats where ctg='"+category+"';")
    playerList=cur.fetchall()
    return playerList

#____________________________________________________________________________________                              
#Function To Get Player Category
def getPlayerCategory(player):
        cur.execute("select ctg from stats where player='"+player+"';")
        category=cur.fetchone()
        return category[0]

#____________________________________________________________________________________                              
#Function To insert Team along with its value

def insertTeam(team,players,value):
    try:
        cur.execute("Insert or Replace into teams (name,players,value) values ('"+team+"','"+players+"','"+str(value)+"');")
        db.commit()
    except:
        db.rollback()
























