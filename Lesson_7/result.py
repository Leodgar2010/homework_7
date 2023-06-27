# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько
# в более длинном файле. При достижении конца более короткого файла,
# возвращайтесь в его начало.
import typing
def read_per_line (file_obj:typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()
    return line[:-1]
def my_func(numbers, names, result):
    with (
        open(numbers, 'r', encoding='utf-8') as nums,
        open(names, 'r', encoding='utf-8') as nam,
        open(result, 'w', encoding='utf-8') as res
    ):
        len_nam = sum(1 for _ in nam)
        print (len_nam)
        len_nums =sum (1 for _ in nums)
        print (len_nums)
        for i in range (max(len_nam,len_nums)):
          name=read_per_line(nam)
          print (name)
          number=read_per_line(nums)
          print (number)
          a,b = map (float, number.rstrip().split('|'))
          temp = a*b
          if temp<0:
                 res.write(f"{name.lower()} : {abs(temp)}\n")
          else:
                 res.write(f"{name.upper()} : {int(temp)}\n")

my_func('numbers.txt','names.txt','result.txt')