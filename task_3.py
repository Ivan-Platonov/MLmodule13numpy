print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

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

def reverse_number(n):
  reverse_n = 0
  while n > 0:
    digit = n % 10
    reverse_n = reverse_n * 10 + digit
    n //= 10
  return reverse_n

firstDigit = input_digits('первое число: ')
secondDigit = input_digits('второе число: ')


reverseFirstDigit = reverse_number(firstDigit)
reverseSecondDigit = reverse_number(secondDigit)
print('\nПервое число наоборот:', reverseFirstDigit)
print('Второе число наоборот:', reverseSecondDigit)

summ = reverseFirstDigit + reverseSecondDigit

print('\nСумма:', summ)
print('Сумма наоборот:', reverse_number(summ))
