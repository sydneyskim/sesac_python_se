my_dict = {'name':'Alice', 'age': 25, 'phone': '123-456-7890'}
# print(my_dict)

# built-in 함수 = 내장함수 = 파이썬에 기본 탑재된 함수
items = my_dict.items()
print(items)
items_list = list(items) # type casting  = 형(type) 변환시켜주는 과정..
print(items_list[1])

for item in items_list:
    print(item)
    
for key, value in items_list:
    print(f'키: {key}, 값: {value}') # 최대한 meaningful 하게 하는 것이 좋다.
    
print('-'*50)

for key, value in sorted(my_dict.items()):
    print(f'키: {key}, 값: {value}')
    
updated_dict = {'car': 'K5', 'city': 'Seoul'}

for key, value in updated_dict.items():
    my_dict[key] = value
    
print(f'원본: {my_dict}')
print(f'업데이트: {updated_dict}')

new_dict = my_dict | updated_dict # python 3.9 이상 ~
print(f'통합본: {new_dict}')

print('-'*50)

users = [
    {'name':'Alice', 'age': 25, 'phone': '123-456-7890'},
    {'name':'Bob', 'age': 19, 'phone': '234-567-8901'},
    {'name':'Charlie', 'age': 22, 'phone': '345-678-9012'},
]

filtered_users = []
for user in users:
    if user.get('age', 0) >= 20: # get,,,0 : age 가 있으면 가져오고, 없으면 디폴트값 0으로 처리
        filtered_users.append(user)
        
print(filtered_users)

filtered_users = [user for user in users if user.get('age', 0) >= 20]
print(filtered_users)

filtered_user_ages = [{key:value for key, value in u.items() if key == 'age' and value >= 20} for u in users]
print(filtered_user_ages)