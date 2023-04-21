from flask import Flask, request
import datetime as dt

app = Flask(__name__)


@app.route('/test', methods=['GET'])
def file_append():
    t1 = dt.datetime.now()
    write_data = 'File appended at: ' + str(t1)
    with open(r'C:\Users\dbhabad\Desktop\exe_demo.txt', 'a') as f1:
        f1.write(write_data)
        f1.write('\n')
    return 'Done'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9300)
