meyve = ["elma", "ananas","çilek", "şeftali","muz","portakal","çilek"]
print(meyve)
#listenin sonuna veri eklemek için
meyve.append("limon")
print(meyve)
#count o veriden kaç tane olduğu index hangi indexte bulunduğunu gösterir
print(meyve.count("çilek"))
print(meyve.index("ananas"))
#insert istenen indexe veriyi ekler o indexteki veri bir ileri kayar 
meyve.insert(1,"muz")
print(meyve)
#bu yöntemle 1. indexteki veriyi değiştirmiş olduk
meyve[1] = "mandalina"
print(meyve)
#listeyi a-z ye sıralar türkçe karakterler listenin sonuna kayabilir
meyve.sort()
print(meyve)
#listeyi tersten sıralar
meyve.reverse()
print(meyve)
#listeye birden fazla veri ekleme işlemi
yeni_meyveler = ["armut", "üzüm"]
meyve.extend(yeni_meyveler)
print(meyve)
#listenin sonuna ayrı bir liste olarak ekledi listenin altında bir liste olmuş oldu
yeni_meyveler2 = ["karpuz", "mango"]
meyve.append(yeni_meyveler2)
print(meyve)
#indexsiz verilirse sondaki veri index verilirse o indexteki veriyi siler
meyve.pop()
print(meyve)
meyve.pop(2)
print(meyve)
#direkt veri yazılarak remove ile silinebilir
meyve.remove("ananas")
print(meyve)
#del ile beraber index verilerek veri silinebilir
del meyve[1]
print(meyve)
#listeyi temizler tamamı silinir
meyve.clear()
print(meyve)
#listenin kendisini siler
del meyve
print(meyve)
