#Kullanıcı doğum tarihini girer, program kaç gün sonra doğum günü olduğunu hesaplar.

from datetime import datetime

dogum = input("Doğum tarihiniz (GG.AA.YYYY): ")
gun, ay, yil = map(int, dogum.split("."))
dt_dogum = datetime(yil, ay, gun) #değişkeni yıl ay gün şekline getirdik bunun sebebi datetime.now() ile bugünü aldığımızda gelen veri yıl ay gün olarak geliyor işleme sokabilmek için kullanıcıdan aldığımız veriyi de datetime.now daki formata çevirmiş olduk
bugun = datetime.now()

# Bu yılki doğum günü
bu_yil_dogum = dt_dogum.replace(year=bugun.year)

if bu_yil_dogum < bugun:
    print((bugun-bu_yil_dogum).days,"gün önce doğum gününüzdü")
    bu_yil_dogum = bu_yil_dogum.replace(year=bugun.year + 1)
    print()

kalan = (bu_yil_dogum - bugun).days
print(f"Doğum gününüze {kalan} gün kaldı! 🎉")