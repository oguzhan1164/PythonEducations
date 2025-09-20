"""
Kullanıcıdan şu bilgileri alıp, ekrana güzel bir mesaj yazdırın:

Ad
Yaş
Şehir
Hobisi

"""
ad = input("Adınız: ")
yas = int(input("Yaşınız: "))
sehir = input("Şehir: ")
hobi = input("Hobiniz: ")
boy=float(input("boyunuzu giriniz"))
devam_durumu = bool(input("devam durumunuz"))#boşveri false dolu veri true

print("\n--- KİŞİSEL TANITIM KARTI ---")
print("İsim:", ad)
print("Yaş:", yas)
print("Şehir:", sehir)
print("Hobi:", hobi)
print("Boy:", boy)
print("Durum:", devam_durumu)
print("----------------------------")