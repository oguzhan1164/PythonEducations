#KKullanıcıdan bir metin al, onu tersten yazdır.
"""
yöntem2
kelime = input("Bir kelime girin: ")
ters=""
for i in range(len(kelime)-1, -1, -1):
    ters+=kelime[i]

print("Tersten yazılışı:", ters)

yöntem 3
cumle=input("Bir cümle giriniz")
sayac=0
for harf in cumle:
    sayac-=1
    print(cumle[sayac])
"""

#yöntem1
metin = input("Bir metin giriniz: ")
ters = ""

for harf in metin:
    ters = harf + ters  # verilen cümleden gelen her harf vermiş olduğumuz işlemde başa gelerek eklenir bu yüzden ters şekilde harf ekler

print("Tersi:", ters)