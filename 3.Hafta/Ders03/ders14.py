#günlük yazma programı

from datetime import datetime

entry = input("Günlük notunuz: ")
tarih = datetime.now().strftime("%d-%m-%Y %H:%M")

with open("gunluk.txt", "a",encoding="utf-8") as f:
    f.write(f"[{tarih}] {entry}\n")