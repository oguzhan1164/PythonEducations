gun = int(input("haftanın kaçıncı günü "))

match gun:
    case 1:
        print("Pazartesi")
    case 2:
        print("Salı")
    case 3:
        print("çarşamba")
    case 4:
        print("perşembe")
    case 5:
        print("cuma")
    case 6:
        print("cumartesi")
    case 7:
        print("pazar")
    case _ :
        print("hatalı gün girşi")
