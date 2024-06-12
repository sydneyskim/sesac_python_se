list1 = [1,2,3]
list2 = ['a','b','c']

zipped = zip(list1, list2)
print(list(zipped))
# [(1, 'a'), (2, 'b'), (3, 'c')]

list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))
# [(1, 'a', True), (2, 'b', False), (3, 'c', True)]

# zip으로 묶을 때는 가장 짧은 데이터를 기준으로 묶인다. 

# v1, v2, v3 = list(zip(*zipped)) # 묶인 데이터 다시 풀기 unpacking
# print(v1)
# print(v2)
# print(v3)

keys = ['name', 'age', 'phone']
values = ['Alice', 25, '123-456-7890']

my_dict = dict(zip(keys, values))
print(my_dict)
# {'name': 'Alice', 'age': 25, 'phone': '123-456-7890'}

values_list = [
    ['Alice', 25, '123-456-7890'],
    ['Bob', 21, '234-567-8901'],
    ['Charlie', 30, '345-678-9012'],
]

dictlists = [dict(zip(keys, values)) for values in values_list]
print(dictlists)
#[{'name': 'Alice', 'age': 25, 'phone': '123-456-7890'}, {'name': 'Bob', 'age': 21, 'phone': '234-567-8901'}, {'name': 'Charlie', 'age': 30, 'phone': '345-678-9012'}]

