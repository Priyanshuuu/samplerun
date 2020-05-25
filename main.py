"""
    @title: MySQL Flask Driver
    @tag: Python, Flask, Driver, main
    @author: Krishnakanth Alagiri
    @gh-profile: K-Kraken
"""

import time
from flask import Flask, render_template, redirect, url_for, request,session,make_response,flash
from werkzeug.utils import secure_filename
app = Flask(__name__)


def genTimeHash(fname):
     import hashlib
     hash = hashlib.sha1()
     tempstr = (str(fname).encode('utf-8')+str(time.time()).encode('utf-8'))
     hash.update(tempstr)
     return str(hash.hexdigest()[:10])


@app.route('/home', methods=['GET', 'POST'])
def login():
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


@app.route('/admin')
def tempadmin():
     return render_template('temp-admin.html')


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



if __name__ == '__main__':
     import webbrowser
     #webbrowser.open("http://127.0.0.1:5000/home")
     app.run(host='0.0.0.0', use_reloader=True, debug=True)
     #app.run(use_reloader=True, debug=True)
