# 📍 Программа, которая задаёт список из n чисел последовательности (1 + 1/n)^n 
# и выводит на экран их сумму.

def input_number(input_message):
    while True:
        input_str = input(input_message)
        if is_int(input_str) and int(input_str) > 0:
            return int(input_str)
        else:
            print("❌ Введено не число!")

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def calculate(n):
    if n != 0:
        return (1 + 1 / n) ** n
    else:
        return False

def get_dictionary_sum(dict_num):
    sum = 0
    for i in range(1, len(dict_num)):
        sum += dict_num[i]
    return sum

number_N = input_number("✏️  Введите число: ")
dictionary_numbers = {}
for i in range(1, number_N + 1):
    dictionary_numbers[i] = round(calculate(i), 2)
print(f'Для N = {number_N} {str(dictionary_numbers)} сумма равна {str(get_dictionary_sum(dictionary_numbers))}')