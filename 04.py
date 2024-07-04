from flask import Flask, request, render_template, flash, redirect, url_for
import json
app = Flask(__name__, template_folder = 'templates')

# /login display login form


@app.route('/')
# login function verify username and password
def login():
    return render_template('login.html')

@app.route('/info', methods = ['POST'])
def info():
    result = request.form
    with open('users.json', 'a') as fp:
        json.dump(result, fp)
    return render_template("confirm.html", result=result)
   
if __name__ == '__main__':
    app.run(debug=True)