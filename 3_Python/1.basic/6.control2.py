x = 10

if x < 10: # 이 조건이 True 일 때....
    print('x가 10보다 작습니다.')
else: # 위 조건이 false 일 때....
    print('x가 10보다 같거나 큽니다.')

# ------------------------------------

score = 95

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score, grade)

print("Score: {}, Grade: {}".format(score, grade))

print("Score: {0}, Grade: {1}".format(score, grade))
print("Score: {1}, Grade: {0}".format(score, grade))

print('점수는 {score} 이고, 성적은 {grade} 입니다.') #문자열
print(f'점수는 {score} 이고, 성적은 {grade} 입니다.') #포멧팅


math = 90
eng= 90

if math >= 90 and eng >= 90: # and, or
    print('졸업조건 충족')
else:
    print('졸업조건 미흡')