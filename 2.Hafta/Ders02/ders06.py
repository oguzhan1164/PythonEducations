ogrenciler = []

print("=== Öğrenci Not Takibi ===")
print("Çıkmak için 'çık' yazın")

while True:
    ad = input("Öğrenci adı: ")
    if ad == "çık":
        break
    soyad = input("Öğrenci soyadı: ")
    if soyad == "çık":
        break
    notu = int(input(f"{ad} için not: "))
    if notu < 0:
        break
    
    ogrenciler.append  ({
        "ad": ad,
        "soyad":soyad,
        "not": notu
    })
 

print("\n--- Tüm Öğrenciler ---")

for ogrenci in ogrenciler:
    print(f"{ogrenci["ad"]} {ogrenci["soyad"]} : {ogrenci["not"]}")