from flask import Flask, render_template, redirect,request,session
import random
app = Flask(__name__)
app.secret_key = "keysssss"
    

@app.route('/')
def index():
    # session.pop('random')
    # session.pop('status')
    # session.pop('guess')
    if 'random' not in session:
        session['random'] = random.randrange(0,101)
    if 'status' not in session:
        session['status'] = 'new'
        print session['random']
    return render_template('index.html')

@app.route('/random', methods=['POST'])
def random_num():
    session['guess'] = int(request.form['guess'])
    print session['guess']
    print session['random']
    if session['guess'] == session['random']:
        return redirect('/correct')
    else:
        return redirect('/wrong')

@app.route('/wrong')
def wrong():
    if session['guess'] < session['random']:
        session['status'] = "low"
    elif session['guess'] > session['random']:
        session['status'] = "high"
    return redirect('/')

@app.route('/correct')
def corret():
    session['status'] = "correct"
    return redirect('/')

@app.route('/reset')
def reset():
    session['random'] = random.randrange(0,101)       
    session.pop('guess') 
    session['status'] = 'new'
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 