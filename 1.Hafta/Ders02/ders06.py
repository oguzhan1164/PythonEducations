yol=float(input("ne kadar yol gittiniz "))
zaman = float(input("ne kadar zamanda gittiniz "))
hiz=yol/zaman

if hiz >= 132:
    print(f"hız sınırını aştınız hızınız : {hiz}")
    print(f"hız sınırını {hiz-132} kadar aştınız")
else:
    print(f"hız sınırını aşmadınız hızınız : {hiz}")
    print("hız kurallarına uyduğunuz için teşekkürler")