
#1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.



def __userinfo__():
    global u_inf
    u_inf = []
    while True:

        u_inp = input("Print in what you think about Python: ")
        u_inf.append(u_inp)

        if not u_inp:
            print("End of input")
            break
    for i in u_inf:
        print(i)
    return print(f"The info you've just sent to the targeted file is: {u_inf}")

print(__userinfo__())

task1 = open("Less5.txt", "w", encoding="utf-8")
for line in u_inf:
    content = task1.write(line + '\n')
task1.close()



#2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
#количества слов в каждой строке.



t_c = open(r"C:\Users\staln\PycharmProjects\Py_basics\engl_proverbs.txt", "r", encoding="utf-8")
c = 1
for l in t_c:
    #length = len(l)
    #print(f"- row {c} has {length} bt")
    #c += 1
print(f"Total lines qty: {c - 1}")



#3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней
#величины дохода сотрудников.


from statistics import mean
with open("Employees.txt", "r", encoding="utf-8") as file:
    salaries = []
    for empl in file:
        name, salary = empl.split(' ')
        salary = float(salary)
        if salary < 20_000:
            print("Salaries below the average:")
            print(name, salary)
        salaries.append(salary)
    print("The average salary level is: ", round(mean(salaries), 2))


'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские 
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''


a = open('En_Ru.txt', 'r+', encoding="utf-8")

c = []
for i in a:
    c.append(i)

for i in c:
    c[0] = 'Один - 1\n'
    c[1] = 'Два - 2\n'
    c[2] = 'Три - 3\n'
    c[3] = 'Четыре - 4\n'

b = open('Ru.txt', 'w', encoding="utf-8")
b.writelines(c)
b = open('Ru.txt', 'r', encoding="utf-8")

for i in b:
    print(i, end='')
a, b.close()



#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.



with open("num.txt", 'w', encoding='utf-8') as n:
    arr = []
    for i in range(20, 100, 10):
        n.write(str(i))
        n.write(' ')
        arr.append(i)
    print(f"The new list which will be added to the {n} file:\n{arr}")



o = open("num.txt", 'r', encoding='utf-8')
con = o.readline().split()
s = []
for el in con:
    el = int(el)
    s.append(el)
res = sum(s)
print(f"The sum of numbers in the file is: {res}")
o.close()


'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
'''


with open("task6.txt", "r", encoding="utf-8") as t:

    my_list = []
    for i in t.read().split('\n'):
        v = i.split(":")
        my_list.append(v)
    my_list = dict(my_list)
    print(my_list)



#7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название,
#форма собственности, выручка, издержки.


import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open("TryJson.txt", 'r') as file:
    for el in file:
        name, firm, revenue, losses = el.split()
        profit[name] = int(revenue) - int(losses)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_ave = prof / i
        print(f'Average profit - {prof_ave:.2f}')
    else:
        print(f'Average profit is 0')
    pr = {'Average profit': round(prof_ave)}
    profit.update(pr)
    print(f'Companies profit each - {profit}')

with open("TryJson.json", 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'A file with extension ".json" has been created: \n '
          f' {[js_str]}')

















