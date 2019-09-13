from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "Ubunifu;the creatives haven"
    return render_template("index.html",title=title)

@app.route("/About")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)