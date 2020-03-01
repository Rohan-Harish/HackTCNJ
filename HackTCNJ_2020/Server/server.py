from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__, template_folder='C:\\Users\\rohan\\Documents\\Coding\\Hackathons\\HackTCNJ\\HackTCNJ_2020\\Server')

names = ['rh388', 'vrp53', 'ps937', 'sn637']
passwords = ['rohanpassword', 'varunpassword', 'prathishapassword', 'sahanapassword']

@app.route('/login')
def starter():
    return render_template('index.html')


@app.route('/authenticate', methods=["POST", "GET"])
def authenticate():
    return "error"
    if request.method == "POST":
        if passwords[names.find(request.form['name'])] == request.form['password']:
            return "Authenticated"
        else:
            return "error"
    else:
        if passwords[names.find(request.form['name'])] == request.form['password']:
            return "Worked"
        else:
            return "error"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 6969)
