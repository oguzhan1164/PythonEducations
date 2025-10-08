"""
KALITIM TEMEL KAVRAMLARI:
- Üst sınıf (Parent class): Temel sınıf
- Alt sınıf (Child class): Üst sınıftan türeyen sınıf
- super(): Üst sınıfın metotlarına erişim
"""

class Ogrenci():
    ogrenci_dersler =["edebiyat","tarih"]
    def __init__(self,ad, soyad):
        self.ad = ad
        self.soyad = soyad

class BolumOgrenci(Ogrenci):
    bolum_dersler=["algoritma","veri yapıları"]
    def __init__(self,ad,soyad,bolum):
        super().__init__(ad,soyad)
        #Ogrenci.__init__(self,ad,soyad)
        self.bolum = bolum

class FOgrenci(BolumOgrenci):
    fakulte_dersleri = ["mühendislik tarihi"]
    def __init__(self,ad,soyad,bolum,fakulte):
        #BolumOgrenci.__init__(self,ad,soyad,bolum)
        super().__init__(ad,soyad,bolum)
        self.fakulte = fakulte
        super().bolum_dersler.append("bilgisayar mühendisliği tarihi")
        self.bolum_dersler = super().bolum_dersler

ogrenci1 = Ogrenci("ali","veli")
print(vars(ogrenci1),ogrenci1.ogrenci_dersler)
print(ogrenci1.ad, ogrenci1.soyad)

bogrenci1 = BolumOgrenci("Neslihan","Can","Makine")
print(bogrenci1.ad, bogrenci1.soyad,bogrenci1.ogrenci_dersler,bogrenci1.bolum,bogrenci1.bolum_dersler)