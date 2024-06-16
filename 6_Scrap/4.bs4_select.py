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
        <p>Copyright C <b>2024.</b> <i>이 페이지 내거임</i></p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser') # html.parser, 1xml

link_tag = soup.select_one('a')
print(link_tag)

all_imgs = soup.select('img')
print(all_imgs)
for img in all_imgs:
    print(img['src'])
    
content_div = soup.select_one('div_content') #div 아래에 있는  .content <- 클래스명
print(content_div)

footer_div = soup.select_one('div#footer')
print(footer_div)

li_lists = soup.select('div.content li') # div아래에 있는 content 클래스 아래에 있는 li들
print(li_lists)

li_lists = soup.find_all('div.content li') # find 시리즈는 태그명 등으로 검색하는 것
print(li_lists)

p_tag_div_footer = soup.select_one('div#footer p')
b_text = p_tag_div_footer.select_one('b')
i_text = p_tag_div_footer.select_one('i')

print(f"볼드텍스트: {b_text}, 이탤릭텍스트: {i_text}")