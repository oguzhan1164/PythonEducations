class Hayvan:
    def __init__(self, isim):
        self.isim = isim

    def ses_cikar(self):
        print("Bilinmeyen ses")

class Kopek(Hayvan):
    def ses_cikar(self):
        print("Hav hav!")

class Kus(Hayvan):
    def __init__(self, isim, kanat_uzunlugu):
        super().__init__(isim)  # Hayvan.__init__ çağrılıyor
        # super() kullanmak, kodun esnekliğini ve bakım kolaylığını artırır. 
        self.kanat_uzunlugu = kanat_uzunlugu
    def ses_cikar(self):
        print("Saldır Fenerbahçe!")
    def ucma(self):
        print("kuş uçuyor")

kopek1 = Kopek("Karabaş")
kopek1.ses_cikar()
kus1 = Kus("Kanarya",3.5)
print(vars(kus1))
kus1.ses_cikar()
kus1.ucma()