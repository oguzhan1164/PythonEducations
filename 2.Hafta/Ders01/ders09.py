#küme tanımlarken {} parantezleri arasında tuple lar () parantezi içinde listeler [] parantezi içerisinde tanımlanır
ogrenciler = {"ali","veli","can","canan","yiğit","can"} 
print(ogrenciler,type(ogrenciler))
#boskume = set()
#print(boskume)
print(len(ogrenciler))

#ogrenciler.pop()
#print(ogrenciler)

for ogrenci in ogrenciler:
    print(ogrenci)

print("seçil" in ogrenciler)

ogrenciler.add("seçil")
print(ogrenciler)

ogrenciler.remove("veli")
print(ogrenciler)