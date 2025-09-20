#sayı tahmin oyunu

import random
tutulan_sayi = random.randint(1, 100)
sayac = 0
while True:
    tahmin = int(input("1-100 arası bir sayı tahmin ediniz "))
    if tahmin < 1 or tahmin > 100:
        print("1-100 arası bir sayı tahmin ediniz ")
        continue
    elif tahmin == tutulan_sayi:
        sayac +=1
        print(f"{sayac} denemede bildiniz tebrikler")
        
        break
    elif tahmin > tutulan_sayi:
        print("daha küçük bir sayı tahmin ediniz ")
        sayac +=1
    elif tahmin < tutulan_sayi:
        print("daha büyük bir sayı tahmin ediniz ")
        sayac +=1