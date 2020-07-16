'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def div_n():
    try:
        f_num = int(input("Put in the first number: "))
        s_num = int(input("Put in the second number: "))
    except ValueError: return print("You've entered the sting value, pls enter the number")
    try:
        res = f_num / s_num
    except ZeroDivisionError: return print("Error, division by zero")
    res = round(f_num / s_num, 1)
    return res

print(div_n())

'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. 
Реализовать вывод данных о пользователе одной строкой.
'''

name = input("Your name: ")
surname = input("Your second name: ")
d_brth = input("Put in here you birth date: ")
city = input("Type in you city of residence: ")
e_mail = input("Enter your e-mail address: ")
phone = input("Enter your phone number: ")

def user_info(a, b, c, d, e, f):
    print(f"Name - {a}; Surname - {b}; Date of birth - {c}; City of residence - {d}; E-mail address - {e}; Phone number - {f} ")

user_info(a = name, b = surname, c = d_brth, d = city, e = e_mail, f = phone)


'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''

def maxof_3(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(a, b, c))
    return sum(my_list)
print(maxof_3(10, 20, 15))


'''
4. Программа принимает действительное положительное число x и целое отрицательное число y. 
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). 
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''

x = int(input("Enter the number: "))
y = int(input("Put in the power number: "))

# first version of powering the number:

def my_func_pow (x, y):
    res = x ** abs(y)
    return res
print(my_func_pow(x, y))

#seconf varsion withou special operator '**':

def my_func(x, y):
    i = 1
    while abs(y) > 0:
        i *= x
        y -= 1
    return i

print(my_func(x, y))

'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, 
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму 
этих чисел к полученной ранее сумме и после этого завершить программу.
'''

def fill_in():
    array_sum = 0
    while True:
        arr = input("Enter your numbers thru the space sign here to get the array sum, for exit put in 'Q': ").split()
        for i in arr:
            try:
                if i == 'Q':
                    print(f"Result: {array_sum}")
                    return print("You've entered 'Q', Range calc is finished.")
                else:
                    array_sum += int(i)
            except ValueError:
                print()
        print(f"Result: {array_sum}")

print(fill_in())


'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит
из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
Необходимо использовать написанную ранее функцию int_func().
'''

def int_func_single(text):
    lst = []
    lst.append(text[0:1].upper() + text[1:])
    return lst
print(int_func_single(input("Enter your word with lower case letters: ")))

def int_func(text):
    lst = []
    for i in range(len(text)):
        lst.append(text[i][0:1].title() + text[i][1:])
    return ' '.join(lst)

print(int_func(input("Enter your text or string: ").split()))