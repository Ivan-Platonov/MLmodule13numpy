print('Задача 6. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
#
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
#
# Известно, что глубина точно больше нуля и меньше четырёх метров.
#
# Обеспечьте контроль ввода.
#
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
#
# Приблизительная глубина безопасной кладки: 0.732421875 м
import numpy as np
from numpy import roots

def error_message():
  print('Необходимо ввести положительное число между 0 и 1.')


def input_digits(Text):
  num = ''
  while num == '':
    try:
      num = float(input(Text))
      if num <= 0 or num > 1:
        error_message()
        num = ''
    except ValueError:
      error_message()
  return num

def solve_cubic_equation(a, b, c, d):
  coeffs = [a, b, c, d]
  roots_value = roots(coeffs)
  return roots_value


def main(danger):
  count = 0
  break_out_flag = False
  while count <= danger:
    depths = solve_cubic_equation(1, -3, -12, 10 - count)
    count += 0.001
    for item in range(len(depths)):
      if depths[item] > 0 and depths[item] < 4:
        print(f'Приблизительная глубина безопасной кладки: {round(depths[item], 9)} м')
        break_out_flag = True
        break
    if break_out_flag:
      break

danger = input_digits('Введите максимально допустимый уровень опасности: ')
main(danger)

