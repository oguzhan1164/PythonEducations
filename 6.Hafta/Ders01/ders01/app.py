from flask import Flask

app = Flask(__name__) #flask uygulama nesnesi oluşturuldu
@app.route("/index")
@app.route("/") #ana sayfa url
def hello():
    return "Merhaba Techİstanbul Python Bootcamp Hoşgeldiniz"
@app.route("/hakkimizda")
def hakkimizda():
    return "Hakkımızda sayfasındasınız"
@app.route('/kullanici/<isim>/<soyisim>')
def kullanici(isim,soyisim):
    return f"Kullanıcı sayfasındasınız:{isim} - {soyisim}"
@app.route('/yil/<int:year>')
def yil_goster(year):
    return f"şuan {year} yılındayız"

if __name__ == "__main__":
    app.run(debug=True) #app.run(debug=True): Geliştirme sunucusunu başlatır; debug=True sayesinde kodda değişiklik yapınca otomatik yeniden yüklenir.