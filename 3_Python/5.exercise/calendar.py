# import calendar

# print(calendar.month(2024,5))

# year = int(input("연도를 입력하세요: "))
# month = int(input("월을 입력하세요: "))

# print(calendar.month(year, month))


# 평달 윤달 구분하기
def isLeapYear(year):
   return year % 4 == 0 and year % 100 != 0 and year % 400 == 0

# 마지막날의 날짜
def lastDay(year, month):
    m = [31, 28, 31, 30, 31, 30, 31, 30, 30, 31, 30, 31 ]
    m[1] = 29 if isLeapYear(year) else 28
    return m[month - 1]

# 1년 1월 1일부터 지나온 날짜
def totalDay(year, month, day):
    # 작년까지 전체 날짜수
    total = (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    for i in range(1,month):
        total += lastDay(year, i)
    return total + day

# 요일 정해주기
def weekDay(year, month, day):
    return totalDay(year,month,day) % 7


# print_calendar(2024,5)
def print_calendar(year, month):
    print('-' * 22)
    print(f"     {year}년 {month}월")
    print('-' * 22)
    print(" 일 월 화 수 목 금 토 ")
    print('-' * 22)

    # 시작 요일을 맞추기 위해 공백 출력
    start_day = weekDay(year, month, 1)
    for _ in range(start_day):
        print("    ", end="")

    # 각 날짜 출력
    for day in range(1, lastDay(year, month) + 1):
        print(f"{day:2d} ", end="")
        if (start_day + day) % 7 == 0:
            print()
    print('\n' + '-' * 22)

# 년도와 달을 동시에 입력받기
input_str = input("년도와 달을 입력해주세요 (예: 2024 5): ")
year, month = map(int, input_str.split())

print_calendar(year, month)