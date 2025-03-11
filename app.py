from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
