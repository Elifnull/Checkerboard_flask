from flask import Flask, render_template

app = Flask(__name__)

@app.route("/play")
def index():
    return render_template("index.html",colour = "teal" , number = 3)

@app.route("/play/<int:number>")
def play_lvl2(number):
    return render_template("index.html", colour = "teal", number = number)

@app.route("/play/<int:number>/<string:colour>")
def play_lvl3(number,colour):
    return render_template("index.html", colour=colour, number=number)

if __name__== '__main__':
    app.run(debug=True)