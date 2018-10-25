from flask import Flask, render_template, request, session, redirect, url_for
import queries
from werkzeug import security
import json

app = Flask(__name__)
app.secret_key = 'vmi29???#@ttd@9UI5FJ%+!SoEQZRszgtzit'


@app.route('/')
def index():
    #if 'user_name' in session:
    #user_id = session['user_id']
    #locations = queries.get_locations_for_user(user_id)
    #return render_template('main.html', locations=locations)
    #return redirect(url_for('registration_and_login'))
    return render_template('main.html')

@app.route('/rotate')
def rotate():
    return render_template('rotate.html')


@app.route('/save-new-person', methods=['POST'])
def save_new_person():
    if 'user_name' in session:
        new_person_name = request.form['name']
        new_person_color = request.form['color']
        new_person_phone = request.form['phone']
        user_id = session['user_id']
        keys = ('id', 'name', 'phone', 'color', 'status')
        new_person_data = queries.save_new_person(new_person_name, new_person_phone, new_person_color, user_id)
        person_data = {k: v for k, v in zip(keys, new_person_data)}
        return json.dumps(person_data)
    return redirect(url_for('registration_and_login'))


@app.route('/registration_and_login')
def registration_and_login():
    if 'user_name' in session:
        return redirect(url_for('index'))
    return render_template('registration_and_login.html')


@app.route("/register", methods=['GET'])
def registration():
    if 'user_name' in session:
        return redirect(url_for('index'))
    return render_template('registration.html')


@app.route("/register", methods=['POST'])
def save_user():
    if 'user_name' in session:
        return redirect(url_for('index'))
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']
    password = security.generate_password_hash(password)
    return json.dumps(queries.insert_user(username, password, email, phone))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'user_name' in session:
        return redirect(url_for('index'))
    if request.method == 'GET':
        return render_template('login.html')
    user_name = request.form['username']
    password = request.form['password']
    hashed_password_data = queries.get_password(user_name)
    if hashed_password_data:
        hashed_password = hashed_password_data['password']
        if security.check_password_hash(hashed_password, password):
            session['user_name'] = user_name
            session['user_id'] = queries.get_user_id(user_name)['id']
            return json.dumps({"invalid_data": False})
    return json.dumps({"invalid_data": True})


@app.route('/logout')
def logout():
    if 'user_name' in session:
        session.pop('user_name')
        session.pop('user_id')
    return redirect(url_for("registration_and_login"))


@app.route('/get-people-data')
def get_people_data():
    if 'user_name' in session:
        user_id = session['user_id']
        people_data = queries.get_people_for_user(user_id)
        return json.dumps(people_data)
    return redirect(url_for('registration_and_login'))


@app.route('/get-locations-data')
def get_locations_data():
    if 'user_name' in session:
        user_id = session['user_id']
        locations_data = queries.get_locations_for_user(user_id)
        return json.dumps(locations_data)
    return redirect(url_for('registration_and_login'))


if __name__ == '__main__':
    app.run(debug=True)
