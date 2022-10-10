# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
 
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
 
import random
 
def equationite_file(st):
    with open('mathEquation.txt', 'w') as data:
        data.write(st)
 
def rnd():
    return random.randint(-100,101)
 
def create_mn(k):
    lst = [rnd() for i in range(k+1)]
    return lst
    
 
def create_equation(sp):
    lst= sp[::-1]
    equation = ''
    if len(lst) < 1:
        equation = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                equation += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    equation += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                equation += f'{lst[i]}x'
                if lst[i+1] != 0:
                    equation += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                equation += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                equation += ' = 0'
    return equation
 
k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
equationite_file(create_equation(koef))