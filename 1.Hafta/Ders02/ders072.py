yemek = input("yemek giriniz ")
icecek = input("içecek bilgisi giriniz ")

if yemek == "pizza" :
    print("pizza geçerli yemek siparişi") 
    if (icecek =="kola" or icecek == "ayran"):
        print("Geçerli sipariş")
        print("afiyet olsun")
    else:
        print(f"{yemek} - {icecek} ikilisi doğru sipraiş değil")
else:
    print("Geçersiz sipariş")