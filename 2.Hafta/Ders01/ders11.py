#Kullanıcıdan not al, listeye ekle, 
# her adımda listeyi göster.

notlar=[]

print("NOT DEFTERİ")
print("Not defterinden çıkmak için 'çık' yazın")

while True:
    yeni_not = input("Notunuzu yazınız")
    if yeni_not.lower() == "çık":
        print("not defteri kapatılıyor")
        break
    notlar.append(yeni_not)
    print("Not eklendi.Güncel notlar:")
    for not_defteri in notlar:
        print(" - " + not_defteri)
    
