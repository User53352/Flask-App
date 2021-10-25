from flask import Flask, request, g, abort

app = Flask(__name__)

@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.route("/")
def index():
    print("index() called")
    return '<p>Testings Request Hooks</p>'

@app.route("/") # после кода аборта сценарии не выполняются
def index():
    abort(404)


if __name__ == "__main__":
    app.run(debug=True)
