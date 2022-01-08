from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", numw = 4, numh = 4, colour1 ="black", colour0 = "red")

@app.route("/<int:numw>")
def width_check(numw):
    return render_template("index.html", numw = numw, numh = 4, colour1 ="black", colour0 = "red")

@app.route("/<int:numw>/<int:numh>")
def widthandheight_check(numw,numh):
    return render_template("index.html", numw = numw, numh = numh, colour1 ="black", colour0 = "red")

@app.route("/<int:numw>/<int:numh>/<string:colour1>")
def colour_check(numw,numh,colour1):
    return render_template("index.html", numw = numw, numh = numh, colour1 =colour1, colour0 = "red")

@app.route("/<int:numw>/<int:numh>/<string:colour1>/<string:colour2>")
def colours_check(numw,numh,colour1,colour2):
    return render_template("index.html", numw = numw, numh = numh, colour1 =colour1, colour0 = colour2)

if __name__== '__main__':
    app.run(debug=True)