# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


 
def createList (quantity):
    import random
    list = []
    for i in range (quantity):
        list.append(random.randint (1 , 5))
    # print(list)
    return list
 
list1 = createList (15)
# print (list1)
set_fromList1 = set(list1)
# print(set_fromList1)
list_fromSet = list(set_fromList1)
# print(list_fromSet)
 
result_list = []
for i in range (len(list_fromSet)):
    count = 0
    for k in range (len(list1)):
                if list_fromSet[i] == list1[k]:
                    count += 1
    if (count == 1):
        result_list.append(list_fromSet[i])
print (f'{list1} -> {result_list}')