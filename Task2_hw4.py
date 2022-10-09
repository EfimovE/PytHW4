# Задайте натуральное число N. Напишите программу, которая составит список простых 
# множителей числа N.


def primeFactors (num):
    i = 2
    listFactors = []
    number = num
    while i <= num:
        if num % i == 0:
            listFactors.append(i)
            num //= i
            i = 2
        else:
            i += 1
    print(f"Cписок простых множителей числа {number} :  {listFactors} ")

primeFactors (int(input("Введите натуральное число N: ")))