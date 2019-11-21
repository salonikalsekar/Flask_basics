from flask import Flask, request

app = Flask(__name__)


@app.route('/')

def index():
    return "hello"

@app.route('/hello/<user>')
def profile(user):
    return "<h1>hello %s</h1>" % user

@app.route('/hellorole/<int:id>')
def roleid(id):
    return "<h1>hello role %s</h1>" % id

@app.route('/request', methods=['GET', 'POST'])
def req():
    if request.method == 'GET':
        return "method used get"
    else:
        return "post"


if __name__ == '__main__':
    app.run()

