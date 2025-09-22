ogrenci_adi = "Timur"
ogrenci_soyadi = "Çakal"
ogrenci_no = 153
ogrenci_katilim = True
ogrenci_ortalama = 3.60

ogrenci1 = [ogrenci_adi, ogrenci_soyadi, ogrenci_no, ogrenci_katilim, ogrenci_ortalama]
print(ogrenci1, type(ogrenci1))

ogrenci2 = ["ali","sunguroglu",14,True,3.2]
print(ogrenci2, type(ogrenci2))

print(ogrenci2[0], type(ogrenci2[0]))
print(len(ogrenci1))
print("ali" in ogrenci2)
print("ali" in ogrenci1)


for bilgi in ogrenci2:
     print(bilgi)


for i in range(len(ogrenci1)):
     print(ogrenci1[i])