# 001 print 기초
# 화면에 Hello World 문자열을 출력하세요.

# print('Hello World')

# 002 print 기초
# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)

# print("Mary's cosmetics")

# 003 print 기초
# 화면에 아래 문장을 출력하세요. (중간에 "가 있음에 주의하세요.)
# 신씨가 소리질렀다. "도둑이야".

# print('신씨가 소리질렀다. "도둑이야".')

# 004 print 기초
# 화면에 C:\Windows를 출력하세요.

# print('C:\Windows')

# 005 print 탭과 줄바꿈
# 다음 코드를 실행해보고 \t와 \n의 역할을 설명해보세요.
# print("안녕하세요.\n만나서\t\t반갑습니다.")

# \t->탭 \n 줄바꿈

# 006 print 여러 데이터 출력
# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.
# print ("오늘은", "일요일")

#오늘은 일요일

# 007 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver;kakao;sk;samsung

# print('naver','kakao','sk','samsung', sep=";")

# 008 print 기초
# print() 함수를 사용하여 다음과 같이 출력하세요.
# naver/kakao/sk/samsung

# print('naver','kakao','sk','samsung', sep="/")

# 009 print 줄바꿈
# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.
# print("first");print("second")

# print("first", end="");print("second")

# 010 연산 결과 출력
# 5/3의 결과를 화면에 출력하세요.

# print(5/3)

# 011 변수 사용하기
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

# 삼성전자 = 50000
# 총평가금액 = 삼성전자 * 10
# print(총평가금액)

# 012 변수 사용하기
# 다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
# 항목	값
# 시가총액	298조
# 현재가	50,000원
# PER	15.79

# 시가총액 = 298000000000000
# 현재가 = 50000
# PER = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(PER, type(PER))

# 013 문자열 출력
# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
# >> s = "hello"
# >> t = "python"
# 두 변수를 이용하여 아래와 같이 출력해보세요.
# 실행 예:
# hello! python

# s = "hello"
# t = "python"
# print(s + "! " + t)

# 014 파이썬을 이용한 값 계산
# 아래 코드의 실행 결과를 예상해보세요.
# >> 2 + 2 * 3 

# print(2 + 2 * 3)
# 8

# 015 type 함수
# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
# >> a = 128
# >> print (type(a))
# <class 'int'>
# 아래 변수에 바인딩된 값의 타입을 판별해보세요.
# >> a = "132"

# a = "132"
# print(type(a))
# <class 'str'>

# 016 문자열을 정수로 변환
# 문자열 '720'를 정수형으로 변환해보세요.
# >> num_str = "720"

# num_str = "720"
# num_int = int(num_str)
# print(num_int)

# 017 정수를 문자열 100으로 변환
# 정수 100을 문자열 '100'으로 변환해보세요.
# num = 100

# num = 100
# str = str(num)
# print(str)

# 018 문자열을 실수로 변환
# 문자열 "15.79"를 실수(float) 타입으로 변환해보세요.

# str = "15.79"
# flt = float(str)
# print(flt)

# 019 문자열을 정수로 변환
# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
# year = "2020"

# year = "2020"
# print(int(year)-2)
# print(int(year)-1)
# print(int(year))

# 020 파이썬 계산
# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

# ac_monthly = 48584
# print(ac_monthly*36)

# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# >> letters = 'python'
# Copy실행 예
# p t

# lang = 'python'
# print(lang[0], lang[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# >> license_plate = "24가 2210"
# 실행 예: 2210

# license_plate = "24가 2210"
# print(license_plate[-4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
# >> string = "홀짝홀짝홀짝"
# 실행 예:
# 홀홀홀

# string = "홀짝홀짝홀짝"
# print(string[::2])

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
# >> string = "PYTHON"
# 실행 예:
# NOHTYP

# string = "PYTHON"
# print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# >> phone_number = "010-1111-2222"
# 실행 예
# 010 1111 2222

# phone_number = "010-1111-2222"
# phone_number2 = phone_number.replace("-"," ")
# print(phone_number2)

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# 실행 예
# 01011112222

# phone_number = "010-1111-2222"
# phone_number2 = phone_number.replace("-","")
# print(phone_number2)

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# >> url = "http://sharebook.kr"
# 실행 예:
# kr

# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
# >> lang = 'python'
# >> lang[0] = 'P'
# >> print(lang)

# TypeError: 'str' object does not support item assignment

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# >> string = 'abcdfe2a354a32a'
# 실행 예:
# Abcdfe2A354A32A

