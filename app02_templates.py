from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    prodi = "TI dan SI"
    return render_template("index.html", prodi=prodi)


if __name__=="__main__":
    app.run(debug=True)