contents = ""

try:
    with open("file.txt", "w") as file:
        # contents = file.read()
        file.write('Hello')

except:
    print('알 수 없는 에러입니다.')

# except FileNotFoundError:
#     print("파일이 없습니다.")

# except PermissionError:
#     print("해당 파일에는 쓰기 권한이 없습니다.")

# except IOError:
#     print("해당 파일에는 읽기/쓰기 권한이 없습니다.")

print("파일내용: ", contents)