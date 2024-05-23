# 미션1, 숫자 1~100까지 에서 숫자를 하나 생성하는 함수를 찾아서 출력하시오
import random

print(random.randint(1,100))

# 미션2. 주사위를 던지는 함수를 작성하시오
def roll_dice():
    return random.randint(1,6)
        
print("주사위를 던진 결과는: ", roll_dice())

# 미션3. 리스트에서 랜덤으로 요소를 선택하기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']

def choose_random_fruit(elements):
    return random.choice(elements)

print("선택된 과일은: ", choose_random_fruit(elements))

# 미션4. 랜덤으로 리스트 섞기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
numbers = [1, 2, 3, 4, 5]
def random_list(elements):
    random.shuffle(elements)
    return elements

print('섞인 리스트: ', elements)
print('섞인 리스트: ', random_list(elements))
print('섞인 리스트: ', random_list(numbers))

# 미션5. 랜덤으로 문자열 생성 (영문 대문자 6자리)
import string

def random_string():
    letters = string.ascii_uppercase
    random_letters = str()
    for i in range(6):
        random_letters += random.choice(letters)
    return random_letters

print("랜덤한 문자열은: ", random_string())

# 미션6. 랜덤 초이스에서 가중치를 고려한 랜덤

random_number = random.choices(range(1, 5), weights = [0.1, 0.2, 0.3, 0.4])

print(random_number)

# 미션7. 랜덤 비밀번호 생성 (대소문자, 숫자포함 8자리)
def password1(): 
    ele_pwd = list(string.ascii_letters + string.digits)
    password = str()
    for i in range(8):
        password += random.choice(ele_pwd)
    return password

print("생성된 랜덤 비밀번호: ", password1())

# 미련8. 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개 이상 포함하는 8자리를 만들려면?)
def password2(): 
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)

    ele_pwd = list(string.ascii_letters + string.digits)
    password = [upper, lower, digit]
    for i in range(5):
        password.append(random.choice(ele_pwd))
        random.shuffle(password)
    return ''.join(password)

print("생성된 랜덤 비밀번호: ", password2())