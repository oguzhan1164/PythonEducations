puan = int(input("Ortalamanızı giriniz"))
if puan < 0:
    print("hatalı puan girişi yaptınız")
elif puan < 70:
    print("Belge almaya puanınız yeterli değil")
elif puan < 85:
    print("Teşekkür alabilirsiniz tebrikler")
elif puan <=100:
    print("Takdir aldınız tebrikler")
else:
    print("geçerli bir puan girişi olmadı")   