# 📍 Программа, которая задаёт список из N элементов, заполненных числами из промежутка [-N, N] 
# и находит произведение элементов на указанных позициях. 
# (позиции хранятся в файле file.txt в одной строке одно число.)

number_n = int(input("✏️  Введите число: "))
result = 1
lst = list(range(-number_n, number_n+1))
print(lst)
data = open("4_file.txt", "r")
for el in data:
    result *= lst[int(el) - 1]
print(result)