"""
versiyon1
sayi = int(input("bir sayı giriniz"))
ssayi = str(sayi)
toplam = 0
for rakam in ssayi:
    kup = int(rakam)**len(ssayi)
    toplam +=kup
    print(rakam, kup, toplam)
if toplam == sayi:
    print(f"girilen {sayi} bir armstrong sayısıdır")
"""
for i in range(1000):
    sayi = i
    ssayi = str(sayi)
    toplam = 0
    for rakam in ssayi:
        kup= int(rakam)**len(ssayi)
        toplam += kup
        # print(rakam, kup, toplam)
    if toplam == sayi:
        print(sayi,"sayisi bir armstrong sayısıdır")