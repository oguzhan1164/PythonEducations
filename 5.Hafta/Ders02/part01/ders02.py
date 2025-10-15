# 1. Gerekli kütüphaneleri import edelim
import requests
from bs4 import BeautifulSoup
# 2. Basit bir web sitesinden veri çekelim
url = "http://google.com"
# 3. Web sitesine istek gönderelim
response = requests.get(url)
# 4. Durum kodunu kontrol edelim
print("status code: ",response.status_code)

#print(response.text)

# 5. İçeriği BeautifulSoup ile analiz edelim
soup = BeautifulSoup(response.text,"html.parser")

# 6. Sayfa başlığını alalım
print("sitenin başlığı ", soup.title.text)
print("sitenin scripti ", soup.script.text)
