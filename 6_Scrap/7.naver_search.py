import requests
from bs4 import BeautifulSoup

base_url = "https://search.naver.com/search.naver"

def naver_search(query):
    params = {"query": query}

    response = requests.get(base_url, params=params)
    return response.text

def extract_main_pack_div(html):
    soup = BeautifulSoup(html, 'html.parser')
    main_pack_div = soup.find("div", id="main_pack")
    return main_pack_div

query = "파이썬 프로그래밍"
soup = naver_search(query)

main_pack_div = extract_main_pack_div(soup)
# print(soup)

print(main_pack_div)
