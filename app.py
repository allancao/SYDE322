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

@app.route('/searchResult', methods=['POST'])
def search_result():
  _subject = str(request.form['subject'])
  _catalogNo = str(request.form['catalogNo'])
  _startTime = str(request.form['startTime'])
  _endTime = str(request.form['endTime'])
  _weekday = str(request.form.getlist('check'))

@app.route('/schedule')
def show_schedule():
  return render_template('schedule.html')

@app.route('/scheduleData')
def formulate_data():
  return data



if __name__ == '__main__':
    app.run()