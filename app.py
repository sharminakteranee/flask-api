from flask import Flask
app = Flask(__name__)

@app.route('/api/v1')
def hello_world():
    return 'Flask Dockerized new...'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
