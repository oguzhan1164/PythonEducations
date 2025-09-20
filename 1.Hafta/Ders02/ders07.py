yemek = input("yemek giriniz ")
icecek = input("içecek bilgisi giriniz ")

if yemek == "pizza" and icecek =="kola":
    print("Geçerli sipariş")
    print("afiyet olsun")
else:
    print(f"{yemek} - {icecek} ikilisi doğru sipraiş değil")