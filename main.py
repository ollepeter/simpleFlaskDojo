from flask import Flask, redirect, url_for, request

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


@app.route('/success/<name>')
def success(name):
    return 'Hello {0} !'.format(name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        print('000 FORM 000')
        print(request.form)     
        return redirect(url_for('success', name=user))
    else:
        user = request.arg.get['nm']
        return redirect(url_for('success', name=user))


@app.route('/genre', methods=['POST'])
def genre():
        genre = request.form['gender']
        values = request.values
        print('000 VALUES 000')
        print(request.values)
        print('000 FORM 000')
        print(request.form)     
        return values['gender']


if __name__ == '__main__':
    app.run(debug=True)
