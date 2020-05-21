"""
    @title: Mysql Flask Connection
    @tag: Python
    @author: Navin Sridhar
    @gh-profile: navins7
"""

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="covid"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM company")

complist = mycursor.fetchall()
logoname = []
CompanySize = []
CompanyNames = []
Locations = []
Tags=[]
idi=[]
availableJobs=[]
lenq=[]
for x in complist:

  idi.append(x[0])
  lenq.append(x[1])
  logoname.append(x[2])
  CompanyNames.append(x[3])
  Locations.append(x[4])
  Tags.append(x[5])
  availableJobs.append(x[6])
  CompanySize.append(x[7])
  
  #print(idi)
  
  
 
  