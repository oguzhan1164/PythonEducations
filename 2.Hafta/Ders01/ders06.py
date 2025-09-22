sebze = ["pataes", "soğan"]
meyve = ["elma", "armut"]
sark = ["peynir", "bal"]
yesillik = ["maydanoz", "roka","semiz otu"]
# pazar_listesi = sebze+meyve+sark+yesillik
# print(pazar_listesi)
# print(len(pazar_listesi))

pazar_listesi = [sebze, meyve,"çekirdek", sark, yesillik]
print(pazar_listesi)
pazar_listesi.append("sütlaç")
print(pazar_listesi)
print(len(pazar_listesi))
print(pazar_listesi[0])
print(pazar_listesi[0][1])
print(pazar_listesi[4][2])
for kategori in pazar_listesi:
    print(kategori)
    if type(kategori) != list:
        continue
    for urun in kategori:
        print("\t",urun)