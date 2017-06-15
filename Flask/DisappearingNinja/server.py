from flask import Flask, request, render_template,redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return 'No ninjas here'

@app.route('/ninja')
def ninja():
    return render_template('ninja.html')

@app.route('/ninja/<color>')
def show_color(color):
    if color == "blue":
        location = "img/leonardo.jpg"
    elif color == "orange":
        location = "../static/img/michelangelo.jpg"
    elif color == "red":
        location = "../static/img/raphael.jpg"
    elif color == "purple":
        location = "../static/img/donatello.jpg"
    else:
        location = "../static/img/notapril.jpg"
    return render_template('display_color.html', url = location)


if __name__ == '__main__':
    app.run(debug=True)