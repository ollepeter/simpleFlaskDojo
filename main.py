from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/hello/<name>')
def hello(name):
    print(name)
    return 'Hello {0} !'.format(name)


@app.route('/square/<int:num>')
def double(num):
    square = num * num
    return 'The square of {0} is {1}!'.format(num, square)


@app.route('/flask/')
def flask():
    return 'This is /flask/...'


if __name__ == '__main__':
    app.run(debug=True)
