import requests
from bs4 import BeautifulSoup

url = "http://www.cine21.com/rank/boxoffice/domestic"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

rank = soup.select('li')

for names in rank:
    movie_rank = names.find('div', class_='mov_name')
    # print(movie_rank)
    

# print(rank)

### 못가져 오는 이유는.. 동적인 자바스크립트는 selenium을 설정해야한다고..?