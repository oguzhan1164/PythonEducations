# dosya oluşturma ve içine veri yazma
import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "kurs.txt"
metin = "\nTech İstanbul python bootcamp çok faydalı"
dosya = open(dosya_adi,"a",encoding="utf-8")
dosya.write(metin)
dosya.close()

#dosya açıp yazma
with open(dosya_adi, "a",encoding="utf-8") as dosya: #a yerine w olursa içeriği silinir öyle eklenir
  dosya.write("bu kurs toplam 80 saat sürecek")

#içeriğine veri eklenen dosyayı açıp okuma
with open(dosya_adi) as dosya:
  print(dosya.read())