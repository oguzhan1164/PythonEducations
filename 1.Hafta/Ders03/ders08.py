"""
if True:
    pass #şuan doldurmak istemiyorsanız ya da o durum için yazılacak bir blok yoksa geçmek için kullanılır
print("Merhaba")

for dd in range(10):
    ad = input("Adınızı giriniz")
    if ad == "burak":
        print("burak bulundu")
        break #if gerçekleştiği an döngüyü bitirmek için kullanılır
    print(dd+1,". öğrenciye soruldu")

"""
for dd in range(10):
    print(dd+1)
    ad = input("Enter name")
    if ad == "burak":
        print("bu kişi zaten kayıtlı")
        continue
    soyad = input("Enter surname")
    print(f"{ad} {soyad} sisteme kaydedildi")


