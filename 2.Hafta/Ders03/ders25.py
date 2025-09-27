# Sözlük Anahtar-Değer Değiştirme
# Bir sözlük içindeki anahtar ve değerleri yer değiştiren fonksiyon
# Fonksiyon, yeni oluşturulan sözlüğü return ile döndürecek
"""
yöntem1
def anahtar_deger_degistir(sozluk):
    yeni_sozluk = {}
    for anahtar,deger in sozluk.items():
        yeni_sozluk[deger] = anahtar
    return yeni_sozluk

"""
#yöntem2
def anahtar_deger_degistir(sozluk):
    return {deger: anahtar for anahtar, deger in sozluk.items()}

# Kullanım
renkler = {"kırmızı": "#FF0000", "yeşil": "#00FF00", "mavi": "#0000FF"}
ters_renkler = anahtar_deger_degistir(renkler)
print("Ters çevrilmiş:", ters_renkler)

treng = {"kırmızı":"red","yeşil":"green","mavi":"blue"}

print("ingilizce renklerin türkçeleri",anahtar_deger_degistir(treng))