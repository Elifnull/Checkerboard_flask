from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    f'Hello, WORLD. I am doing it!'

@app.route('/<dojo>')
def dojo(dojo):
    return f"{dojo}, yes i did make '{dojo}' a variable!"

@app.route('/say/<string:name>')
def speak_say(name):
    return f'I am obligated to say "HI, {name.capitalize()}"'

@app.route('/repeat/<int:num>/<string:word>')
def repeat(word,num):
    sentance = ''
    for i in range(0, num):
        sentance += f'<p>{word}<p>'
    return sentance

if __name__== '__main__':
    app.run(debug=True)