gun = int(input("haftanın kaçıncı günündeyz"))

if gun == 1 or gun == 3 or gun == 6:
    print("Python bootcamp var")
elif gun == 2 or gun == 4 or gun == 5 or gun == 7:
    print("bugün bootcamp yok")
else:
    print("hatalı gün girişi yapıldı")