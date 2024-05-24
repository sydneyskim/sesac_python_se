import random

# 한글 이름을 만드려면?
surname = ['김', '이', '박', '최', '정']
middlename = ['수', '민', '태', '여', '승']
lastname = ['원', '림', '미', '은', '희']
names = ['John', 'Jane', 'Michael', 'Emily']

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    # return random.choice(names)
    return name

for _ in range(10):
    print(generate_name())