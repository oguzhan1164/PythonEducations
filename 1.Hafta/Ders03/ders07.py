#yontem 1
# cevap = input("pizza ister misiniz")
# while cevap == "evet":
#     print("buyrun pizzanız")
#     cevap = input("pizza ister misin")

#print("---"*20)
#yontem 2
cevap = bool(input("pizza ister misiniz"))
while cevap == True: #cevabın dolu olup olmadığına bakıyor(while cevap: şeklinde bırakılsaydı da aynı şekilde çalışırdı sadece klavyeden bir girdi olup olmadığına bakıyor ta ki boş bırakana kadar)
    print("buyrun pizzanız")
    cevap = bool(input("pizza ister misiniz"))