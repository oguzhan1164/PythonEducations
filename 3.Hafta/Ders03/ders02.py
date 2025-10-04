# dosyadan veri okuma işlemleri
with open("kayit.txt","r") as dosya:
    # print(dosya.read()) 
    # print(type(dosya.read()))
    #print(dosya.read(10)) #karakter okuma
    print("----- içerik 1 -----")
    icerik = dosya.read()
    print(len(icerik),type(icerik))
    print(icerik)
    print("---- içerik 2 ----")
    icerik2 = dosya.read()
    print(len(icerik2),type(icerik2))
    print(icerik2)