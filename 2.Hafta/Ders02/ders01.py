ogrenci = ["Ali", 22, "Bilgisayar Müh.", 85]

ogrenci_sozluk = {
    "isim": "Ali",
    "yas": 22,
    "bolum": "Bilgisayar Müh.",
    "not": 85
}

araba = {
    "marka": "Toyota",
    "model": "Corolla",
    "yil": 2020,
    "renk": "gri"
}
print(araba)
print(type(araba))
print(araba["marka"])  # Toyota
print(araba["yil"])     # 2020

araba["yil"] = 2022          # güncelle
araba["kilometre"] = 45000   # yeni ekle

del araba["renk"]

print(araba)