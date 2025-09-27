# Fibonacci serisi hesaplama
# Kullanıcıdan kaç terim istediğini alır ve Fibonacci serisini döner
""" 
def fibonacci(adet):
    seri = []
    a, b = 0, 1
    for _ in range(adet):
        seri.append(a)
        a, b = b, a + b
    return seri

# Kullanım
print("İlk 10 Fibonacci sayısı:", fibonacci(10))

def faktoriyel(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * faktoriyel(n-1)
print(faktoriyel(5))
"""
def yazTersten(metin):
    if len(metin) == 0:
        return metin
    else:
        #return metin[-1] + yazTersten(metin[:-1])
        return yazTersten(metin[1:]) + metin[0]
print(yazTersten("merhaba"))
print(yazTersten("python"))