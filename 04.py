from flask import Flask, request, render_template, flash, redirect, url_for
app = Flask(__name__)

# /login display login form


@app.route('/login', methods=['GET', 'POST'])
# login function verify username and password
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:

            # flashes on successful login
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)