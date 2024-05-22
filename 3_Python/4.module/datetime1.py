# https://docs.python.org/ko/3/library/datetime.html
import datetime # 객체라 객체 안의 멤버를 부르기 위해

# 모듈명, 객체명, 함수명

# 모듈명.함수명

# 현재 시간 출력
current_time = datetime.datetime.now()
print(current_time)

# 내가 원하는 시간 생성
my_time = datetime.datetime(2024, 1, 1, 10, 30, 0)
print(my_time)