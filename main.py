from flask import Flask, request, render_template

app = Flask(__name__)

#
# @app.route('/')
#
# def index():
#     return "hello"

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

# templates
@app.route('/')
@app.route('/profile/<name>')
def getprofile(name=None):
    return render_template('profile.html', name=name)


@app.route('/shopping')
def shoplist():
    shop = ["tuna", "ketchup"]
    return render_template('shopping.html', food=shop, s = "s")


if __name__ == '__main__':
    app.run()

