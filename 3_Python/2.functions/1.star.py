# print('*')
# print('**')
# print('***')
# print('****')

row = int(input('출력을 원하는 높이를 입력하세요: '))
for i in range(1, row + 1):
    print('*' * i)

row = input('출력을 원하는 높이를 입력하세요: ')
num_rows = int(row)
for i in range(1, num_rows + 1):
    print(f'*' * i)

#    *
#   **
#  ***
# ****

row = int(input('출력을 원하는 높이를 입력하세요: '))
for i in range(1, row +1):
    print(' ' * (row - i) + '*' * i) # 공백도 출력해야함

row = int(input('출력을 원하는 높이를 입력하세요: '))
for i in range(1, row + 1):
    print(' ' * (row - i) + '*' * (2 * i - 1))

row = int(input('출력을 원하는 높이를 입력하세요: '))
for i in range(row-1, 2, -1):
    print(' ' * (row - i) + '*' * (2 * i - 1))