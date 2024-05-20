def hello():
    print('hello1')
    print('hello2')
    print('hello3')

hello()

def numbers(num1):
    result = num1 + 4
    if result < 10:
        return result
    
numbers(3)
print(numbers(3))

num1 = numbers(3)
num2 = numbers(6)

print(num1)
print(num1, num2)


# ------------------------------
# 미션1. 덧셈을 하는 함수를 작성하시오.
# 숫자 두개를 입력 받아서, 해당 숫자의 합산을 반납한다. 

def add1(number1, number2):
    sum = number1 + number2
    return sum

print(add1(4,5))
print(add1(55,70))

def add2(num1, num2): # 더 간결하게
    return num1 + num2

print(add2(2,3))


def add3(num1, num2):
    return num1, num2, num1+num2

print(add3(1,2)) # (1, 2, 3) -> 기본적으로 튜플에 담겨서 나온다

# 미션2, 덧셈함수 만들었으니... 뺄셈, 곱셈, 나눗셈 함수도 보기
# 모두 다 덧셈처럼 2개의 인자를 입력받아, 하나의 결과를 반환하시오

def sub(num1, num2):
    return num1 - num2

print(sub(5,2))

def mul(num1, num2):
    return num1 * num2

print(mul(4,9))

def div(num1, num2):
    return num1 / num2

print(div(6,3))