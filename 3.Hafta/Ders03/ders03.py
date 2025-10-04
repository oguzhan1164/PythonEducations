#dosyadan veri okuma
# with open("kayit.txt","r") as dosya:
#     print(dosya.readline())
#     print(dosya.readline())

# with open("kayit.txt","r") as dosya:
#     for x in dosya:
#         print(x)
dosya=open("kayit.txt","r")
metin = dosya.read()
print(metin)
satirlar = metin.split("\n")
print(satirlar)

asil_metin = list(metin)
print(asil_metin)