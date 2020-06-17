"""
    @title: Mysql Flask Connection
    @tag: Python
    @author: Navin Sridhar
    @gh-profile: navins7
"""


import test as TS


def retDBcreds():
    host = "127.0.0.1"
    user = "root"
    passwd = ""
    port = '3306'
    return([host, user, passwd, port])


def addToCompanies(logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        port='3306',
        database="covid"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO company (logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, details) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (logoname, CompanyNames, Locations, Tags,
           int(availableJobs), int(CompanySize), details)
    mycursor.execute(sql, val)
    mydb.commit()


def retrieveCompaniesForHome(tags=None):
    # print("tags =",tags)
    if(tags == None):
        tags = ""
    import mysql.connector
    host, user, passwd, port = retDBcreds()
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port,
        database="covid"
    )
    mycursor = mydb.cursor()
    mycursor.execute(
        "SELECT logoname, CompanyNames, Locations, Tags, availableJobs, CompanySize, id FROM company where Tags like '%"+tags+"%' or Locations like '%"+tags+"%' order by CompanyNames")
    complist = mycursor.fetchall()
    logoname = []
    CompanySize = []
    CompanyNames = []
    Locations = []
    Tags = []
    availableJobs = []
    cid = []
    for x in complist:
        logoname.append(x[0])  # logoname with extn (1.gif etc)
        CompanyNames.append(x[1])  # company name
        Locations.append(x[2])  # location of company
        Tags.append(x[3].split(","))  # tags associated
        availableJobs.append(x[4])  # available number of jobs
        CompanySize.append(x[5])  # size of a company
        cid.append(x[6])  # Primary key of the company

    return(logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs, cid)


def addToProjects(logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize, details):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        port='3306',
        database="covid"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO projects (logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize, details) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (logoname, ProjectNames, Locations, Tags, int(
        availableVacancies), int(ProjectSize), details)
    mycursor.execute(sql, val)
    mydb.commit()


def retrieveProjectsForHome(tags=None):
    import mysql.connector
    # print("tags =",tags)
    if(tags == None):
        tags = ""

    host, user, passwd, port = retDBcreds()
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port,
        database="covid"
    )
    # For performing test with random database sample, comment this during production.
    # TS.run_sql_file('company.sql', mydb, 'projects')

    mycursor = mydb.cursor()
    mycursor.execute("SELECT logoname, ProjectNames, Locations, Tags, availableVacancies, ProjectSize FROM projects  where Tags like '%" +
                     tags+"%' or Locations like '%"+tags+"%' order by ProjectNames")
    projectlist = mycursor.fetchall()
    logoname = []
    ProjectSize = []
    ProjectNames = []
    Locations = []
    Tags = []
    availableVacancies = []
    for x in projectlist:
        logoname.append(x[0])  # logoname with extn (1.gif etc)
        ProjectNames.append(x[1])  # company name
        Locations.append(x[2])  # location of company
        Tags.append(x[3].split(","))  # tags associated
        availableVacancies.append(x[4])  # available number of jobs
        ProjectSize.append(x[5])  # size of a company

    return(logoname, ProjectSize, ProjectNames, Locations, Tags, availableVacancies)


# For Companies information and Job opportunities.

def addTo_OP(id, logoname, job_type, techstack, culture, D_R, description, company_type):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        port='3306',
        database="covid"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO opportunities (id, logoname, job_type, techstack, culture, D_R, description, company_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (int(id), logoname, job_type, techstack,
           culture, D_R, description, company_type)
    mycursor.execute(sql, val)
    mydb.commit()


def retrieveOpportunitiesForHome(cid):
    import mysql.connector

    host, user, passwd, port = retDBcreds()
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port,
        database="covid"
    )

    mycursor = mydb.cursor()
    fetch = "SELECT company.Locations, company.CompanySize, company.details, company.logoname, job_type, techstack, culture, D_R, description, company_type, company.CompanyNames  FROM opportunities,company where opportunities.id ='" + \
        str(cid) + "' AND company.id ='" + str(cid) + "'"
    mycursor.execute(fetch)
    Opportunities = mycursor.fetchall()
    Locations = []
    CompanySize = []
    Details = []
    logoname = []
    Job_Type = []
    TechStack = []
    Culture = []
    D_R = []
    Description = []
    Company_Type = []
    company_name = []

    for x in Opportunities:
        Locations.append(x[0])
        CompanySize.append(x[1])
        Details.append(x[2])
        logoname.append(x[3])
        Job_Type.append(x[4])
        TechStack.append(x[5])
        Culture.append(x[6])
        D_R.append(x[7])
        Description.append(x[8])
        Company_Type.append(x[9])
        company_name.append(x[10])

    return(Locations, CompanySize, Details, logoname, Job_Type, TechStack, Culture, D_R, Description, Company_Type, company_name)


def verifyToken(tok):
    import mysql.connector
    host, user, passwd, port = retDBcreds()
    mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port,
        database="covid")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM token ")
    fetch = mycursor.fetchall()
    for i, j in fetch:
        if j == tok:
            return "Token Valid"

    return "TOken Invalid"

def addToToken(id,token):
    import mysql.connector
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        port='3306',
        database="covid"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO token (id,token) VALUES (%s, %s)"
    val = (int(id),token)
    mycursor.execute(sql, val)
    mydb.commit()    


# Driver for Unit Testing
if __name__ == '__main__':
    # logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs = retrieveCompaniesForHome()
    # print("\n", logoname, "\n", CompanySize, "\n", CompanyNames, "\n", Locations, "\n", Tags, "\n", availableJobs)
    # addToCompanies("4.gif", "Adobe", "Chennai, TN", "Open-source orientation,Very collaborative,Internet Software,AWS,Chef,Kubernetes",2, 5000, "Hello")
    pass
