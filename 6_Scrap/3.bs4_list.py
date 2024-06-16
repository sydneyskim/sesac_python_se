# pip install bs4

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
    <title>간단한 예제</title>
</head>
<body>
    <div class="container">
    <h1>안녕하세요</h1>
    <p>이것은 간단한 html 예제입니다.</p>
    </div>
    <a href="https://www.naver.com">네이버 링크</a>
    <img src = "example.jpg" alt="예제 이미지">
    <img src = "example2.jpg" alt="예제 이미지2" width="500", height="600">
    <div class="content">
    <ul>
        <li>항목1</li>
        <li>항목2</li>
        <li>항목3</li>
        <li>항목4</li>
    </ul>
    </div>
    <div id="footer">
        <p>Copyright C 2024. 이 페이지 내거임</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, 1xml
# print(soup)
# print(html_doc)
# print(html_doc.head)
# print(soup.p.text)

list_items = soup.ul.find_all('li')
# print(list_items)
# for li in list_items:
#     print(li.text)
# print(list_items[1].text)
    
# 클래스가 container인 항목 가져오기
container_div = soup.find('div', class_='container')
# print(container_div.h1.text)
# print(container_div.p.text)

# footer를 가져다가 그 footer안에 있는 글자를 출력하시오
footer_div = soup.find('div', id ='footer')
# print(footer_div.p.text)

content_ul = soup.find('div', class_='content').ul
# print(content_ul)

# for li in content_ul.find_all('li'):
#     print(li.text)

link_tag = soup.a # 가장 먼저 dom에서 잡하는 a 태그
print(link_tag.text)
naver_link = link_tag["href"]
print(link_tag["href"])

# import requests
# response = requests.get(naver_link)
# print(response.text)

img_tag = soup.img
print(img_tag["src"])
print(img_tag["alt"])

img_tags = soup.find_all('img')
img_tag1 = img_tags[0]
img_tag2 = img_tags[1]
print(f"이미지태그1: ", img_tag1)
print(f"이미지태그2: ", img_tag2)

print(f"소스:  {img_tag1.get('src')}, alt글자: {img_tag1['alt']}, width: {img_tag1.get('width','너비없음')}")
# 있는지 없는지 확인할 때는 .get() 추가!!
print(f"소스:  {img_tag2['src']}, alt글자: {img_tag2['alt']}, width: {img_tag2['width']}")