# 계산기 코드 작성하기
# 1. 연산자 및 두개의 숫자를 입력받아 그 결과를 출력하시오.
# 2. 무한반복하기
def calc(opr, num1, num2):
     #    if opr not in ["*", "/", "+", "-"]:
     #         raise ValueError("올바른 연산자를 입력하세요")
     #    if not isinstance(num1, int) or not isinstance(num2, int):
     #         raise ValueError("숫자를 입력해주세요.")
    
        if opr == "*":
             result = num1 * num2
        elif opr == "/":
             result = num1 / num2
        elif opr == "+":
             result = num1 + num2
        elif opr == "-":
             result = num1 - num2

        return result

while True:
     while True:
          try:
               opr = input("연산자를 입력하세요: ")
               if opr not in ["*", "/", "+", "-"]:
                    raise ValueError("올바른 연산자를 입력하세요")
               break
          except ValueError as e :
               print("입력값에 오류가 있습니다.: " + str(e))
     while True:
          try:
               num1 = int(input("첫번째 숫자를 입력하세요: "))
               if not isinstance(num1, int):
                    raise ValueError("숫자를 입력해주세요.")
               break
          except ValueError as e :
               print("입력값에 오류가 있습니다.: " + str(e))
          except TypeError as t :
               print("입력값에 오류가 있습니다.: " + str(t))
     while True:
          try:
               num2 = int(input("두번째 숫자를 입력하세요: "))*1
               if not isinstance(num2, int):
                    raise ValueError("숫자를 입력해주세요.")
               elif num2 == 0:
                  raise ValueError("0으로 나눌 수 없습니다.")
          except ValueError as e :
               print("입력값에 오류가 있습니다.: " + str(e))
          except TypeError as e :
               print("입력값에 오류가 있습니다.: " + str(t))
          else:
               print(f"결과: {calc(opr, num1, num2)}")
               break


# 연산자, 숫자2개 입력받기
# 연산자가 +-*% 가 아니면 예외발생
# 숫자가 숫자가 아니면 예외발생
# 연산하기 
# 결과출력
# 계속반복