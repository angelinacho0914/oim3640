from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        return f'<h1> Hello, {name}! </h1> <p> I am excited to learn! </p>' 
    return f'<h1> Hello World! </h1>'


@app.route('/square/') # Routing
@app.route('/square/<number>')
def square(number=None):
    if number is None:
        return "You need to provide a number"
    return str(int(number) ** 2)


if __name__ == '__main__':
    app.run(debug=True)