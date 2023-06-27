# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice

VOWEL = 'аеёиоуыэюя'
CONSONANCE = "бвгджзклмнпрстфхцчшщ"
MIN_LENGHT = 4
MAX_LENGHT = 7


def write_names(filename, row_count):
    with open(filename, 'w', encoding='utf-8') as f:
        for _ in range(row_count):
            a = ""
            for i in range(randint(MIN_LENGHT, MAX_LENGHT)):
                if i in (1, 3):
                    a += choice(CONSONANCE)
                else:
                    a += choice(VOWEL)

            f.write(f"{a.capitalize()}\n")


write_names('names.txt', 5)
