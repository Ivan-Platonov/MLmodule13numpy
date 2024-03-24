print('Задача 1. Урок информатики 2')

# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
#
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
#
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
#
# Пример 1:
#
# Введите число: 92345
#
# Формат плавающей точки: x = 9.2345 * 10 ** 4
#
# Пример 2:
#
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3

from decimal import Decimal


def big_digit(digit):
  step = 0
  while digit > 10:
    digit = Decimal(str(digit)) / 10
    step += 1
  print('Формат плавающей точки: x =', digit, '* 10 **', step)


def small_digit(digit):
  step = 0
  while digit < 1:
    digit = Decimal(str(digit)) * 10
    step += 1
  print(f'Формат плавающей точки: x = {float(digit)} * 10 ** -{step}')


def input_digit():
  digit = ''
  while digit == '':
    try:
      digit = float(input('Введите число: '))
      if digit <= 0:
        print('Ошибка ввода. Введите положительное число.')
        digit = ''
    except ValueError:
      print('Необходимо ввести число!!!')

  if digit >= 1:
    big_digit(digit)
  else:
    small_digit(digit)


input_digit()