# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление. Функцию hex используйте
# для проверки своего результата.

num = int(input('Введите целое число: '))
number = num
hex_num = hex(num)
hex_list = '0123456789abcdef'
our_hex_num = ""

while number > 0:
    result = number % 16
    new_num = hex_list[result]
    our_hex_num = new_num + our_hex_num
    number = number // 16
our_result = '0x' + our_hex_num

if our_result == hex_num:
    print(
        f'Из числа {num} вы получите шестнадцатеричное строковое представление в виде {our_result}')
    print(f'Функцию hex = {hex_num}')
else:
    print('Что-то пошло не так!')