import pathlib
import os


# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
#
# * При переименовании в конце имени добавляется порядковый номер.
#
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
def renaming(output_name, source_ext, output_ext):
    count = 1
    for i in os.listdir():
        if os.path.isfile(i) and i.split('.')[1] == source_ext:
            a = f"{i.split('.')[0]}_{output_name}_{count}.{output_ext}"
            os.rename(i, a)
            count += 1


renaming('test', 'tif', 'jpg')
