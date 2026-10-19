people = [
    {"name": "Elvin", "birth_year": 2004},
    {"name": "Ali", "birth_year": 2003},
    {"name": "Murad", "birth_year": 2000},
    {"name": "Leyla", "birth_year": 2005},
    {"name": "Aysel", "birth_year": 1996},
    {"name": "Anar", "birth_year": 2002}
]

leap_count = 0

for person in people:
    year = person["birth_year"]
    age = 2026 - year

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        is_leap = True
        leap_count += 1
    else:
        is_leap = False

    print(person["name"], "- Yas:", age, "- Uzun il:", is_leap)

print("Uzun ilde dogulanlarin sayi:", leap_count)
