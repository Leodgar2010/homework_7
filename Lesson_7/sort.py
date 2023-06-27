# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не
# подошли для сортировки.
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
#
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
#
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
import os
import shutil
from random import randint

DIC = {'films': ['avi', 'mkv'], 'pictures': ['jpg', 'gif'], 'documents': ['txt', 'doc']}


def my_func(DIC):
    for i in DIC.keys():
        if i not in os.listdir():
            os.mkdir(f"{i}")
    for i in os.listdir():
        if os.path.isfile(i):
            for j in DIC.keys():
                if i.split(".")[1] in DIC.get(j):
                    if i not in os.listdir(j):
                        shutil.copy(i, j)
                        os.remove(i)
                    else:
                        b = i
                        while True:
                            a = (f'{b.split(".")[0]}_{randint(1, 100)}.{b.split(".")[1]}')
                            os.renames(b, a)
                            if a not in os.listdir(j):
                                shutil.copy(a, j)
                                os.remove(a)
                                break
                            else:
                                b = a


my_func(DIC)
