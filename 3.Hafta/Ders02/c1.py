import math #Matematik kütüphanesi
import random
import datetime
"""

#en çok kullanılan modüllerden bazıları:
#math modülü matematiksel işlemler için kullanılır. 
print("=== MATH MODÜLÜ ===")
print("Pi sayısı:", math.pi)
print("2'nin üssü 3:", math.pow(2, 3))
print("Karekök 16:", math.sqrt(16)) 
print("Mutlak değer -5:", abs(-5))
print("Yuvarlama 4.7:", round(4.7))
print("Yuvarlama 4.4:", round(4.4))
print("En yakın tam sayı 4.5:", round(4.5))
print("En yakın tam sayı 4.6:", round(4.6))
print("En yakın tam sayı 4.4:", round(4.4))
print("cos",math.cos(math.radians(90)))

#random modülü rastgele sayılar üretmek için kullanılır.
print("\n=== RANDOM MODÜLÜ ===")    
print("0-1 arası rastgele sayı:", random.random())
print("1-10 arası rastgele sayı:", random.randint(1, 10))
print("1-100 arası rastgele sayı:", random.randint(1, 100))
print("1-5 arasında rastgele ondalıklı sayı türetme", random.uniform(1.0, 5.0))

renkler = ["kırmızı", "mavi", "yeşil"]
secilen = random.choice(renkler)
print("Seçilen renk:", secilen)

isimler = ["Ali", "Ayşe", "Mehmet"]
random.shuffle(isimler)
print(isimler)  # ['Mehmet', 'Ali', 'Ayşe']


#datetime modülü tarih ve saat işlemleri için kullanılır.
print("\n=== DATETIME MODÜLÜ ===")
simdi = datetime.datetime.now()
print("Şimdi:", simdi)
print("Yıl:", simdi.year)
print("Ay:", simdi.month)
print("Gün:", simdi.day)    
print("Saat:", simdi.hour)
print("Dakika:", simdi.minute)
print("Saniye:", simdi.second)
print("Mikrosaniye:", simdi.microsecond)
print("Haftanın günü (0-6):", simdi.weekday())  
print("Haftanın günü adı:", simdi.strftime("%A"))
print("Ay adı:", simdi.strftime("%B"))
print("Tarih formatı:", simdi.strftime("%d/%m/%Y")) 
print("Saat formatı:", simdi.strftime("%H:%M:%S"))
print("Tarih ve saat formatı:", simdi.strftime("%d/%m/%Y %H:%M:%S"))
print("ISO formatı:", simdi.isoformat())
print("Zaman damgası:", simdi.timestamp())
print("Yılın günü:", simdi.timetuple().tm_yday)
print("Haftanın günü (1-7):", simdi.isoweekday())
print("Haftanın günü adı (İngilizce):", simdi.strftime("%A"))
print("Ay adı (İngilizce):", simdi.strftime("%B"))
print("Haftanın günü adı (Türkçe):", simdi.strftime("%A").replace("Monday", "Pazartesi").replace("Tuesday", "Salı").replace("Wednesday", "Çarşamba").replace("Thursday", "Perşembe").replace("Friday", "Cuma").replace("Saturday", "Cumartesi").replace("Sunday", "Pazar"))
print("Ay adı (Türkçe):", simdi.strftime("%B").replace("January", "Ocak").replace("February", "Şubat").replace("March", "Mart").replace("April", "Nisan").replace("May", "Mayıs").replace("June", "Haziran").replace("July", "Temmuz").replace("August", "Ağustos").replace("September", "Eylül").replace("October", "Ekim").replace("November", "Kasım").replace("December", "Aralık"))
print("Yılın hafta sayısı:", simdi.isocalendar()[1])
print("Yılın hafta sayısı (alternatif):", simdi.strftime("%U"))
"""
import time #programın çalışırkenki zamanını yönetebilmek için bu kütüphane kullanıldı
import turtle
print("turtle kütüphanesi")
ekran = turtle.Screen()
ekran.bgcolor("yellow")
ok = turtle.Turtle()
ok.forward(100) #100 birim oku hareket ettirdik
ok.right(90) #90 derece sağ döndürdük
time.sleep(1) #her işlem arasında 1 saniye beklemek için kullandık
ok.forward(100) 
ok.right(90) 
time.sleep(1)
ok.forward(100) 
ok.right(90) 
time.sleep(1)
ok.forward(100) 
ok.right(90) 
time.sleep(1)
ok.penup()
ok.forward(110)
ok.pendown()
for _ in range(3):
    ok.forward(150)
    ok.right(120)
    time.sleep(1)


ekran.exitonclick()
#ok.done() # Çizimi bitir