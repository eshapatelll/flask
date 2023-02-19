from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define the list of student organizations
orgs = ['Club A', 'Club B', 'Club C', 'Club D', 'Club E']

# Define a dictionary to store registered users
registered_users = {}

# Define a function to validate form data
def validate_form(name, org):
    if not name or not org:
        return False
    if org not in orgs:
        return False
    return True

# Define the home page route and form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        org = request.form['org']
        if validate_form(name, org):
            registered_users[name] = org
            return redirect(url_for('list_users'))
        else:
            error = 'Please enter a valid name and select a valid organization.'
            return render_template('home.html', orgs=orgs, error=error)
    else:
        return render_template('home.html', orgs=orgs)

# Define the list of registered users route
@app.route('/list-users')
def list_users():
    return render_template('list_users.html', registered_users=registered_users)

if __name__ == '__main__':
    app.run(debug=True)
