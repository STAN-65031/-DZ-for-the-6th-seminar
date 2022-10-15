# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"

# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


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


def input_names(amount):
    list_names = []
    list_word = []
    while amount > 0:
        name = input("Введите имя: ")
        list_names.append(name)
        amount = amount - 1
    list_names.sort()
    return list_names


def forms_dictionary(names):
    dictionary = {}
    for name in names:
        if name[0] not in dictionary:
            dictionary[name[0]] = [name]
        if name not in dictionary[name[0]]:
            dictionary[name[0]] += [name]
    return dictionary


num = input_numbers("Задайте количество имён: ")
res = input_names(num)
print(res)

print(forms_dictionary(res))
