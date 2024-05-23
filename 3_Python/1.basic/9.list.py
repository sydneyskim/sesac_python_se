# list comprehension 리스트 컴프리헨션
# []
# [표현식 for 항목 in 반복 (조건문)]

# 1. 1부터 10까지의 숫자를 담는 리스트를 생성하시오.
nums = [num for num in range(1, 10)]
    # 최종표현할 변수명 (num) for 항목(num) in 반복(range(1, 10)

print(nums)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 위 숫자의 각 숫자의 제곱을 구하고 싶으면?
squares = [num ** 2 for num in range(1, 10)]
print(squares)
#[1, 4, 9, 16, 25, 36, 49, 64, 81]

# 3. 1부터 20까지 짝수로 이루어진 리스트
even_numbers = [num for num in range(1, 20 + 1) if num % 2 == 0]
print(even_numbers)
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 홀수
odd_numbers = [num for num in range(1, 20 + 1) if num % 2 == 1]
print(odd_numbers)
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# 4. 문자열의 각 글자를 대문자로 바꾼 리스트를 생성하시오 
word = 'hello'
# 원하는 결과1 = ['h', 'e', 'l', 'l', 'o']
letters = [char for char in word]
print(letters)
# 원하는 결과2 = ['H', 'E', 'L', 'L', 'O']
upper_letters = [char.upper() for char in word]
print(upper_letters)