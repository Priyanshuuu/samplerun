"""
    @title: Mysql Flask Connection
    @tag: Python
    @author: Navin Sridhar
    @gh-profile: navins7
"""


import mysql.connector


def addToCompanies(logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details):
  mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="",
      database="covid"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO company (logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details) VALUES (%s, %s, %s, %s, int(%s), int(%s), %s)"
  val = (logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details)
  mycursor.execute(sql, val)

  mydb.commit()




def retrieveCompaniesForHome():
  import mysql.connector
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="covid"
  )

  mycursor = mydb.cursor()
  mycursor.execute("SELECT logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize FROM company order by CompanyNames")
  complist = mycursor.fetchall()
  logoname = []
  CompanySize = []
  CompanyNames = []
  Locations = []
  Tags = []
  availableJobs = []
  for x in complist:
    logoname.append('uploads/logos/'+x[0])  # logoname with extn (1.gif etc)
    CompanyNames.append(x[1]) # company name
    Locations.append(x[2]) # location of company
    Tags.append(x[3].split(",")) # tags associated
    availableJobs.append(x[4]) # available number of jobs
    CompanySize.append(x[5]) # size of a company
  
  return(logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs)

# Driver for Unit Testing 
if __name__ == '__main__':
  # logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs = retrieveCompaniesForHome()
  # print("\n", logoname, "\n", CompanySize, "\n", CompanyNames, "\n", Locations, "\n", Tags, "\n", availableJobs)

  addToCompanies("4.gif", "Adobe", "Chennai, TN", "Open-source orientation,Very collaborative,Internet Software,AWS,Chef,Kubernetes",
                 2, 5000, "Hello")
