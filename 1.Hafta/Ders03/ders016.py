metin = input("Metin giriniz")
sayac = 0

for harf in metin:
    if harf == "a" or harf == "A": #bunun yerine harf.lower() ya da harf.upper() metodu ile hepsini 1 çeşide çevirip öyle de if ile arayabiliriz
        sayac +=1

print(f"Kurduğunuz cümlede {sayac} kadar a harfi var")
