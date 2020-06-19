"""
    @title: Database Testing with Flask Connection
    @tag: Python
    @author: Priyanshu Pandey
    @gh-profile: Priyanshuuu
"""
    
import databaseOps as db
import mysql.connector
import string
import random

def run_sql_file(filename, connection, type):
    '''
    The function takes a filename, connection and type as input
    and will perfrom the SQL query on the given connection with random sample sets.
    '''
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="covid"
    )
    file = open(filename, 'r')
    sql = s = " ".join(file.readlines())

    mycursor = mydb.cursor()
    if type=='company':
        mycursor.execute("DROP TABLE IF EXISTS company;")
        mycursor.execute(sql)

    elif type=='projects':
        mycursor.execute("DROP TABLE IF EXISTS projects;")
        mycursor.execute(sql)

    
    def randomString(stringLength=5):
      letters = string.ascii_lowercase
      return ''.join(random.choice(letters) for i in range(stringLength))

    places = ['Delhi','Kolkata','Hydrabad','Punjab','Chennai', 'Mumbai', 'Pune', 'Banglore']    
    lang = ['Python', 'C++', 'Java', 'Dart', 'Flutter','Kotlin', 'Node.js']
    
    if type=='company':
        for i in range(5):
            db.addToCompanies(str(random.randrange(1, 6, 1))+".gif", randomString(), random.choice(places), '#'+randomString(), random.randrange(1, 10, 1), random.randrange(50, 100, 1),random.choice(lang))
    
    elif type=='projects':
        for i in range(10):
            db.addToProjects(str(random.randrange(1, 6, 1))+".gif", "Project " + str(i+1), random.choice(places), '#'+randomString(), random.randrange(1, 10, 1), random.randrange(5, 10, 1),random.choice(lang))

    
if __name__ == "__main__":
    pass
