from flask import Flask, render_template, request
import queries

app = Flask(__name__)


@app.route('/')
def index():
    user_id = 1
    locations = queries.get_locations_for_user(user_id)
    return render_template('main.html', locations=locations)


@app.route('/rotate')
def rotate():
    return render_template('rotate.html')


if __name__ == '__main__':
    app.run(debug=True)