# 레거시한 코딩 스타일
def remove_duplicate(numbers):
    unique_list = []
    
    for n in numbers:
        duplicate_check = False

        for u in unique_list:

            print(f'입력값:{n}, 유닉목록:{u}')

            if n == u:
                print(f'중복: {n} == {u}')
                duplicate_check = True
                break
        if not duplicate_check:
            print(f'중복 아닌 것:{n}')
            unique_list.append(n)

    return unique_list

numbers = [1, 2, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9]
unique_numbers = remove_duplicate(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)

# 조금 더 파이썬스러운 스타일

def remove_duplicate2(numbers):
    unique_list = []

    for n in numbers:
        if n in unique_list:
            pass
        else:
            unique_list.append(n)
    return unique_list

numbers = [1, 2, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9]
unique_numbers = remove_duplicate2(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)



def remove_duplicate3(numbers):
    unique_list = []

    for n in numbers:
        if n not in unique_list:
            unique_list.append(n)
    return unique_list

numbers = [1, 2, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9]
unique_numbers = remove_duplicate3(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)

# 모던 파이썬 코드 set

def remove_duplicate4(numbers):
    return list(set(numbers))

numbers = [1, 2, 4, 4, 4, 5, 6, 6, 7, 7, 7, 7, 8, 9]
unique_numbers = remove_duplicate4(numbers)

print("원본 리스트: ", numbers)
print("유닉 리스트: ", unique_numbers)