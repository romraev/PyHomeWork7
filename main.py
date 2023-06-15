# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках 
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  
# Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, 
# если с ритмом все не в порядке

# song = list(input('Enter song: ').split())

# def countVocals(song, i):
#     count = len(list(filter(lambda x: x == 'а' or x == 'у' or x == 'е' or x == 'ы' or x == 'о' or x == 'э' or x == 'я' or x == 'и' or x == 'ю', list(song[i]))))
#     return count

# def isRhythm(op, song):
#     flag = True
#     for i in range(len(song)):
#         if op(song, i) != op(song, 0):
#             flag = False
#     return flag

# if isRhythm(countVocals, song) == True:
#     print('Парам пам-пам')
# else: print('Пам парам')


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве 
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк 
# и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, rows, cols):
    tabl = [operation(r+1, c+1) for r in range(rows) for c in range(cols)]
    
    for i in range(rows*cols): 
        if (i+1)%cols != 0:
            print(tabl[i], end='\t') 
        else: 
            print(tabl[i], end='\t') 
            print()

row = int(input('enter rows number: '))
col = int(input('enter cols number: '))

print_operation_table(lambda x, y: x*y, row, col)