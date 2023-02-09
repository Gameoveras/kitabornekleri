from flask import Flask, render_template, request, url_for, flash, redirect
import sqlite3

app = Flask(__name__)

baglanti = sqlite3.connect("yeni.db", check_same_thread=False)

@app.route("/")
def anasayfa():
    urunler = baglanti.execute('SELECT * FROM urun').fetchall()
    return render_template('index.html', urunler=urunler)

@app.route("/kaydol/", methods=['POST', 'GET'])
def kaydol():
    if request.method == 'POST':
        adsoyad = request.form['adsoyad']
        eposta = request.form['eposta']
        sifre = request.form['parola']
        baglanti.execute("Insert into kullanici(adsoyad,eposta,sifre) Values ('{}','{}','{}')" .format(adsoyad, eposta, sifre))
        baglanti.commit()
        
        return redirect(url_for('urunkaydet'))
       
    return render_template('kaydol.html')


@app.route("/girisyap/", methods=['GET', 'POST'])
def giris():
    if request.method == 'POST':
        eposta = request.form['eposta']
        sifre = request.form['parola']
        kisiler = baglanti.execute('SELECT * FROM kullanici').fetchall()
        for kisi in kisiler:
            if kisi[2] == eposta:
                if kisi[3] == sifre:
                    return redirect(url_for('urunkaydet'))
    return render_template('girisyap.html')


@app.route("/urunekle/", methods=['POST','GET'])
def urunkaydet():
    if request.method == 'POST':
        urunadi = request.form['urunadi']
        urunaciklamasi = request.form['urunaciklamasi']
        fiyat = request.form['fiyat']
        baglanti.execute("Insert into urun(urunadi,urunaciklamasi,urunfiyati) Values ('{}','{}','{}')" .format(urunadi, urunaciklamasi, fiyat))
        baglanti.commit()
        return redirect(url_for('urunkaydet'))
    return render_template('urunekle.html')


if __name__ == "__main__":
    app.run(debug=True)
