from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #Data yg akan di looping
    prodi = ['Sistem Informasi', 'Teknik Informatika','Bisnis Digital']

    #Data yg di kondisikan
    keahlian = "ahli"
    return render_template("index.html", prodi=prodi, keahlian=keahlian)

if __name__ == "__main__":
    app.run(debug=True)
