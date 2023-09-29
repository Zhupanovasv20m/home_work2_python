# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и произведение*
# дробей. Для проверки своего кода используйте модуль fractions.

import fractions

first_str = input('Введите первую дробь типа a/b: ').split('/')
second_str = input('Введите вторую дробь типа a/b: ').split('/')
numerator_one = int(first_str[0])
denominator_one = int(first_str[1])
numerator_two = int(second_str[0])
denominator_two = int(second_str[1])

sum_of_num = (numerator_one/denominator_one) + (numerator_two/denominator_two)
print(sum_of_num)

res = (numerator_one/denominator_one) * (numerator_two/denominator_two)
print(res)



f1 = fractions.Fraction(numerator_one, denominator_one)
f2 = fractions.Fraction(numerator_two, denominator_two)
print(f1 + f2)
print(f1 * f2)