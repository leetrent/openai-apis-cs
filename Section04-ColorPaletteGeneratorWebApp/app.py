import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    createResult = openai.Completion.create(
        model="text-davinci-003",
        max_tokens=200,
        prompt="Make me laugh!"
    )
    return(createResult["choices"][0]["text"])
    #return render_template("index.html")

@app.route("/palette", methods=["POST"])
def palette():
    return "Hello there P. Bear"

if __name__ == "__main__":
    app.run(debug=True)