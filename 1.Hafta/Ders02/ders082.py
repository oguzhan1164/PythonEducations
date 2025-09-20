sinif = int(input("hangi sınıfa gidiyorsun "))

if sinif == 0:
    print("Okul öncesi")
elif 1 <= sinif <= 4:
    print("İlkokul")
elif 5 <= sinif <= 8:
    print("Ortaokul")
elif 9 <= sinif <= 12:
    print("Ortaöğretim")
else:
    print("geçerli bir sınıf seviyeniz yok")