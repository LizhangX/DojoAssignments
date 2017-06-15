from flask import Flask, render_template, request, session, flash, redirect
from mysqlconnection import MySQLConnector
import md5
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "dasdf"
mysql = MySQLConnector(app,'registration')

@app.route('/')
def index():
    if 'login' not in session:
        session['login'] = 0
    if session['login'] != 0:
        return redirect('/success')
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    f = request.form['fname']
    l = request.form['lname']
    e = request.form['email']
    p = request.form['password']
    pc = request.form['password_c']

    if f < 2 or not f.isalpha():
        flash("Invalid first name. First Name - letters only, at least 2 characters")
    elif l < 2 or not l.isalpha():
        flash("Invalid last name. Last Name - letters only, at least 2 characters ")
    elif e < 1 or not EMAIL_REGEX.match(e):
        flash("Invalid email. ")
    elif p < 8 or not p.isalpha():
        flash("Invalid password. at least 8 characters")
    elif pc != p:
        flash('passwords not match')
    else:
        pw = md5.new(p).hexdigest()
        # check if the users is registered
        query = "select * from users where email = :e "
        data = {
            'f': f,
            'l': l,
            'e': e,
            'pw': pw
        }
        user = mysql.query_db(query, data)
        print user
        if user != []:
            flash("Email already registered!")
            return redirect('/')
        insert_query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (:f, :l, :e, :pw, now())"
        session['login'] = mysql.query_db(insert_query, data)
        flash('Congratulations! You are successfully registered!')
        # session['login'] = user[0][users_id]
        return redirect('/success')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    password = md5.new(request.form['password']).hexdigest()
    email = request.form['email']
    user_query = "SELECT * FROM users WHERE users.email = :email AND users.password = :password"
    query_data = { 'email': email, 'password': password}
    user = mysql.query_db(user_query, query_data)
    if len(user) != 0:
        print 'log in successful'
        session['login'] = user[0]['user_id']
        print session['login']
        flash('Your are successfully logged in!')
        return redirect('/success')
    else:
        flash('please enter the correct email and password')
        return redirect('/')

@app.route('/success')
def success():
    query = "select first_name from users where user_id = :id"
    data = {
        'id': session['login']
    }
    user = mysql.query_db(query, data)
    name = user[0]['first_name']
    return render_template('success.html', name = name)

@app.route('/logout', methods=['POST'])
def logout():
    session['login'] = 0
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 