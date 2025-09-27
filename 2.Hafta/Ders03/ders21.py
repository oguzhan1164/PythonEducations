#Sözlük + Fonksiyon: Öğrenci Not Ortalaması
# Bir öğrencinin notlarının ortalamasını hesaplayan fonksiyon
# Öğrenci bilgileri bir sözlük (dictionary) içinde tutulacak
# Fonksiyon, öğrencinin not ortalamasını return ile döndürecek
"""
def ogrenci_ortalama_hesapla(ogrenci):
    notlar = ogrenci["notlar"]
    ortalama = sum(notlar) / len(notlar)
    return ortalama

# Kullanım
ogrenci = {"ad": "Ali", "notlar": [70, 85, 90, 65]}
ortalama = ogrenci_ortalama_hesapla(ogrenci)
print(f"{ogrenci['ad']} ortalaması: {ortalama:.2f}")
"""
def student_score_average(student):
    total = 0
    for score in student['scores']:
        total += score
    average_score = total / len(student['scores'])
    return average_score
print(student_score_average({"ad":"Oğuzhan","scores":[70,80,90,65]}))