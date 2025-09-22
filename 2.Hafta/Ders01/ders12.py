#1. yöntem
"""
import random
tutulan_sayi = random.randint(1, 10)

tahminler=[]

while True:
    tahmin=int(input("1-10 arası bir sayı tahmin ediniz"))
    if tahmin > 10 or tahmin < 0:
        print("1-10 arası bir sayı tahmin ediniz ")
        continue
    elif tahmin > tutulan_sayi:
        print("daha küçük bir sayı tahmin ediniz ")
        tahminler.append(tahmin)
    elif tahmin < tutulan_sayi:
        print("daha büyük bir sayı tahmin ediniz ")
        tahminler.append(tahmin)
    elif tahmin == tutulan_sayi:
        tahminler.append(tahmin)
        print(f"Tebrikler bildiniz önceki tahminler :{tahminler} ")
        break

"""
#2. yöntem
import random
tutulan_sayi = random.randint(1, 10)

tahminler=[]

while True:
    tahmin=int(input("1-10 arası bir sayı tahmin ediniz"))
    if tahmin > 10 or tahmin < 0:
        print("1-10 arası bir sayı tahmin ediniz ")
        continue
    elif tahmin > tutulan_sayi:
        print("daha küçük bir sayı tahmin ediniz ")
        tahminler.append(tahmin)
    elif tahmin < tutulan_sayi:
        print("daha büyük bir sayı tahmin ediniz ")
        tahminler.append(tahmin)
    elif tahmin == tutulan_sayi:
        tahminler.append(tahmin)
        print("Tebrikler bildiniz")
        break
print(tahminler)