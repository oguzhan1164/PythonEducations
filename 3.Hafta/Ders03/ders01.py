#dosya işlemleri

isim = "Oguzhan"
yas = 26

# Bu bilgiyi bir dosyaya yazalım ki, sonra da okuyabilelim

"""
 Üç temel dosya formatı: 

.txt → düz metin
.csv → virgülle ayrılmış değerler (Excel benzeri)
.json → yapılandırılmış veri (web, API’lerde çok kullanılır)
"""

import os
bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))
dosya_adi = bulundugum_dizin + "/" + "kayit.txt"

# dosya = open("kayit.txt","w") # yazma modunda dosya açma 

# dosya.write(f"Merhaba {isim} , {yas}") # dosyanın içine veri yazdırma
# dosya.close() #dosyayı kapatma
# eğer dosya açar ve kapatmaz isek dosya kilitli kalır

#kapatma durumunu unutma ihtimaline karşı with ullanımı

with open("merhaba.txt", "w") as dosya: #yazma modunda dosya açıyoruz with ile
    dosya.write(f"Merhaba {isim} , {yas}") #içeriğine birşeyler yazıyoruz
# otomatik kapanır

"""
dosya açma modları 
w => yazma (varsa içeriği siler baştan yazar) eğer dosya yoksa dosyayı oluşturur
a => ekleme (dosyanın sonuna ekleme yapar) dosya yoksa oluşturur
r => dosyayı okur, dosya yoksa hata verir
x => dosyayı oluşturur, dosya varsa hata verir

t modu text default mode ve metin işlemek için
b binary mode (image dosyaları gibi)

rt text modunda okuma 

"""