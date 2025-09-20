ad = input("Adınızı giriniz")
yas=int(input("Yaşınızı giriniz"))

for harf  in range(yas):
    print("{}. kere {}".format(harf+1,ad))


for ks in range(len(ad)):
    print("{} .kere {} {}. karakteri".format(ks+1,ad, ad[ks]))