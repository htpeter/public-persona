from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("./homepage.html", **template_variables)


if __name__ == "__main__":
    app.run(debug=False)
