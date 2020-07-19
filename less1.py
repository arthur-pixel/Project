from sys import argv


'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. 
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для 
конкретных значений необходимо запускать скрипт с параметрами.
'''

script_name, hours, fee, rew = argv


def __salary__():
    slr = int(hours) * int(fee)
    percent = (slr / 100) * int(rew)
    global on_hand
    on_hand = slr + percent
    return on_hand


print(f"Sallary Count file name: {script_name}")
print(f"Working hours: {hours}")
print(f"Per hour rate in 'RUB': {fee}")
print(f"Reward %: {rew}")
print(f"Employee sallary before VAT 'RUB': {__salary__()}")

'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего 
элемента.
'''

initial_l = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_ = []

for i in range(len(initial_l) - 1):
    if initial_l[i] < initial_l[i + 1]:
        new_.append(initial_l[i + 1])

print(f"Original array: {initial_l}")
print(f"Derivated list: {new_}")


'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
'''

my_range = [print(el) for el in list(range(20, 241)) if el % 20 == 0 or el % 21 == 0]

'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, 
соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания 
обязательно использовать генератор.
'''


my_arr = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list = []
arr = [my_list.append(el) for el in my_arr if my_arr.count(el) <= 1]
print(my_list)


'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные 
числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
'''


from functools import reduce
lst = list(range(100, 1001))
res_l = []
ev_num = [res_l.append(el) for el in lst if el % 2 == 0]
print(res_l)
print("Multiplication result: ", reduce(lambda x, y: x * y, res_l))


'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
'''

from itertools import count

for el in count(20):
    if el > 30:
        break
    else:
        print(el)


from itertools import cycle, count
e_l = [25, 30, 35, 40, 45, 50] #the list determined in advance

print("Original list: ")
for el in count(25, 5):
    if el > 50:
        break
    else:
        print(f" - {el}")

c = 0
print("Repeating cycle: ")
for i in cycle(e_l):
    if c > 5:
        break
    else:
        print(f" -- {i}")
        c += 1



'''
7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). 
Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
'''

def fact(n):
    p = 1
    for i in range(1, n + 1):
        p *= i
        yield p

n = int(input("Enter your number: "))

for el in fact(n):
    print(el)





