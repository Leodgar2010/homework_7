# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не
# подошли для сортировки.

import os
import pathlib
import shutil

DIC ={'films':['avi','mkv'], 'pictures':['jpg','gif'], 'documents':['txt','doc']}
print(os.listdir())
def my_func (DIC):
    a=os.listdir()
    for i in a:
        print(i.split('.')[1])
        if os.path.isfile(i) and i[1] in DIC.get('pictures'):
            shutil.copy(i,'pictures')

my_func(DIC)





