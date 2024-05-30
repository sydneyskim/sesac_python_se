# 점수 이름 입력해서 제일 높은 스코어인사람 보여주기 

# 메뉴 선택
# 입력받기 -> 리스트에 추기
# 리스트에서 1등 구하기..

def ShowMenu():
    print("1. 스코어 입력")
    print("2. 스코어 확인")
    print("3. 종료")
    
def input_score(scores):
    name = input("이름을 입력해주세요: ")
    while True:
        try:
            score = int(input("스코어를 입력하세요: "))
            break
        except ValueError:
            print("유효한 숫자를 입력하세요.")

    scores.append((name, score))
    print("입력된 점수: ")
    for i, (n, s) in enumerate(scores):
        print(f"{i + 1}. 이름: {n}, 스코어: {s}")

    print("뒤로가려면 숫자 2를 누르세요.")
    while True:
        choice = input()
        if choice == '2':
            break

def highScore(scores):
    if scores:
        highest = max(scores, key=lambda x: x[1])
        print(f"최고점: 이름: {highest[0]}, 스코어: {highest[1]}")
    else:
        print("아직 입력된 스코어가 없습니다.")
    
    print("뒤로가려면 숫자 2를 누르세요.")
    while True:
        choice = input()
        if choice == '2':
            break

def main():
    scores = []
    while True:
        ShowMenu()
        choice = input("메뉴를 선택하세요: ")
        if choice == '1':
            input_score(scores)
        elif choice == '2':
            highScore(scores)
        elif choice == '3':
            print('프로그램을 종료합니다.')
            break
        else:
            print("유효한 메뉴를 선택해주세요.")

main()