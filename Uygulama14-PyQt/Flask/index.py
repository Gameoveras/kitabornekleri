from flask import Flask, render_template, flash
import sqlite3

app = Flask(__name__)

baglanti = sqlite3.connect("yeni.db", check_same_thread=False)

@app.route("/")
def anasayfa():
    urunler = baglanti.execute('SELECT * FROM urun').fetchall()
    return render_template('index.html', urunler=urunler)

if __name__ == "__main__":
    app.run(debug=True)
