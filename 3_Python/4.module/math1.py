import math

# 모둘명, 함수명

print(math.pi)

print(math.pow(5,2)) # 5의 2승 = 25

# 원의 넓이 : pi * r ^ 2
radius= 5
area = math.pi * math.pow(radius, 2)
print(f"반지름이 {radius} 인 원의 넓이는 {area} 입니다.")

# 로그 계싼
x = 2.718
log_value = math.log(x)
print("natural log ", log_value)