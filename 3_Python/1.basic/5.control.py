# 제어문
# 반복문, 조건문 for, while ~할때까지

count = 0

while (count <= 10): # 이 조건이 True인 동안
   count = count + 2 
   print(count)

print('for')
for i in range(10): # 특정 목록 내에서의 반복 range(10) = [0,1,2,3,4,5,6,7,8,9]
   print(i)

users = ['park', 'kim', 'lee', 'son']
for name in users:
   print(name)

for num in [-5, 7, 133, "sesac", "keke"]:
    print(num)

for i in range(3,7): #range(3,7) = [3,4,5,6]
   print(i)

for i in range(1,10,2): # range(1,10,2) = [1,3,5,7,9] (건너뛰기)
   print(i)