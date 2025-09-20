carpim = 1
adet = 0
girilen_sayilar = ""
while True:
    sayi = int(input("bir sayı giriniz"))
    if (sayi == 0) and adet < 10:
        continue
    carpim *= sayi
    adet +=1
    girilen_sayilar += str(sayi) + " - "

    if adet == 10:
        print("10 adet 0 dan farklı sayı girdiniz")
        print("girilen sayıların çarpımı: ",carpim)
        print("girilen sayılar: ",girilen_sayilar)
        break
