demet = (24,8, 2.5,"Mert", True,"Mert",["Mert","Seçme","CEng"],(24,8,2.5,True,"Mert",[""]))
print(demet)
print(type(demet))

pazar = ["elma","armut","salatalık","marul"]
pazarDemeti = tuple(pazar)
print(pazarDemeti)

print(demet.index("Mert"))
print(demet.count("Mert"))

for eleman in demet:
    print(eleman)
#tuple la veri sonradan eklenmediği için listeye çevrilip veri eklenip tekrar tuple a dönüştürüldü
dlist = list(demet)
dlist[1] = "can"
print(dlist)
demet = tuple(dlist)
print(demet)

print(demet[:3])
print(demet[::-1])
