import sqlite3
import random

class dboperations:
    def __init__(self):
        conn=sqlite3.connect('finances.sqlite')
        self.sql=conn.cursor()
        initscript='''
            CREATE TABLE IF NOT EXISTS Participants(
                Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name VARCHAR2(50) NOT NULL,
                roll NUMBER(2) NOT NULL,
                stream VARCHAR2(50) NOT NULL,
                year NUMBER(50) NOT NULL
            );
        '''
        self.sql.executescript(initscript)

    def enterData(self, name, roll, stream, year):
        self.sql.execute('''
            INSERT INTO Participants(name, roll, stream, year)
            VALUES (?, ?, ?, ?)
        ''',(name, roll, stream, year))
        self.sql.execute('COMMIT')

    def createFixtures(self):
        size=0
        self.sql.execute('SELECT count(*) FROM Participants')
        size=self.sql.fetchone()[0]
        idList=[]
        idList.extend(range(1,size+1))
        random.shuffle(idList)

        fileHandle=open('Fixtures.txt','w')
        numberOfPlayers=size
        num=0

        while numberOfPlayers>=2:
            num=num+1
            if numberOfPlayers==16:
                fileHandle.write('\n -- -- Round of 16 -- -- ')
            elif numberOfPlayers==8:
                fileHandle.write('\n -- -- Quarter Finals -- -- ')
            elif numberOfPlayers==4:
                fileHandle.write('\n -- -- Semi Finals -- -- ')
            elif numberOfPlayers==2:
                fileHandle.write('\n -- -- Final -- -- ')
            else:
                fileHandle.write('\n -- -- Round'+str(num)+' -- --')

            fileHandle.write('\n')
            counter=0

            for i in range(0, int(numberOfPlayers), 2):
                counter=counter+1
                if numberOfPlayers!=2:
                    fileHandle.write('\n -- Match '+str(counter)+' -- \n')
                if num==1:
                    self.sql.execute('SELECT name, stream, year, roll FROM Participants WHERE id = ?', (idList[i], ))
                    row=self.sql.fetchone()
                    participant1 = row[0]+'('+str(row[1])+', Year: '+str(row[2])+', Roll: '+str(row[3])+')'
                    self.sql.execute('SELECT name, stream, year, roll FROM Participants WHERE id = ?', (idList[i+1], ))
                    row=self.sql.fetchone()
                    participant2 = row[0]+'('+str(row[1])+', Year: '+str(row[2])+', Roll: '+str(row[3])+')'
                    fileHandle.write(participant1+'\n    vs   \n'+participant2+'\n')
                else:
                    fileHandle.write('Winner of Match '+str(i+1)+' of previous round \n    vs    \nWinner of Match'+str(i+2)+' of previous round\n')

            numberOfPlayers=numberOfPlayers/2

#Testing block for this class. Does not run if run through launcher.
if __name__=='__main__':
    db=dboperations()
    db.enterData('Sankhanil Nayek', 42, 'BCA', 3)
    db.enterData('Rajashri Naskar', 19, 'BCA', 3)
    db.enterData('Saptangshu Ghosh', 25, 'BCA', 3)
    db.enterData('Abhijit Halder', 69, 'BCA', 3)
    db.createFixtures()