from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
#secreat key
app.config["SECRET_KEY"] = "iniSecretkeyku"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/redirect-about")
def redirect_about():
    return redirect(url_for('about'))

@app.route("/redirect-contact")
def redirect_contact():
    return redirect(url_for('contact'))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
