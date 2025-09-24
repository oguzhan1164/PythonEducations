#hepsi aynı listeyi tanımlamak için kullanılabilir
sayilar = [1,2,3,4,5,6,7,8,9,10]
sayilar = list(range(1,11))
sayilar = [x for x in range(1,11)]

cifti_katla = {x:x*2 for x in sayilar}

print(cifti_katla)