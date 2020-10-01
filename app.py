from flask import Flask, render_template, request, session

app = Flask(__name__)
#secreat key
app.config["SECRET_KEY"] = "iniSecretkeyku"

@app.route("/")
def index():
    #Data yg akan di looping dan dikondisikan
    prodi = ['Sistem Informasi', 'Teknik Informatika','Bisnis Digital']

    jurusan="Sistem Informasi"

    return render_template("index.html", prodi=prodi, jurusan=jurusan)

#layout
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about") 
def about():
    return render_template("about.html")

#parsing nilai int, string
@app.route("/parsing/<string:nilaiku>")
def ayo_parsing(nilaiku):
    return "nilainya adalah : {} ".format(nilaiku)
#argument parser
@app.route("/parserargument")
def ini_argument():
    data = request.args.get("nilai")
    return "nilainya dari argument parser : {}".format(data)

#memparsing nilai dari url untuk set nilai session
@app.route("/halaman/<int:nilai>")
def session_pertama(nilai):
    session["nilaiku"] = nilai
    return "Berhasil mengeset nilainya"

#menampilkan pada halaman lain
@app.route("/halaman/lihat")
def vew_session_pertama():
    #teknik mengatasi error
    try:
        data = session["nilaiku"]
        return "Nilai yang telah diset adalah = {} ".format(data)
    except:
        return "Anda Keluar, anda tiak memiliki akses.!"

#logout / distroy session
@app.route("/halaman/logout")
def logout_session_pertama():
    session.pop("nilaiku")
    return "Berhasil logout / menghapus session"

if __name__ == "__main__":
    app.run(debug=True)
