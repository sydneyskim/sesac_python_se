def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return '0으로 나눌 수 없습니다.'
    except TypeError:
        return '입력값이 숫자가 아닌 값이 있습니다.'
    # except:
    #     print('알 수 없는 이유로 나눌 수 없습니다.')
    #     return "NaN"
    else:
        print("오류가 안나고 계산을 잘 완료하였습니다.")
    finally:
        print("여기는 오류가 났건 성공했건 무조건 호출됩니다.")
    return result

print(div(5, 3))
print(div(10, 2))
print(div(15, 5))
print(div(5, 0))
print(div(5, "a"))

# 문자숫자를 받아서 -> 숫자로 변환하기
# "20" -> 20
def convert_to_interger(num_str):
    try:
        result = int(num_str)
    except ValueError:
        print('유효한 숫자를 입력하세요')
        return None
    
    return result
    
print(convert_to_interger("20"))
print(convert_to_interger("100"))