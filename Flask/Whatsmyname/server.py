from flask import Flask, request, render_template,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    print request.form["your_name"]
    return redirect('/')

app.run(debug=True)