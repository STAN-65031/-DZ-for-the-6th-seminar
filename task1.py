# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.
# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import sample

def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
            if number == 0:
                okey = False
                print("Список не может быть равен 0")
        except ValueError:
            print("Это не число!")
    return number

def creates_list(number):
    list_nums = sample(range(1, number * 5), number)
    return list_nums

def finds_numbers(li):
    res = []
    for i in range(len(li)):
        if li[i-1] < li[i]:
            res.append(li[i])
    return res

num = input_numbers("Задайте длинну списка: ")
used_list = creates_list(num)
print(used_list)
result = finds_numbers(used_list)
print(result)

res = [used_list[i] for i in range(len(used_list)) if used_list[i-1] < used_list[i]]
print(res)

