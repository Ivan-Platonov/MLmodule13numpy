print('Задача 4. Недоделка 2')

# Вы всё так же работаете в конторе по разработке игр и смотрите различные программы прошлого горе-программиста. В одной из игр для детей, связанной с мультяшной работой с числами, вам нужно было написать код согласно следующим условиям: программа получает на вход два числа; в первом числе должно быть не менее трёх цифр, во втором — не менее четырёх, иначе программа выдаёт ошибку. Если всё нормально, то в каждом числе первая и последняя цифры меняются местами, а затем выводится их сумма.

# И тут вы натыкаетесь на программу, которая была написана предыдущим программистом и которая как раз решает такую задачу. Однако старший программист попросил вас немного переписать этот код, чтобы он не выглядел так ужасно. Да и вам самим становится, мягко говоря, не по себе от него.

# Постарайтесь разделить логику кода на три отдельные логические части (функции):
# count_numbers — получает число и возвращает количество цифр в числе;
# change_number — получает число, меняет в нём местами первую и последнюю цифры и возвращает изменённое число;
# main — функция ничего не получает на вход, внутри она запрашивает нужные данные от пользователя, выполняет дополнительные проверки и вызывает функции 1 и 2 для выполнения задачи (проверки и изменения двух чисел).


# Разбейте приведённую ниже программу на функции. Повторений кода должно быть как можно меньше. Также сделайте, чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.
def error_message():
  print('Необходимо ввести положительное число, не равное нулю!!!')


def input_digits(finishText):
  num = ''
  while num == '':
    try:
      num = int(input(f'Введите {finishText}'))
      if num <= 0:
        error_message()
        num = ''
    except ValueError:
      error_message()
  return num


def count_numbers(digit):
  count = 0
  while digit > 0:
    digit //= 10
    count += 1
  return count


def change_number(digit):
  count = count_numbers(digit)
  last_digit = digit % 10
  first_digit = digit // 10**(count - 1)
  between_digits = digit % 10**(count - 1) // 10
  cange_digit = last_digit * 10**(count -
                                  1) + between_digits * 10 + first_digit
  return cange_digit

#Good function
#def change_number(digit):
#  digitList = []
#  for number in str(digit):
#    digitList.append(number)
#  digitList[0], digitList[-1] = digitList[-1], digitList[0]
#  return int(''.join(digitList))


def main():
  firstDigit = input_digits('первое число: ')
  secondDigit = input_digits('второе число: ')
  if count_numbers(firstDigit) < 3:
    print('В первом числе меньше трёх цифр.')
  elif count_numbers(secondDigit) < 4:
    print('Во втором числе меньше четырёх цифр.')
  else:
    changeFirstNumber = change_number(firstDigit)
    changeSecondNumber = change_number(secondDigit)
    print('\nИзменённое первое число:', changeFirstNumber)
    print('Изменённое второе число:', changeSecondNumber)
    print('\nСумма чисел:', changeFirstNumber + changeSecondNumber)


main()
