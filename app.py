from flask import Flask, render_template, request, json
app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/loginUser',methods=['POST','GET'])
def loginUser():
     # read the posted values from the UI
    _username = request.form['inputName']
    _password = request.form['inputPassword']

    #validate the received values
    if _username and _password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})

@app.route('/search')
def search_classes():
	return render_template('search.html')

if __name__ == '__main__':
    app.run()