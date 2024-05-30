import random

# 날짜 + 시간 생성기 클래스
class DateTimeGenerator:
    year_start = 2020
    year_end = 2024
    
    # 날짜 시간 랜덤생성
    def generate_datetime(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        hour = random.randint(1, 24)
        minute = random.randint(1, 60)
        second = random. randint(1, 60)
        datetime = f"{year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
        
        return datetime