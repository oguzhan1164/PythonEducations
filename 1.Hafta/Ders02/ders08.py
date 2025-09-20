puan = int(input("Ortalamanızı giriniz"))
if puan < 0:
    print("hatalı puan girişi yaptınız")
else:
    if puan < 70:
        print("Belge almaya puanınız yeterli değil")
    else:
        if puan <85:
            print("Teşekkür alabilirsiniz tebrikler")
        else:
            if puan <=100:
                print("Takdir aldınız tebrikler")
            else:
                print("Geçerli bir puan girişi olmadı")