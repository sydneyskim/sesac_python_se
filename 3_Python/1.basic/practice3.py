# 201
# "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.

# def print_coin():
#     print("비트코인")

# 202
# 201번에서 정의한 함수를 호출하라.

# print_coin()

# 203
# 201번에서 정의한 print_coin 함수를 100번호출하라.

# for i in range(100):
#     print_coin()

# 204
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.

# def print_coins():
#     for i in range(100):
#         print("비트코인")

# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# hello()
# def hello():
#     print("Hi")
# 실행 예
# NameError: name 'hello' is not defined

# 함수가 정의되기 전에 호출되었기 때문

# 206
# 아래 코드의 실행 결과를 예측하라.
# def message() :
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# A
# B
# C
# A
# B

# 207
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# A
# C
# B

# 208
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# A
# C
# B
# E
# D

# 209
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()

# B
# A

# 210
# 아래 코드의 실행 결과를 예측하라.
# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()

# B
# C
# B
# C
# B
# C
# A

# 211
# 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")

# 안녕
# Hi

# 212
# 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)

# 7
# 15

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'

# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.

# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int

# 같은 타입 두개가 아닌 다른 타입의 두개가 입력됨

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.

# def print_with_smile(string):
#     print(string + ":D")

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

def print_with_smile(string):
    print(string + ":D")

# print_with_smile("안녕하세요")

# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.

# def print_upper_price(price):
#     print(price * 1.3)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.

# def print_sum (a, b) :
#     print (a + b)

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# print_arithmetic_operation(3, 4)
# 3 + 4 = 7
# 3 - 4 = -1
# 3 * 4 = 12
# 3 / 4 = 0.75

# def print_arithmetic_operation(a, b):
#     print(a, "+", b, "=", a + b)
#     print(a, "-", b, "=", a - b)
#     print(a, "*", b, "=", a * b)
#     print(a, "/", b, "=", a / b)

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.

# def print_max(a, b, c):
#     max_val = 0
#     if a > max_val :
#         max_val = a
#     if b > max_val :
#         max_val = b
#     if c > max_val :
#         max_val = c
#     print(max_val)

# 221
# 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# print_reverse("python")
# nohtyp

# def print_reverse(string) :
#     print(string[::-1])

# 222
# 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# print_score ([1, 2, 3])
# 2.0

# def print_score(score_list) :
#     print(sum(score_list)/len(score_list))

# 223
# 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# print_even ([1, 3, 2, 10, 12, 11, 15])
# 2
# 10
# 12

# def print_even (my_list) :
#     for i in my_list :
#         if i % 2 == 0 :
#             print(i)

# 224
# 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 이름
# 나이
# 성별

# def print_keys(dic):
#     for keys in dic.keys():
#         print(keys)

# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# print_value_by_key  (my_dict, "10/26")
# [100, 130, 100, 100]

# def print_value_by_key (my_dict, key) :
#     print(my_dict[key])

# 226
# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# print_5xn("아이엠어보이유알어걸")
# 아이엠어보
# 이유알어걸

# def print_5xn(line):
#     chunk_num = int(len(line) / 5)
#     for i in range(chunk_num + 1) :
#         print(line[i * 5: i * 5 + 5])

# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

# def print_mxn(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1) :
#         print(line[x * num: x * num + num])

# 228
# 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# calc_monthly_salary(12000000)
# 1000000

# def calc_monthly_salary(annual_pay) :
#     monthly_pay = int(annual_pay / 12)
#     return monthly_pay

# 229
# 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(a=100, b=200)

# 왼쪽: 200
# 오른쪽: 100

# 230
# 아래 코드의 실행 결과를 예측하라.
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)
# my_print(b=100, a=200)

# 231
# 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)

# 에러 발생

# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# make_url("naver")
# www.naver.com

# def make_url(string) :
#     url = "www." + string + ".com"
#     return url

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']

# def make_list (string) :
#     my_list = []
#     for 변수 in string :
#         my_list.append(변수)
#     return my_list

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

# def pickup_even(items):
#     result = []
#     for item in items:
#         if item % 2 == 0:
#             result.append(item)
#     return result

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# convert_int("1,234,567")
# 1234567

# def convert_int (string) :
#     return int(string.replace(',', ''))

# 236
# 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 22

# 237
# 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)

# 22

# 238
# 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     return num * 10
# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 140

# 239
# 아래 코드의 실행 결과를 예측하라.
# def 함수1(num) :
#     return num + 4
# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)
# c = 함수2(10)
# print(c)

# 16

# 240
# 아래 코드의 실행 결과를 예측하라.
# def 함수0(num) :
#     return num * 2
# def 함수1(num) :
#     return 함수0(num + 2)
# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)
# c = 함수2(2)
# print(c)

# 28

# 241 현재시간
# datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()
# print(now)

# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()
# print(now, type(now))

# 243 timedelta
# datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.

# import datetime

# now = datetime.datetime.now()

# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)

# 244 strftime
# 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# 18:35:01 

# import datetime

# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))

# 245 strptime
# datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다. "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.

# import datetime

# day = "2020-05-04"
# ret = datetime.datetime.strptime(day, "%Y-%m-%d")
# print(ret, type(ret))
      
# 246 sleep 함수
# time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.

# import time
# import datetime

# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)

# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.

# 248 os 모듈
# os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.

# import os
# ret = os.getcwd()
# print(ret, type(ret))

# 249 rename 함수
# 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.

# import os
# os.rename("C:/Users/hyunh/Desktop/before.txt", "C:/Users/hyunh/Desktop/after.txt")

# 250 numpy
# numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.

# import numpy
# for i in numpy.arange(0, 5, 0.1):
#     print(i)
