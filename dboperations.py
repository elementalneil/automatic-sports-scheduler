import sqlite3

class dboperations:
    def __init__(self):
        conn=sqlite3.connect('finances.sqlite')
        self.sql=conn.cursor()
        initscript='''
            CREATE TABLE IF NOT EXISTS Participants(
                name VARCHAR2(50) NOT NULL,
                roll NUMBER(2) NOT NULL,
                stream VARCHAR2(50) NOT NULL,
                year NUMBER(50) NOT NULL,
                PRIMARY KEY(stream, year, roll)
            );
        '''
        self.sql.executescript(initscript)

    def enterData(self, name, roll, stream, year):
        self.sql.execute('''
            INSERT INTO Participants(name, roll, stream, year)
            VALUES (?, ?, ?, ?)
        ''',(name, roll, stream, year))
        self.sql.execute('COMMIT')

#Testing block for this class. Does not run if run through launcher.
if __name__=='__main__':
    db=dboperations()
    db.enterData('Sankhanil Nayek', 42, 'BCA', 3)
    db.enterData('Rajashri Naskar', 19, 'BCA', 3)
    db.enterData('Saptangshu Ghosh', 25, 'BCA', 3)
    db.enterData('Abhijit Halder', 69, 'BCA', 3)