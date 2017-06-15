from flask import Flask,request,redirect,session,flash,render_template
import datetime

app = Flask(__name__)
app.secret_key = "aznodekx"

@app.route('/')
def index():
    session['d'] = datetime.date.today()
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    uppercase = 0
    number = 0
    for i in range(len(request.form['password'])):
        if request.form['password'][i].isupper():
             uppercase += 1
        if request.form['password'][i].isupper():
            number += 1
    if len(request.form['email']) < 1 or len(request.form['first_name']) < 1 or len(request.form['last_name']) < 1 or len(request.form['password']) < 1 or len(request.form['password_re']) < 1:
        flash('Please make sure you filled out all the fields. Thank you.')
    elif not request.form['first_name'].isalpha() or not request.form['last_name'].isalpha():
        flash('Please make sure the name fields do not have any numbers.')
    elif len(request.form['password']) <= 8:
        flash('Password should be more than 8 characters.')
    elif not request.form['password'] == request.form['password_re']:
        flash('Please make sure your passwords matches.')
    elif uppercase == 0 or number == 0:
        flash('Please enter a password with at least a uppercase and a number.')
    else:
        flash('Thanks for submitting your information.')
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 