"""
    @title: Mysql Flask Connection
    @tag: Python
    @author: Navin Sridhar
    @gh-profile: navins7
"""


import test as TS

def addToCompanies(logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details):
  import mysql.connector
  mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="Priyanshu25@",
      port='3306',
      database="covid"
  )
  mycursor = mydb.cursor()
  sql = "INSERT INTO company (logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  val = (logoname, CompanyNames, Locations, Tags, int(availableJobs), int(CompanySize), details)
  mycursor.execute(sql, val)
  mydb.commit()


def retrieveCompaniesForHome():
  import mysql.connector
  mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="Priyanshu25@",
      port='3306',
      database="covid"
      )


  TS.run_sql_file('company.sql', mydb, 'company') # For performing test with random database sample, comment this during production. 

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



def addToProjects(logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize, details):
  import mysql.connector
  mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="Priyanshu25@",
      port='3306',
      database="covid"
  )

  mycursor = mydb.cursor()
  sql = "INSERT INTO projects (logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize, details) VALUES (%s, %s, %s, %s, %s, %s, %s)"
  val = (logoname, ProjectNames, Locations, Tags, int(availableVacancies), int(ProjectSize), details)
  mycursor.execute(sql, val)
  mydb.commit()


def retrieveProjectsForHome():
  import mysql.connector
  mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      passwd="Priyanshu25@",
      port='3306',
      database="covid"
      )
  
  TS.run_sql_file('projects.sql', mydb, 'projects')  # For performing test with random database sample, comment this during production. 

  mycursor = mydb.cursor()
  mycursor.execute("SELECT logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize FROM projects order by ProjectNames")
  projectlist = mycursor.fetchall()
  logoname = []
  ProjectSize = []
  ProjectNames = []
  Locations = []
  Tags = []
  availableVacancies = []
  for x in projectlist:
    logoname.append('uploads/logos/'+x[0])  # logoname with extn (1.gif etc)
    ProjectNames.append(x[1]) # company name
    Locations.append(x[2]) # location of company
    Tags.append(x[3].split(",")) # tags associated
    availableVacancies.append(x[4]) # available number of jobs
    ProjectSize.append(x[5]) # size of a company
  
  return(logoname, ProjectSize, ProjectNames, Locations, Tags, availableVacancies)



# Driver for Unit Testing 
if __name__ == '__main__':
  # logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs = retrieveCompaniesForHome()
  # print("\n", logoname, "\n", CompanySize, "\n", CompanyNames, "\n", Locations, "\n", Tags, "\n", availableJobs)
  addToCompanies("4.gif", "Adobe", "Chennai, TN", "Open-source orientation,Very collaborative,Internet Software,AWS,Chef,Kubernetes",2, 5000, "Hello")
  