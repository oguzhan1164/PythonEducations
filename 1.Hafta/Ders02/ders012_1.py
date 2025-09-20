gun = int(input("haftanın kaçıncı günü "))

match gun:
    case 1 | 3 | 6:
        print("bugün bootcamp var")
    case 2 | 4 | 5 | 7:
        print("bugün bootcamp yok")
   
    case _ :
        print("hatalı gün girşi")
