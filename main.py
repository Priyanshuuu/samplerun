"""
    @title: MySQL Flask Driver
    @tag: Python, Flask, Driver, main
    @author: Krishnakanth Alagiri
    @gh-profile: K-Kraken
"""

from flask import Flask, render_template, redirect, url_for, request,session,make_response,flash
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
     import databaseOps as dp
     import random # Only for SQL-Less testing, remove otherwise
     logoname, CompanySize, CompanyNames, Locations, Tags, availableJobs = dp.retrieveCompaniesForHome()
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


@app.route('/admin', methods=['GET', 'POST'])
def tempadmin():
     return render_template(
         'temp-admin.html',
     )



if __name__ == '__main__':
     app.run(host='0.0.0.0', use_reloader=True, debug=True)
