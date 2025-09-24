hafta_ici = {"pazartesi":1,"sali":2}
hafta_sonu = {"cumartesi":6,"pazar":7}

hafta_ici.update(hafta_sonu)
print("birleşik günler", hafta_ici)

gun = "persembe"

if gun in hafta_ici:
    print("gün kayıtlı")
else:
    print("kayıtlı gün değil")

print(len(hafta_ici))