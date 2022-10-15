# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

# in
# 424

# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

def input_numbers(inputText):
    okey = False
    while not okey:
        try:
            number = int(input(f"{inputText}"))
            okey = True
            if number <= 20:
                okey = False
                print("Число не может быть меньше 20")
        except ValueError:
            print("Это не число!")
    return number


def creates_list(number):
    list_nums = []
    for i in range(20, number+1):
        if i % 20 == 0 or i % 21 == 0:
            list_nums.append(i)
    return list_nums



num = input_numbers("Введите число: ")
used_list = creates_list(num)
print(used_list)

list_nums = [i for i in range(20, num +1) if i % 20 == 0 or i % 21 == 0]
print(list_nums)
