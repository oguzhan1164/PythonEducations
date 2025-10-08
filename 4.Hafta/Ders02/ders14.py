import datetime
bugun = datetime.date.today()

print(bugun)
print(repr(bugun)) #tekrar nesne oluşturmaya uygun geliştirici için
print(str(bugun))# kullanıcı için açıklayıcı 
tarih = datetime.date(2018, 9, 2)
print(type(tarih))
print(tarih)

# tarihs = eval(repr(bugun))
# print(tarihs, type(tarihs))
# class Araba:
#     teker = 4
#     def __str__(self):
#         return "bu bir arabadır"

# otomobil = Araba()
# print(otomobil)