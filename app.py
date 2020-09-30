from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    #Data yg akan di looping dan dikondisikan
    prodi = ['Sistem Informasi', 'Teknik Informatika','Bisnis Digital']

    jurusan="Sistem Informasi"

    return render_template("index.html", prodi=prodi, jurusan=jurusan)

if __name__ == "__main__":
    app.run(debug=True)
