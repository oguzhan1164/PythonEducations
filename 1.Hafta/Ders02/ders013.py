ad="RidvanCelikbas"

#soldan sağ 0 1 2 3 .....
#sağdan sola -1 -2 -3 ...

boyut = len(ad)
print(boyut)
print(ad[0])
print(ad[13])

print(ad[-1])
print(ad[-14])
#print(ad[baslangıç:bitis]) başlangıçtan itibaren alıcaksak print(ad[:6])
print(ad[0:6])
print(ad[:6])
print(ad[:6:1]) #başlangıçtan 6.karaktere kadar 1 er 1 er arttırarak eğer 2 yaparsak artış değerini 2 şer 2 şer ilerler
print(ad[:6:2])
print(ad[0:6:2]) #bir üstteki nin normal hali

print(ad[-10:-4:2])
print(ad[5::2]) #bitiş noktası verilmediği için sonuna kadar gider
print(ad[::]) #baştan sona gider
print(ad[::-1])

print("R" in ad)
print("K" in ad)
print("lik" in ad)

print(ad.upper())
print(ad.lower())
print(ad.isalnum())
print(ad.isdigit())