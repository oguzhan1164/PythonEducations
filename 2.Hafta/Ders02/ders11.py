urunler = []

print("=== Pazar Listesi ===")
print("Çıkmak için 'bitir' yazın")
toplam = 0
while True:
    ad = input("Ürün adı: ")
    if ad == "bitir":
        break
    
    fiyat = float(input("Fiyat (TL): "))
    
    urun = {
        "ad": ad,
        "fiyat": fiyat,
    }
    urunler.append(urun)
    print(f"'{ad}' sisteme eklendi.\n")
    toplam +=fiyat
    
print("\n--- Tüm Ürünler ---")
for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']} TL,]")


print(f"Toplam harcamanız :{toplam} TL")