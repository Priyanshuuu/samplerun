"""
    @title: MySQL Flask Driver
    @tags: Python, Flask, Driver, main
    @author: Krishnakanth Alagiri
    @gh-profile: K-Kraken
    @gh-repo-url: https://github.com/scholarly-science/COVID-Opportunities/
"""

import time
from flask import Flask, render_template, redirect, url_for, request,session,make_response,flash
app = Flask(__name__)


# Companies Home Page
@app.route('/home', methods=['GET'])
def companies():
     import databaseOps as db
     import random # Only for SQL-Less testing, remove otherwise
     logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs = db.retrieveCompaniesForHome()
     totalSize = len(CompanyNames)

     return render_template(
          'index.html', 
          len=totalSize,
          logoname=logoname, 
          CompanyNames=CompanyNames, 
          Locations=Locations, 
          Tags=Tags, 
          availableJobs=availableJobs,
          CompanySize=CompanySize
     )

# Projects Page
@app.route('/projects')
def projects():
     import databaseOps as db
     logoname, ProjectSize, ProjectNames, Locations, Tags, availableVacancies = db.retrieveProjectsForHome()
     totalSize = len(ProjectNames)

     return render_template(
          'projects.html', 
          len=totalSize,
          logoname=logoname, 
          ProjectNames=ProjectNames, 
          Locations=Locations, 
          Tags=Tags, 
          availableVacancies=availableVacancies,
          ProjectSize=ProjectSize
     )

# Details Pages; Where companies individual Informations are shows 
@app.route('/details', methods=['GET'])
def details():
     if request.method == 'GET':
          cid = request.args.get('cid') # Refer PRIMARY KEY (id) for companies and other related tables
          print(cid)
     return render_template('details.html')

# Temporary Data Entry Page
@app.route('/admin')
def tempadmin():
     return render_template('temp-admin.html')

# Validate and pushes information to the db
@app.route('/adminuploader', methods=['GET', 'POST'])
def adminupload():
     if request.method == 'POST':
          import databaseOps as db
          logoname = request.form['logoname']
          CompanyName = request.form['CompanyName']
          Location = request.form['Location']
          Tags = request.form['Tags']
          availableJobs = request.form['availableJobs']
          CompanySize = request.form['CompanySize']
          details = request.form['details']
          try:
               db.addToCompanies(logoname, CompanyName, Location, Tags, availableJobs, CompanySize, details)
               return 'Entry successful'
          except:
               return 'Entry unsuccessful'

# Driver Code
if __name__ == '__main__':
     app.run(host='0.0.0.0', use_reloader=True, debug=True)
