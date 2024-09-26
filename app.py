from flask import Flask, request, render_template
import re

app = Flask(__name__)

# Define the email validation function
def validate_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    if not validate_email(email):
        return "Invalid email address!", 400
    
        # Write the data to a text file
    with open('data.txt', 'a') as file:
        file.write(f"Name: {name}, Email: {email}\n")

    return "Submitted successfully!"

# Route to retrieve and display stored data
@app.route('/users')
def users():
    users_data = []
    try:
        with open('data.txt', 'r') as file:
            users_data = file.readlines()
    except FileNotFoundError:
        users_data = ["No data found."]

    return render_template('users.html', users=users_data)

if __name__ == '__main__':
    app.run(debug=True)