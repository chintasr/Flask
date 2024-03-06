from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/regex-matcher')  # Route for Regex Matcher
def regex_matcher():
    return render_template('regex_matcher.html')

@app.route('/results', methods=['POST'])  # Route for processing Regex Matcher form submission
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

@app.route('/email-validation')  # Route for Email Validation
def email_validation():
    return render_template('email_validation.html')

@app.route('/validate-email', methods=['POST'])  # Route for processing Email Validation form submission
def validate_email():
    email = request.form['email']
    regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    is_valid = re.match(regex_pattern, email)
    if is_valid:
        result = "Valid Email Address"
    else:
        result = "Invalid Email Address"
    return render_template('validate_email.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
