from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "asdfadsdf"
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def index():
    if not 'error' in session:
        session['error'] = 0
    return render_template('index.html')

@app.route('/email_validation', methods=['POST'])
def email_validation():
    query = "SELECT email FROM emails"
    email_list = mysql.query_db(query)
    email_entered = {'email': request.form['email']}
    print email_entered
    # print email_list
    if email_entered not in email_list:
        session['error'] = 1
        return redirect('/')
    else:
        query = 'UPDATE emails SET entered_at = now() WHERE email = '"'{}'"''.format(request.form['email'])
        mysql.query_db(query)
        session['error'] = 0
    return redirect('/show')

@app.route('/show')
def show():
    query = "SELECT email, entered_at FROM emails ORDER BY entered_at DESC"
    email_db = mysql.query_db(query)
    print email_db


    return render_template('show.html', email_db = email_db)
if __name__ == '__main__':
  app.run(debug=True)
 