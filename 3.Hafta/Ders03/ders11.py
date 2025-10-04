#Web siteleri, mobil uygulamalar veriyi genellikle JSON formatında taşır.
import json
import os

bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "ogrenci.json"

ogrenciler = [
{
    "isim": "Zeynep",
    "yas": 23,
    "bolum": "Matematik"
},

{
    "isim": "Oguzhan",
    "yas": 26,
    "bolum": "Bilgisayar"
}]

with open("ogrenci.json", "w") as f:
    json.dump(ogrenciler, f, indent=4)  # güzel format
   
with open("ogrenci.json", "r") as f:
    veri = json.load(f)
    print(veri,type(veri))
    for ogrenci in veri:
        print(ogrenci["yas"],type (ogrenci["yas"]))
"""
json.load() → dosyadan okur
json.loads() → string’den okur
json.dump() → dosyaya yazar
json.dumps() → string’e çevirir 
"""