birlesik = ""

while True:
    metin = input("bir metin giriniz")
    if metin.lower()=="exit":
        print(birlesik)
        break
    else:
        birlesik += metin