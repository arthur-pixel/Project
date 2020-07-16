'''1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
'''

c = [True, 456 , 'Python', 3.8]
print(type(c))
print(type(c[0]), type(c[1]), type(c[2]), type(c[3]))


'''2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 
0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''

el_Num = list(map(int, input("Enter some number of natural numbers: ").split()))
n = 0
m = 1
for i in range(len(el_Num) // 2):
    print("\n The initial list was: ", i, el_Num)
    el_Num[n], el_Num[m] = el_Num[m], el_Num[n]
    print("Now it has been changed to: ", el_Num)
    n += 2
    m += 2


'''3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц 
(зима, весна, лето, осень). Напишите решения через list и через dict.
'''
print("Season of the month form Dictionary")
d = {
'1' : 'winter',
'2' : 'winter',
'3' : 'Spring',
'4' : 'Spring',
'5' : 'Spring',
'6' : 'summer',
'7' : 'Summer',
'8' : 'Summer',
'9' : 'Autumn',
'10' : 'Autumn',
'11' : 'Autumn',
'12' : 'Winter'}
chk = input("Enter the month number: ")
print(d.get(chk))
print("Season of the month from the list")
month_num = ['Winter', 'Winter', 'Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn', 'Autumn', 'Winter']
chck = int(input("Enter the month number: "))
chck -= 1
print(month_num[chck])


'''4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки необходимо пронумеровать. Если слово длинное, 
выводить только первые 10 букв в слове.
'''
userInput = input("Enter your sentence: ")
spl = userInput.split()
count = 0
for lsp in spl:
    count += 1
    print(count, ".", lsp[:10], sep='')

'''5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.'''

rating = list(map(int, input("Enter the array to represent the rating scale: ").split()))
my_list = rating
print(my_list)
rate = int(input("Input your rate here: "))
for i in my_list:
    if rate == i:
        n = my_list.index(i)
        my_list.insert(n, rate)
        break
print("My rating has been updated with the new mark: ", rate)
print("Rating status has been changed: ", my_list)
mini = min(my_list)
if rate < min(my_list):
    min_rate = my_list.index(min(my_list))
    my_list.insert(min_rate + 1, rate)
    maxi = max(my_list)
if rate > max(my_list):
    max_rate = my_list.index(max(my_list))
    my_list.insert(max_rate, rate)
else:
    my_list.append(rate)
print("Thanks for rating my code!")
print("Current rating status is: ", my_list)

'''6. Реализовать структуру данных товара...
'''
print("Goods data structure")
bld_str = ['Item name', 'Item price', 'Item quantity', 'Type of measurements']
name = input("Enter the item name: ")
insName = []
insName.append(name)
price = input("Enter the price: ")
insPrice = []
insPrice.append(price)
qty = input("Enter the quantity: ")
insQty = []
insQty.append(qty)
item_spec = input("Enter the item measurement: ")
insMeas = []
insMeas.append(item_spec)
goods_info = {bld_str[0]: insName[0], bld_str[1]: insPrice[0], bld_str[2]: insQty[0], bld_str[3]: insMeas[0]}
a = str(goods_info)
print("1", a)
