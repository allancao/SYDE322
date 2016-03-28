from flask import Flask, render_template, request, json, url_for, redirect
import UWSchedulerService
app = Flask(__name__)

@app.route('/login')
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
        return render_template('search.html')
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
  print(_subject)
  print(_catalogNo)

  courses = UWSchedulerService.get_course(subject = _subject, catalog_number = _catalogNo )
  item = UWSchedulerService.get_course(subject='SYDE', catalog_number='322')
  print(item)

@app.route('/Schedule', methods = ['GET'])
def show_schedule():
  "Youre showing the Schedule"

if __name__ == '__main__':
    app.run()