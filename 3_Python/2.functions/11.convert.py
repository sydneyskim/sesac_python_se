# 1. 문자를 입력받아, 대소문자를 변경하시오.
# 문자내의 대문자 -> 소문자, 소문자 -> 대문자 변경
# 예) Hello -> hELLo

def convert_case(text):
    converted_text = ""
    for char in text:
        if char.islower():
            converted_text += char.upper()
        elif char.isupper():
            converted_text += char.lower()
        else:
            converted_text += char
    return converted_text

print(convert_case("Hello"))
# print(convert_case("WelCOME"))
# print(convert_case("GoodBye"))
# print(convert_case("Good Bye"))
# print(convert_case("This is long messege. haha1234"))

def convert_case2(text):
    return''.join([char.upper() if char.islower() else char.lower() for char in text])
    
                    # for char in text # text를 읽어서 char 추출한다.
                    # 맨 앞에 char는 for문의 결과 char가 담기는 곳
                    # char.upper() -> if char.islower()
                    # char.lower()
                    # if 구문의 ... char.upper()를 하기 위한 조건

print(convert_case2('HellO'))