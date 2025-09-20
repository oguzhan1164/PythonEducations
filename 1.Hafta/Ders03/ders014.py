"""
Versiyon 1
sicaklik = 0
while sicaklik <= 200:
    sicaklik += 50
    if sicaklik == 100:
        print("Dikkat: Orta sıcaklık uyarısı !!!")
        continue
    elif sicaklik == 200:
        print("Fırınınız Hazır.")
        break
    print(f"Fırın {sicaklik}°C")
"""

sicaklik = 0
while sicaklik <=200:
    sicaklik +=50
    match sicaklik:
        case 100:
            print("Fırın sıcaklığı orta dereceye ulaştı")
            continue
        case 200:
            print("Fırın hazır")
            break
    print(f" fırın sıcaklığı {sicaklik}°C")
