from flask import Flask, render_template, redirect, url_for, request,session,make_response,flash
app = Flask(__name__)
# Temp Variables, Change values for testing 
len=6
logoname = []
CompanySize = []

CompanyNames = [
     "World Wildlife Fund",
     "Shell",
     "Adidas",
     "Adobe",
     "Dell",
     "GitHub"
     ]

Locations = [
     "San Francisco, CA", 
     "New York, NY",
     "San Francisco, CA",
     "New York, NY",     
     "San Francisco, CA",
     "New York, NY"
     ]

Tags=[
    ["Clear individual goals", "EQ emphasis", "Work-life balance", "Advertising"],
    ["Open-source orientation", "Flat hierarchy","EQ emphasis", "SaaS", "Big Data"],
    ["Clear individual goals", "SaaS", "EQ emphasis","Flexible working hours", "Big Data"],
    ["Analytics", "EQ emphasis", "Work-life balance", "Health Care"],
    ["Clear individual goals", "EQ emphasis", "Work-life balance", "Advertising"],
    ["Open-source", "Flat hierarchy","EQ emphasis", "SaaS", "Big Data"],
    ["Clear individual goals", "EQ emphasis","Flexible working hours", "Big Data"],
]

availableJobs=[1,2,3,4,5,6]   

@app.route('/', methods=['GET', 'POST'])
def login():
     import random # Only for SQL-Less testing, remove otherwise
     for i in range(1,len+1):
          logoname.append('uploads/logos/'+str(i)+'.gif')
     
     for i in range(1, len+1):
          CompanySize.append(random.randint(1000, 3000))


     return render_template(
          'index.html', 
          len=len, 
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
