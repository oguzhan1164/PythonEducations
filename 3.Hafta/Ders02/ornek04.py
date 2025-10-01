import json

# Python objesini JSON string'e çevirme
data = {"isim": "Ali", "yas": 30, "sehirler": ["İstanbul", "Ankara"]}
data2={"FirstName":"Liza","LastName":"Bon","age":35,"e-posta":"lizabon@example.com"}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str, type(json_str))
json_str2 = json.dumps(data2,ensure_ascii=False,indent=2)

# JSON string'ini Python objesine çevirme
parsed = json.loads(json_str)
print(type(parsed))
print(parsed["isim"])  # Ali

parsed2 = json.loads(json_str2)
print(parsed2["LastName"])

# Dosyaya JSON yazma
with open("veri.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# JSON dosyasını okuma
with open("veri.json", "r", encoding="utf-8") as f:
    okunan = json.load(f)
    print(okunan)
    