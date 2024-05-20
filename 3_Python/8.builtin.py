# 빌트인함수
# while True: # 조건문이 '참'인 동안 실행한다.
#     a = input('숫자를 입력하세요: ')
#     print(a)

# 미션3. 숫자를 두개 입력받아서, 덧셈 결과를 출력하시오.
str_a = input('첫번째 숫자를 입력하세요: ')
str_b = input('두번째 숫자를 입력하세요: ')

# input값의 모든 것을 다 문자열로 처리된다
# 우리가 해야할 것은 형변환... type
# type casting = 타입을 변경한다
int_a = int(str_a)
int_b = int(str_b)

print(f'두 숫자의 합은 {int_a + int_b} 입니다')