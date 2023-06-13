from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return "Hello there from Flask!!!"

@app.route("/pooh")
def pooh():
    return "Hello there P. Bear"

if __name__ == "__main__":
    app.run(debug=True)