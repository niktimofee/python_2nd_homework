# 📍 Программа, которая принимает на вход вещественное число и показывает сумму его цифр.

def input_number (input_message):
    while True: 
        input_str = input(input_message)
        if is_float(input_str):
            return float(input_str)
        else:
            print("❌ Введено не число!")
            
def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def count_sum_in_str(number):
    str_to_count = str(number)
    sum = 0
    for i in range(0,len(str_to_count)):
        if is_int(str_to_count[i]):
            sum += int(str_to_count[i])
    return sum

def count_sum(number):
    sum = 0
    div = 0
    if number < 0:
        number = -number
    print(f'number = {number}, sum = {sum}, div = {div}')
    while True:
        if number >= 1:
            number = number/10
        if number < 1:
            number = number*10
        print(f'number = {number}, sum = {sum}, div = {div}')
        if int(number) == 0:
            break
    return sum

number_N = input_number ("✏️  Введите число: ")
output_str = f'Сумма цифр в числе "{str(number_N)}" равна {str(count_sum_in_str(number_N))}'
print(output_str)