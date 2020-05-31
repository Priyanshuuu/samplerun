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

# 404 Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error_pages/404.html'), 404

# Companies Home Page
@app.route('/home', methods=['GET'])
def companies():
     import databaseOps as db
     import random # Only for SQL-Less testing, remove otherwise
     tags = None
     if request.method == 'GET':
          # Tags optionally retrieved from GET
          tags = request.args.get('tags')

     logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs, cid = db.retrieveCompaniesForHome(tags)
     totalSize = len(CompanyNames)

     return render_template(
          'index.html', 
          len=totalSize,
          logoname=logoname, 
          CompanyNames=CompanyNames, 
          Locations=Locations, 
          Tags=Tags, 
          availableJobs=availableJobs,
          CompanySize=CompanySize,
          CompanyId=cid
     )

# Projects Page
@app.route('/projects')
def projects():
     import databaseOps as db
     tags = None
     if request.method == 'GET':
          # Tags optionally retrieved from GET
          tags = request.args.get('tags')

     logoname, ProjectSize, ProjectNames, Locations, Tags, availableVacancies = db.retrieveProjectsForHome(tags)
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
@app.route('/details', methods=["GET", "POST"])
def details():
     import databaseOps as db # details?cid=2
     if request.method == 'GET':
          cid = request.args.get('cid') # Refer PRIMARY KEY (id) for companies and other related table.
     Locations, CompanySize, Details, logoname, Job_Type, TechStack, Culture, D_R, Description , Company_Type, Company_Name = db.retrieveOpportunitiesForHome(cid)
     T_S = list(TechStack[0].split(','))
     D_R = list(map(str.strip, D_R[0].split('. ')))
     Culture = list(map(str.strip, Culture[0].split(',')))
     return render_template('details.html',
          Company_Type=Company_Type[0],
          Locations=Locations[0],
          CompanySize=CompanySize[0],
          Company_Name=Company_Name[0],
          lenT_S=len(T_S),
          TechStack=T_S,
          lenCul=len(Culture),
          Culture=Culture,
          Description=Description[0],
          len_DR=len(D_R),
          D_R=D_R,
          Job_Type=Job_Type,
          len_JT=len(Job_Type),
          logoname=logoname[0],
          Details=Details[0]
          )

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
     from os import system
     # system("cls")
     # app.run(host='0.0.0.0', use_reloader=True, debug=True)
     import webbrowser
     webbrowser.open("http://127.0.0.1:5000/")
     app.run(use_reloader=True, debug=True)

