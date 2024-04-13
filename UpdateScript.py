import requests
from bs4 import BeautifulSoup
# github profil pin repolarının başlık, açıklama ve dili alan bir script
url = 'https://www.github.com/atalhatabak'
response = requests.get(url)
if response.status_code == 200:
    with open('atalhatabakGithub.html', 'w', encoding='utf-8') as f:
        f.write(response.text)
    print("HTML kaynağı başarıyla indirildi.")
else:
    print("Sayfa indirilemedi. HTTP hata kodu:", response.status_code)

with open('atalhatabakGithub.html', 'r', encoding='utf-8') as file:
    html_content = file.read()


data = {
    "repo1" : {"name":"", "desc":"", "lang":""},
    "repo2" : {"name":"", "desc":"", "lang":""},
    "repo3" : {"name":"", "desc":"", "lang":""},
    "repo4" : {"name":"", "desc":"", "lang":""},
    "repo5" : {"name":"", "desc":"", "lang":""},
    "repo6" : {"name":"", "desc":"", "lang":""},
}


soup = BeautifulSoup(html_content, 'html.parser')

for i in range(6):
    span_element = soup.find_all('span', class_='repo')
    datax = "repo"+str(i+1)
    if span_element:
        data[datax]["name"] = span_element[i].text.strip()
    else:
        data[datax]["name"] = "None"

for i in range(6):
    span_element = soup.find_all('p', class_='pinned-item-desc')
    datax = "repo"+str(i+1)
    if span_element:
        data[datax]["desc"] = span_element[i].text.strip()
    else:
        data[datax]["desc"] = "None"

for i in range(6):
    span_element = soup.find_all('span', itemprop='programmingLanguage')
    datax = "repo"+str(i+1)
    if span_element:
        data[datax]["lang"] = span_element[i].text.strip()
    else:
        data[datax]["lang"] = "None"
        
for i in range(6):
    datax = "repo"+str(i+1)
    print(data[datax])