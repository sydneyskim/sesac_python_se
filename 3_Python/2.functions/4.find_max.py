numbers = [-3, -7, -2, -9, -1, -4, -5, -6, -8]

def find_max(numbers):
    max_num = numbers[0] # 리스트의 첫번째 숫자를 최대값으로 초기설정

    for i in numbers[1:]: #numbers[1:] 두번째요소부터 마지막요소까지
        if i > max_num:
            max_num = i
    print(f'가장 큰 숫자는 {max_num} 입니다.')

find_max(numbers) #함수 호출