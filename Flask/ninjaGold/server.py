from flask import Flask, render_template,redirect, request, session
import random
from datetime import datetime, date, time
app = Flask(__name__)
app.secret_key = "qwerasdf"


@app.route('/')
def index():
    # session['gold'] = 0
    if 'gold' not in session:
        session['gold'] = 0
        session['change'] = 0  
        session['log'] = ''
        session['display'] ='' 
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    d = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    if request.form['building'] == 'farm':
        session['change'] = random.randint(10,20)
        session['log'] = "<p>Earned "+ str(session['change']) + " golds from the farm! (" + d + ")</p>"
    elif request.form['building'] == 'cave':
        session['change'] = random.randint(5,10)
        session['log'] = "<p>Earned "+ str(session['change']) + " golds from the cave! (" + d + ")</p>"
    elif request.form['building'] == 'house':
        session['change'] = random.randint(2,5)
        session['log'] = "<p>Earned "+ str(session['change']) + " golds from the house! (" + d + ")</p>"
    elif request.form['building'] == 'casino':
        session['change'] = random.randint(0,50) * random.sample([1,-1],1)[0]
        if session['change'] >= 0:
            session['log'] = "<p>Entered a Casino and won " + str(session['change']) + " golds!!!YEAH!!! (" + d + ")</p>"  
        else:
            session['log'] = "<p id=\"red\">Entered a Casino and lost " + str(-session['change']) + " golds...ouch... (" + d + ")</p>"
    session['gold'] += session['change']
    session['display'] = session['log'] + session['display']
    print session['display']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['gold'] = 0
    session['change'] = 0  
    session['log'] = ''
    session['display'] ='' 
    return redirect('/')

if __name__ == '__main__':
  app.run(debug=True)
 