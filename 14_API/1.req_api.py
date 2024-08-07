import requests

# 외부에 요청...
# 니가 가지고 있는 정보좀 주시오...

# 1. 특정 사용자의 정보 조회 하기 (예, 1번 사용자)
user_id = 1
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

response = requests.get(url)
post_data = response.json()
for comment in post_data:
    # print(comment)
    print(comment['title'])

print('-'*20)
# 2. 게시글 ID를 기준으로... 댓글 가져오기...
post_id = 1
url = f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments"

response = requests.get(url)
post_data = response.json()
for comment in post_data:
    print(comment['email'])