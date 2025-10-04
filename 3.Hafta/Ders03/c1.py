# Scope, bir değişkenin, fonksiyonun veya nesnenin nerede tanımlandığı ve nerelerden erişilebildiği bilgisidir.
# Python’da her isim (değişken, fonksiyon, sınıf vb.) bir kapsam (scope) içinde yaşar.
# Bu kapsam, o ismin geçerli olduğu bölgeyi belirler.

# Python, isim araması yaparken LEGB kuralını takip eder:

# L Local Mevcut fonksiyon/metot içinde tanımlananlar
# E Enclosing İç içe fonksiyon varsa, dıştaki fonksiyonun scope’u
# G Global Modül (dosya) seviyesinde tanımlananlar
# B Built-in Python’un yerleşik isimleri (len,print,int, vs.)
#Python bir ismi ararken: Local → Enclosing → Global → Built-in sırasıyla bakar.

#local spoce

#def fonksiyon():
#  x = 500      #Değişken tanımlı olduğu fonksiyonun scope u kadar tanımlıdır
#  print(x)

#Fonksiyonlar içinde scope
#def ustFonksiyon():
#   x=300
#   def altFonksiyon():
#       print(x)
#       y=500
#   print(y) #alt fonksiyondaki veri üst fonksiyondan erişilemediği için hata verir
#   altFonksiyon()

#ustFonksiyon()

#global scope
#global değişkenler ana kod alanında tanımlanır ve heryerden erişilebilir

# x = 300

# def myfunc():
#   print(x)

# myfunc()

# print(x)

#global ve yerel local değişkenler
#sayi = 500

#def myfunc():
#    sayi = 200
#    print(sayi)

#myfunc()

#print(sayi)

#global keyword ile global değişkenlere erişim ve değişiklikler yapma

#sayi = 500

#def fonksiyon():
#    global sayi
#    sayi = 250
#    print(sayi)
#print(sayi)
#fonksiyon()
#print(sayi)
#farklı bi örnek global keyword e

# def fonksiyon():
#     global sayi
#     sayi = 250
#     print(sayi)

# fonksiyon()
# print(sayi)


#nonlocal keyword ile içerdeki fonksiyon versine dışardan erişim sağlama

def ustFonksiyon():
    isim="hulya"
    def altFonksiyon():
        nonlocal isim
        isim="gulsum"
    print(isim)
    altFonksiyon()
    print(isim)
    return isim
#print(isim) nonlocal ile global e değişken tanımlanmadığı için bu satırda isim değişkenine ulaşılamıyor

ustFonksiyon()
