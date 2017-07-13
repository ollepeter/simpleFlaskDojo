from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST'])
def result():
    results = request.form
    print(results)
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
