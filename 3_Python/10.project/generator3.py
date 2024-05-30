import random
import uuid
import csv
from itertools import chain

class IdGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class NameGenerator:
    names = []

    def __init__(self):
        with open('names.txt', 'r', encoding='utf-8') as file:
            # names = file.read().splitlines()
            csvreader = csv.reader(file)
            csv_list_name = [n for n in csvreader]
            names_list = list(chain(*csv_list_name))
            self.names = [n.strip() for n in names_list]
            
    def generate_name(self):
        return random.choice(self.names)

class BirthdateGenerator:
    year_start = 1980
    year_end = 2005

    def generate_birthdate(self):
        year= random.randint(self.year_start, self.year_end)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f"{year}-{month:02d}-{day:02d}"

class GenderGenerator:   
    def generate_gender(self):
        return random.choice(['Male', 'Female'])

class AddressGenerator:
    cities = []

    def __init__(self):
        with open('cities.txt', 'r') as file:
            reader = csv.reader(file)
            data = [line for line in reader]
            data = list(chain.from_iterable(data))
            self.cities =[d.strip() for d in data]

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"

class DataGenerator:
    numbers = 1
    data = []

    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.addr_gen = AddressGenerator()

    def generate_users(self):
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.addr_gen.generate_address()

            a_user = (id, name, birthdate, gender, address)
            self.data.append(a_user)


# 메인함수
if __name__ == "__main__":

    users1 = DataGenerator(100)
    users1.generate_users()

    # print(data)

    for d in users1.data:
        print(d)
