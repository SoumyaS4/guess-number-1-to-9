from flask import Flask
import random

gen_num = random.randint(1, 9)

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Guess The Number 1  to 9 </h1>'\
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=500></img>'

@app.route('/<int:number>')
def greet(number):
    if gen_num > number :
        return '<h1 style= "color: red" >Too high, try Again</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"width=200></img>'
    elif gen_num < number:
        return '<h1 style= "color : red" >Too low, try Again</h1>'\
                '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"width=200></img>'
    else:
        return '<h1 style= "color: green" >You found me</h1>'\
                '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"width=200></img>'

@app.route('/logout')
def bye():
    return "have a good day"

if __name__ == "__main__":
    app.run(debug=True)