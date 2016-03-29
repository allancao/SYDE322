from flask import Flask
from flask import request, render_template, jsonify, url_for, redirect, make_response
import json
import pickle
import UWSchedulerService

app = Flask(__name__)

global data
global scheduleObj
scheduleObj= "[{'start_time': '15:30', 'days': 'Tuesday', 'end_time': '17:20', 'title': 'SYDE 322 LEC 001'}]"

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/loginUser',methods=['POST'])
def loginUser():
     # read the posted values from the UI
    _username = request.form['inputName']
    _password = request.form['inputPassword']
    # validate the received values
    if _username and _password:
        return redirect('/search')
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/searchResult', methods=['POST'])
def search_result():
  data = []
  _subject = str(request.form['subject'])
  _catalogNo = str(request.form['catalogNo'])
  _startTime = str(request.form['startTime'])
  _endTime = str(request.form['endTime'])

  getCoursesByTime = UWSchedulerService.get_course_schedule_by_time(subject = _subject, catalog_number = _catalogNo, start_time = _startTime, end_time = _endTime)

  for i in getCoursesByTime:
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
    		dayz = dayz + ', ' + day
    info = i.subject + ' ' + i.catalog_number + ' ' + i.section

    course_info = {"title":info, "start_time":i.start_time, "end_time":i.end_time, "days":dayz};
    data.append(course_info)
  print data
  return json.dumps(data)

@app.route('/schedule')
def show_schedule():
  return render_template('schedule.html')

@app.route('/scheduleData', methods=['POST'])
def get():
   _myArray = request.form['myArray']
   scheduleObj = _myArray
   return scheduleObj

@app.route('/data')
def formulate_schedule():
  with open("events.json", "r") as input_data:
    return input_data.read()

# formulate_schedule()
if __name__ == '__main__':
    app.run()

  # start_date = request.args.get('start', '')
  # # end_date = request.args.get('end', '')

  # newobj = pickle.loads(scheduleObj)
  # for obj in newobj:
  #   print obj
  # # calObj = {
  # #   "title": "SYDE 322 LEC 001",
  # #   "start": "2016-03-29T15:30:00",
  # #   "end": "2016-03-29T17:20:00"
  # # }
  # return jsonify(newobj)



