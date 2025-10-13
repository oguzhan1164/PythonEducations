class futbolcu():
    kosu = "koşabilir"
    depar = "depar atar"
    maas = 500
    def __init__(self,ayak="sağ"):
        self.mevki = "orta"
        self.ayak = ayak
    pass
class basketbolcu():
    turnike = "turnike atabilir"
    ucluk = "üçlük atabilir"
    maas = 750
    def __init__(self,boy):
        self.bolge = "ileri"
        self.boy = boy
    pass
class multisporcu(basketbolcu,futbolcu):
    def __init__(self,ayak,boy):
        basketbolcu.__init__(self,boy)
        futbolcu.__init__(self,ayak)
    pass
mahmut = multisporcu("sol",190)
print(mahmut.turnike)
print(mahmut.kosu)
print(mahmut.maas)
print(mahmut.bolge)
print(mahmut.mevki)
print(mahmut.ayak)
print(mahmut.boy)