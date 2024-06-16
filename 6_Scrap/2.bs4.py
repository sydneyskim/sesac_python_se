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
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, 1xml
print(soup)
print(html_doc)
# print(html_doc.head) # 오류
print(soup.body.h1.text)
print(soup.p.text) # body 밖에 있는 모든 p까지