# print(1/0) # zero division error (горит красным)
# try: # пробуем заранить сломанный код
#     letter = "a"
#     print(1/int(letter)) # valueError (букву нельзя превратить в число)
# except: # ловим ошибку
#     print("Ошибочка")
#
#
# try: # Пробуем разделить на 0
#     print(1/0)
# except: # указываем, что делать после этой ошибки
#     print("На ноль делить нельзя")


# import sys
#
# randomList = ["a", 0, 2]
# for element in randomList:
#     try:
#         print("Данный элемент: ", element)
#         operation = 1/int(element)
#     except:
#         print("Упс!", sys.exc_info()[0])
#         print()





# Пример-1 ловля конкретных исключений
# try:
#     print(n) # переменной n несуществует, поэтому ошибка
# except (ZeroDivisionError): # несмотря на то, что мы ловим какую-то ошибку
#     print("Ошибка")

# Пример-2 несколько исключений
# try:
#     print(n) # переменной n несуществует, поэтому ошибка
# except (ZeroDivisionError, NameError):
#     print("Ошибка")


# Пример-3
# try:
#     num = int(input("введите число: "))
#     print(num/0)
#     print(x) # NameError
# except ValueError:
#     print("Принимает только числа")
# except (TypeError, ZeroDivisionError):
#     print("Делит только на 0")
# except:
#     print("Непредвиденная операция")


# Пример-4 пробуем вызвать ошибку и сразу же поймать ее
# try:
#     num = int(input("Введите позитивное число: "))
#     if num <=0:
#         raise ValueError("Это негативное число!")
# except ValueError as ve:
#     print(ve)



# Пример-5 try-except-else
# try:
#     print("Привет")
# except:
#     print("Что-то не так")
# else:
#     print("Всё по плану")



# Пример использования всего вместе
# try:
#     print(2)
# except:
#     print("Что-то не так")
# else:
#     print("Всё по плану")
# finally:
#     print("Блок try-except закончен")




# Пример ошибки с индексом
# lst = [5, 10, 20]
# try:
#     print(lst[5])
# except IndexError as error:
#     print("Exception is: {}".format(type(error).__name__))


# my_list1 = []
# for element in range(10):
#     try:
#         num = int(input("введите число: "))
#         if num % 2 == 0:
#             my_list1.append(num)
#         else:
#             raise BaseException("Так делать нельзя!")
#     except BaseException as error:
#         print("Exception is: {}".format(type(error).__name__))
# print(my_list1)






# функция, которая принимает 3 аргумента - числа
# выводит самое большое число

# def maximum(num1, num2, num3):
#     if num1 > num2 and num1 > num3:
#         print(num1, "Самое большое число!")
#     elif num2 > num1 and num2 > num3:
#         print(num2, "Самое большое число!")
#     elif num3 > num1 and num3 > num2:
#         print(num3, "Самое большое число!")
#     elif num1 == num2 and num1 == num3:
#         print("Числа равны.")
#     elif num1 == num2 or num1 == num3 or num2 == num3:
#         print("Два числа равны.")

# Проверка если в тексте, все является числом
# my_list = []
# count = 0
# while count < 3:
#     num = input("введите число: ")
#     x = num.isdigit()
#     if x == True:
#         my_list.append(num)
#         count = count + 1
# print(my_list)
# maximum(int(my_list[0]), int(my_list[1]), int(my_list[2]))