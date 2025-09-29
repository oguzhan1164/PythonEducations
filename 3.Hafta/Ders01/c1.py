"""
try:
    #riskli kodlar
    yas = int(input("Yaşınızı giriniz "))
    if yas < 18:
        print("Reşit değilsiniz.")
    else:
        print("Reşitsiniz")

except:
    #hata durumunda çalışacak kodlar
    print("Hata oluştu lütfen geçerli bir yaş giriniz.sayısal veri olmalı")

print("Program sonlandı")


ValueError int("abc")  gibi geçersiz dönüşüm
IndexError liste[10] ama listede 5 eleman var
TypeError "merhaba" + 5 gibi uyumsuz işlem
KeyError sozluk["olmayan_anahtar"]
ZeroDivisionError 5 / 0 gibi sıfıra bölme
AttributeError nesne.yok_ozellik gibi var olmayan özellik erişimi
Exception tüm hataların üst sınıfı
NameError tanımlanmamış_değişken gibi tanımsız değişken erişimi

try:
    sayi = int(input("Bir sayı giriniz"))
    sonuc = 100 / sayi
    print(sonuc)
except ValueError:
    print("Geçersiz giriş! Lütfen bir sayı giriniz")
except ZeroDivisionError:
    print("0 ile bölme işlemi yapamazsınız")
except Exception as e:
    print("Beklenmeyen bir hata oluştu",str(e))

    
⚠️ raise → manuel olarak hata tetikler
try-except ile birlikte kullanılırsa daha güçlü olur:     
    

yas = int(input("Yaşınız: "))

if yas < 0 or yas > 150:
    raise ValueError("Yaş 0-150 arasında olmalı!")
else:
    print("Yaşınız:", yas)
    print("geçerli yaş")
"""
try:
    yas = int(input("Yaşınızı giriniz"))
    if yas < 0 or yas > 150:
        raise ValueError("Yaş 0-150 arasında olmalı!")
except ValueError as e :
    print("Hata",e)

print("Program sonlandı")