import random
import csv
from itertools import chain

# 이름 생성기 클래스
class NameGenerator:
    surnames = []
    givennames = []
   # 이름 기본값 설정
    def __init__(self):
        #성
        with open('datas/surname.txt', 'r', encoding='utf-8') as file: #파일열기
            cvsreader = csv.reader(file) # cvs 리더 객체 생성 -> 한줄씩 순회함
            list_surname = [sn for sn in cvsreader] # 각 줄인 sn을 list에 저장
            surname_list = list(chain(*list_surname)) # chain(*) 붙이기, 평탄화
            self.surnames = [n.strip() for n in surname_list] # list 순회하며 앞뒤공백 제거과정
        #이름
        with open('datas/givenname.txt', 'r', encoding='utf-8') as file:
            cvsreader = csv.reader(file)
            list_givenname = [gn for gn in cvsreader]
            givenname_list = list(chain(*list_givenname))
            self.givennames = [n.strip() for n in givenname_list]
    # 랜덤 이름 생성
    def generate_name(self):
        surname = random.choice(self.surnames)
        givenname = random.choice(self.givennames)
        fullname = surname + givenname
        return fullname