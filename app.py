from flask import Flask
from flask import render_template, request, jsonify, url_for, redirect, make_response
import json
import UWSchedulerService

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/loginUser',methods=['POST'])
def loginUser():
     # read the posted values from the UI
    _username = request.form['inputName']
    _password = request.form['inputPassword']
    #validate the received values
    print(_username)
    print(_password)
    if _username and _password:
        return redirect('/search')
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/schedule')
def show_schedule():
  return render_template('schedule.html')

@app.route('/scheduleData')
def formulate_data():
  return data

@app.route('/searchResult', methods=['POST'])
def search_result():
  _subject = str(request.form['subject'])
  _catalogNo = str(request.form['catalogNo'])

  data = []

  getSchedule  = UWSchedulerService.get_course_schedule(subject = _subject, catalog_number = _catalogNo)
  for i in getSchedule:

    info = ''
    days = []
    dayz = ''
    print(i)
    if "T" in i.weekdays:
    	if i.weekdays.count("T") == 1:
    		if i.weekdays.count("h") == 1:
    			days.append("Thursday")
    		else:
    			days.append("Tuesday")
    	if i.weekdays.count("T") == 2:
    		days.append("Tuesday")
    		days.append("Thursday")
    if "W" in i.weekdays:
    	days.append("Wednesday")
    if "F" in i.weekdays:
    	days.append("Friday")
    if "M" in i.weekdays:
    	days.append("Monday")

    first = True;
    for day in days:
    	if first:
    		first = False
    		dayz = dayz + day
    	else:
    		dayz = dayz + ',' + day

    info = i.subject + ' ' + i.catalog_number + ' ' + i.section


    course_info = json.dumps({"title":info, "start_time":i.start_time, "end_time":i.end_time, "days":dayz},sort_keys=True, indent=4)
    data.append(course_info)

  print data



if __name__ == '__main__':
    app.run()