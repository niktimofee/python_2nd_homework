# 📍 Программа, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

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

def mult(n):
    if n == 1:
        return n
    else:
        return n * mult(n - 1)

number_N = input_number("✏️  Введите число: ")
list_numbers = []
for i in range(1, number_N + 1):
    list_numbers.append(mult(i))
output_str = str(list_numbers)
print(f'Пусть N = {number_N}, тогда: {output_str}')