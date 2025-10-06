# ÖRNEK 1: Basit Sınıf Tanımlama
class Araba:
    """Basit bir araba sınıfı"""
    hiz =10
    def __init__(self, marka, model, yil):
        # __init__ metodu: Yapıcı metod (constructor)
        # self: Oluşturulan nesneyi temsil eder
        self.marka = marka      # Özellik (attribute)
        self.model = model      # Özellik (attribute)
        self.yil = yil          # Özellik (attribute)
        self.hiz = Araba.hiz       # Varsayılan değer
    
    def bilgileri_goster(self):
        """Arabanın bilgilerini gösteren metod"""
        return f"{self.yil} {self.marka} {self.model}, Hız: {self.hiz} km/s"
    
    def hizlan(self, miktar):
        """Arabanın hızını artıran metod"""
        self.hiz += miktar
        return f"Hızlandı! Yeni hız: {self.hiz} km/s"
    
    def fren(self, miktar):
        """Arabanın hızını azaltan metod"""
        self.hiz = max(0, self.hiz - miktar)  # Hız negatif olamaz
        return f"Fren yapıldı! Yeni hız: {self.hiz} km/s"
    @classmethod
    def ortak_Hiz_arttir(cls,miktar):
        cls.hiz += miktar 

# Kullanım
Araba.ortak_Hiz_arttir(100)
araba1 = Araba("Toyota", "Corolla", 2022)
araba2 = Araba("Honda", "Civic", 2023)

print(araba1.bilgileri_goster())
print(araba2.bilgileri_goster())

araba1.hizlan(50)
print(araba1.bilgileri_goster())

araba1.fren(20)
print(araba1.bilgileri_goster())

araba3 = Araba("renault","megane",2025)
print(araba3.bilgileri_goster())
araba3.hizlan(30)
print(araba3.bilgileri_goster())


