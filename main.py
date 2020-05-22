"""
    @title: MySQL Flask Driver
    @tag: Python, Flask, Driver, main
    @author: Krishnakanth Alagiri
    @gh-profile: K-Kraken
"""

import time
from flask import Flask, render_template, redirect, url_for, request,session,make_response,flash
from werkzeug import secure_filename
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


@app.route('/admin')
def tempadmin():
     return render_template('temp-admin.html')


@app.route('/adminuploader', methods=['GET', 'POST'])
def adminupload():
     if request.method == 'POST':
          import databaseOps as db
          # logoname = request.logoname
          f = request.files['file']
          logoname = genTimeHash(str(f.filename))
          # app.config['UPLOAD_FOLDER']="static/uploads/logos/"
          app.config['UPLOAD_FOLDER'] = "U://Users//Krishna_Alagiri//Projects//Web//Scolarly_Science//COVID-Opportunities//static//uploads//logos"
          f.save(app.config['UPLOAD_FOLDER'], logoname)
          CompanyName = request.form['CompanyName']
          Location = request.form['Location']
          Tags = request.form['Tags']
          availableJobs = request.form['availableJobs']
          CompanySize = request.form['CompanySize']
          details = request.form['details']
          #try:
          db.addToCompanies(logoname, CompanyName, Location, Tags, availableJobs, CompanySize, details)
          return 'Entry successful'
          #except:
          #     return 'Entry unsuccessful'



if __name__ == '__main__':
     app.run(host='0.0.0.0', use_reloader=True, debug=True)
