from flask import *

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    print(uname)
    print(passwrd)
    if uname == "Dnyanesh" and passwrd == "12345":
        return "Welcome %s" % uname
    else:
        return 'Login Failed..!!'

if __name__ == '__main__':
    app.run()
