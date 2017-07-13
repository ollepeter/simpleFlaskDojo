from flask import Flask, redirect, url_for

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


@app.route('/admin')
def greet_admin():
    return 'Hello Admin!'


@app.route('/guest/<guest>')
def greet_guest(guest):
    return 'Hello {0} as guest'.format(guest)


@app.route('/user/<name>')
def check_admin(name):
    if name == 'admin':
        return redirect(url_for('greet_admin'))
    else:
        return redirect(url_for('greet_guest', guest=name))


if __name__ == '__main__':
    app.run(debug=True)
