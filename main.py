from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks=score)


@app.route('/result')
def result():
    dict = {'phy': 50,
            'che': 60,
            'maths': 70
            }
    return render_template('result.html', result=dict)


if __name__ == '__main__':
    app.run(debug=True)
