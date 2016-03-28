from flask import Flask, render_template, request, json, url_for, redirect
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
    print _username
    print _password
    #validate the received values
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
  _time = request.form['time']

  courses = UWSchedulerService.get_course(subject = _subject, catalog_number = _catalogNo )
  for i in courses:
    print(i)

  getSchedule  = UWSchedulerService.get_course_schedule(subject = _subject, catalog_number = _catalogNo)
  for i in getSchedule:
    print(i)


@app.route('/Schedule', methods = ['GET'])
def show_schedule():
  "Youre showing the Schedule"

if __name__ == '__main__':
    app.run()