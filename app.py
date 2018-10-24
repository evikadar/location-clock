from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/rotate')
def rotate():
    return render_template('rotate.html')



if __name__ == '__main__':
    app.run(debug=True)