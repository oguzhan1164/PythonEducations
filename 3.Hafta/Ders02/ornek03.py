#şanslı yedili

import random

semboller = [1,2,3,4,5,6,7]
deneme = 0
while True:
    input("Oynamak için ENTER'a basın...")
    sonuc = [str(random.choice(semboller)) for _ in range(3)]
    print(" | ".join(sonuc))
    deneme += 1
    if sonuc[0] == sonuc[1] == sonuc[2]:
        print("🎉 JACKPOT!")
        print("deneme sayısı",deneme)
        break
    else:
        print("Tekrar dene!")