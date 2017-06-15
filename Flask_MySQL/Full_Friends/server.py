from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'Full_friends')

@app.route('/')
def index():
    print "inside root"
    query = "SELECT name, age, created_at FROM users"
    friends = mysql.query_db(query) 
    print friends
    return render_template('index.html', friends = friends)

@app.route('/add_friend', methods = ['POST'])
def add_friend():
    print "inside /addfriend"
    query = "INSERT INTO users(name, age, created_at) VALUES (:name, :age, now()) "
    data = {
        'name': request.form['name'],
        'age': request.form['age']
    }
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 