# string = 'abcdfe2a354a32a'
# string = string.replace("a","A")
# print(string)

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
# >> string = 'abcd'
# >> string.replace('b', 'B')
# >> print(string)

# abcd

# 031 문자열 합치기
# 아래 코드의 실행 결과를 예상해보세요.
# >> a = "3"
# >> b = "4"
# >> print(a + b)

# 34

# 032 문자열 곱하기
# 아래 코드의 실행 결과를 예상해보세요.
# >> print("Hi" * 3)

# HiHiHi

# 033 문자열 곱하기
# 화면에 '-'를 80개 출력하세요.
# 실행 예:
# --------------------------------------------------------------------------------

# print("-" * 80)

# 034 문자열 곱하기
# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# >>> t1 = 'python'
# >>> t2 = 'java'
# 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# 실행 예:
# python java python java python java python java

# t1 = 'python'
# t2 = 'java'
# t3 = ' '

# print(t1 + t2 + t3 + t1 + t2 + t3 + t1 + t2 + t3)

# 035 문자열 출력
# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: %s 나이: %d" %(name1, age1))
# print("이름: %s 나이: %d" %(name2, age2))

# 036 문자열 출력
# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print("이름: {} 나이: {}".format(name1, age1))
# print("이름: {} 나이: {}".format(name2, age2))

# 037 문자열 출력
# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.

# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13

# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

# 038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"

# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",","")
# 타입변환 = int(컴마제거)
# print(타입변환)

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"

# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "

# data = "   삼성전자    "
# data1 = data.strip()
# print(data1)

# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"

# ticker = "btc_krw"
# upper_ticker = ticker.upper()
# print(upper_ticker)

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"

# ticker = "BTC_KRW"
# lower_ticker = ticker.lower()
# print(lower_ticker)

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

# a = "hello"
# a = a.capitalize()

# 044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"

# file_name = "보고서.xlsx"
# file_name.endswith("xlsx")

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"

# file_name = "보고서.xlsx"
# file_name.endswith(("xlsx","xls"))

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
# file_name = "2020_보고서.xlsx"

# file_name = "2020_보고서.xlsx"
# file_name.startswith("2020")

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"

# a = "hello world"
# a.split()

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"

# ticker = "btc_krw"
# ticker.split("_")

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"

# date = "2020-05-01"
# date.split("-")

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "

# data = "039490     "
# date = data.rsplit()

# 051 리스트 생성
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)
# 순위	영화
# 1	   닥터 스트레인지
# 2    스플릿
# 3	   럭키

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

# 052 리스트에 원소 추가
# 051의 movie_rank 리스트에 "배트맨"을 추가하라.

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("베트맨")
# print(movie_rank)

# 053
# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']

# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)

# 054
# movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# print(movie_rank)

# 055
# movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']

# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)

# 056
# lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트를 만들어라.
# >> lang1 = ["C", "C++", "JAVA"]
# >> lang2 = ["Python", "Go", "C#"]
# 실행 예:
# >> langs
# ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']

# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]

# langs = lang1 + lang2
# print(langs)

# 057
# 다음 리스트에서 최댓값과 최솟값을 출력하라. (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# 실행 예:
# max:  7
# min:  1

# nums = [1, 2, 3, 4, 5, 6, 7]
# print("max: ", max(nums))
# print("min: ", min(nums))

# 058
# 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 15

# nums = [1, 2, 3, 4, 5]
# print(sum(nums))

# 059
# 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]

# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))

# 060
# 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# 3.0

# nums = [1, 2, 3, 4, 5]
# avg = sum(nums)/len(nums)
# print(avg)

# 061
# price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# 출력 예시:
# [100, 130, 140, 150, 160, 170]

# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])

# 062
# 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [1, 3, 5, 7, 9]

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[::2])

# 063
# 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 실행 예:
# [2, 4, 6, 8, 10]

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])

# 064
# 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# 실행 예:
# [5, 4, 3, 2, 1]

# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 065
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 Naver

# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0],interest[2])

# 066 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print(''.join(interest))

# 067 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))

# 068 join 메서드
# interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# 출력 예시:
# 삼성전자
# LG전자
# Naver
# SK하이닉스
# 미래에셋대우

# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))

# 069 문자열 split 메서드
# 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# 이를 interest 이름의 리스트로 분리 저장하라.
# 실행 예시
# >> print(interest)
# ['삼성전자', 'LG전자', 'Naver']

# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)

# 070 리스트 정렬
# 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]

# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)

# 071
# my_variable 이름의 비어있는 튜플을 만들라.

# my_variable = ()
# print(type(my_variable))

# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화
# 1	닥터 스트레인지
# 2	스플릿
# 3	럭키

# movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

# 073
# 숫자 1 이 저장된 튜플을 생성하라.

# tuple = (1, )
# print(type(tuple))

# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# 튜플은 원소 값을 변경 할 수 없다.

# 075
# 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4

# 튜플 -> 괄호없이도 동작한다.

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')

# 변경할 수 없음. 새로 만들어야 함
# t = ('A', 'b', 'c') 

# 077
# 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')

# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# data = list(interest)

# 078
# 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']

# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# data = tuple(interest)

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)

# apple banana cake

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# (2, 4, 6, 8 ... 98)

# data = tuple(range(2, 100, 2))
# print(data)

# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4, 5]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _= scores
# print(valid_score)

# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,b,*valid_score = scores
# print(valid_score)

# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# a,*valid_score,b = scores
# print(valid_score)

# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.

# temp = { }

# 085
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
# 이름	희망 가격
# 메로나	1000
# 폴라포	1200
# 빵빠레	1800

# icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# print(icecream)

# 086
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
# 이름	희망 가격
# 죠스바	1200
# 월드콘	1500

# icecream = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
# icecream["죠스바"] = 1200
# icecream["월드콘"] = 1500
# print(icecream)

# 087
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# 실행 예:
# 메로나 가격: 1000

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# print("메로나가격: ", ice["메로나"])

# 088
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# ice['메로나'] = 1300

# print(ice)

# 089
# 다음 딕셔너리에서 메로나를 삭제하라.
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# del ice["메로나"]

# print(ice)

# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'

# 딕셔너리에 없는 키이기 때문

# 091 딕셔너리 생성
# 아래의 표에서, 아이스크림 이름을 키값으로, (가격, 재고) 리스트를 딕셔너리의 값으로 저장하라. 딕셔너리의 이름은 inventory로 한다.
# 이름	가격	재고
# 메로나	300	20
# 비비빅	400	3
# 죠스바	250	100

# inventory = {"메로나": [300, 200],
#              "비비빅": [400, 3],
#              "죠스바": [250, 100]}
# print(inventory)

# 092 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 가격을 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 300 원

# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}

# print(inventory["메로나"][0], "원")


# 093 딕셔너리 인덱싱
# inventory 딕셔너리에서 메로나의 재고를 화면에 출력하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 실행 예시:
# 20 개

# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}

# print(inventory["메로나"][1], "개")

# 094 딕셔너리 추가
# inventory 딕셔너리에 아래 데이터를 추가하라.
# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# 이름	가격	재고
# 월드콘	500	7
# 실행 예시:
# >> print(inventory)
# {'메로나': [300, 20], '비비빅': [400, 3], '죠스바': [250, 100], '월드콘': [500, 7]}

# inventory = {"메로나": [300, 20],
#               "비비빅": [400, 3],
#               "죠스바": [250, 100]}
# inventory["월드콘"] = [500, 7]
# print(inventory)

# 095 딕셔너리 keys() 메서드
# 다음의 딕셔너리로부터 key 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# ice = list(icecream.keys())
# print(ice)

# 096 딕셔너리 values() 메서드
# 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# value = list(icecream.values())
# print(value)

# 097 딕셔너리 values() 메서드
# icecream 딕셔너리에서 아이스크림 판매 금액의 총합을 출력하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# 출력 예시:
# 6700

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# print(sum(icecream.values()))

# 098 딕셔너리 update 메서드
# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가하라.
# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# 실행 예시:
# >> print(icecream)
# {'탱크보이': 1200,  '폴라포': 1200,  '빵빠레': 1800,  '월드콘': 1500,  '메로나': 1000,  '팥빙수':2700, '아맛나':1000}

# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}
# icecream.update(new_product)
# print(icecream)

# 099 zip과 dict
# 아래 두 개의 튜플을 하나의 딕셔너리로 변환하라. keys를 키로, vals를 값으로 result 이름의 딕셔너리로 저장한다.
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# 실행 예시:
# >> print(result)
# {'apple': 300, 'pear': 250, 'peach': 400}

# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)

# result = dict(zip(keys,vals))
# print(result)

# 100 zip과 dict
# date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성하라.
# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]
# 실행 예시:
# >> print(close_table)
# {'09/05': 10500, '09/06': 10300, '09/07': 10100, '09/08': 10800, '09/09': 11000}

# date = ['09/05', '09/06', '09/07', '09/08', '09/09']
# close_price = [10500, 10300, 10100, 10800, 11000]

# close_table = dict(zip(date, close_price))
# print(close_table)

