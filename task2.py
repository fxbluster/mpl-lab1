from functools import reduce

people = [
    {"name": "Elvin", "birth_year": 2004},
    {"name": "Ali", "birth_year": 2003},
    {"name": "Murad", "birth_year": 2000},
    {"name": "Leyla", "birth_year": 2005},
    {"name": "Aysel", "birth_year": 1996},
    {"name": "Anar", "birth_year": 2002}
]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

leap_people = list(filter(lambda person: is_leap(person["birth_year"]), people))
print("Uzun ilde dogulanlar:", leap_people)

ages = list(map(lambda person: 2026 - person["birth_year"], people))
print("Yaslar:", ages)

total_age = reduce(lambda a, b: a + b, ages)
average_age = total_age / len(ages)

print("Yaslarin cemi:", total_age)
print("Orta yas:", average_age)
