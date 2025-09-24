ogrenci = ["Ali", 22, "Bilgisayar Müh.", 85]

ogrenci = {
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

print(araba["marka"])  # Toyota
print(araba["yil"])     # 2020

araba["yil"] = 2022          # güncelle
araba["kilometre"] = 45000   # yeni ekle int(input("km bilgisi giriniz")) şeklinde de veri kullanıcıdan istenebilir

del araba["renk"]
#Tüm Anahtarları Al
print(araba.keys())
# dict_keys(['marka', 'model', 'yil', 'kilometre'])

#Tüm Değerleri Al
print(araba.values())
# dict_values(['Toyota', 'Corolla', 2022, 45000])
print(araba.items())
#dict_items([('marka', 'Toyota'), ('model', 'Corolla'), ('yil', 2022), ('kilometre', 45000)])

for dd in araba:
    print(dd,araba[dd])



#Tüm Anahtar-Değer Çiftlerini Al
for anahtar, deger in araba.items():
    print(f"{anahtar}: {deger}")
