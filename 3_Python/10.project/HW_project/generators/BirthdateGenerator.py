import random

# 생년월일 생성기 클래스
class BirthdateGenerator:
    year_start = 1924
    year_end = 2014
    
    # 생년월일 랜덤생성 , 나이 계산
    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        # 올해년도에서 생년 빼기.. + 1 햔국식 나이.. 
        age = 2024 - year + 1
        birthdate = f"{year}-{month:02d}-{day:02d}"
        
        return birthdate, age