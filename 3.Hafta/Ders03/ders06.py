#dosya silme işlemleri
import os

bulundugum_dizin = os.path.dirname(os.path.abspath(__file__))

dosya_adi = bulundugum_dizin+"/"+"deneme.txt"

#os.remove(bulundugum_dizin+"/deneme.txt")


if os.path.exists(dosya_adi):
  os.remove(dosya_adi)
else:
  print("silinecek dosya bulunamadı")