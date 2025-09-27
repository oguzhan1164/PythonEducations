# En büyük sayıyı bulma
# Bir liste içindeki en büyük sayıyı bulan fonksiyon
# Fonksiyon, en büyük sayıyı return ile döndürecek
"""
def en_buyuk_bul(*args):
    return max(args)

def en_buyuk_bul(*args):
    if not args:
        return None
    return max(args)

# Kullanım
liste = [15, 8, 23, 4, 42, 11]
print("En büyük sayı:", en_buyuk_bul(liste))

def find_max(*args):
    max_number = args[0]
    for arg in args:
        if arg > max_number:
            max_number = arg
    return max_number

print("En büyük sayı:", find_max(15,8,23,4,42,11))
"""

def en_buyuk_bul(*args):
    if len(args) == 1:
        return args[0]
    else:
        en_buyuk = en_buyuk_bul(*args[1:])
        return args[0] if args[0] > en_buyuk else en_buyuk

print(en_buyuk_bul(15,8,23,4,42,11))