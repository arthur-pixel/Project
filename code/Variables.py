print('''Задание 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько
чисел и строк и сохраните в переменные, выведите на экран.
''')

print("Enter your personnel information as required below:")
name = input("Enter your name: ")
age = input("Enter your full age: ")
prof = input("Enter your profession: ")
experience = input("Enter your working experience in years: ")
print("Your profile summary is: "'\n'f" Name: {name}'\n'Age: {age}'\n'Proffesion: {prof}'\n'Experience: {experience}")

print('''Задание 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и 
выведите в формате чч:мм:сс. Используйте форматирование строк.
''')

print("Time transition from seconds to hours & minutes you will be asked to enter the time in seconds below")
sec = int(input("Enter the time in seconds: "))
hours = (sec // 3600)
minutes = sec % 3600 / 60
seconds = sec % 60
if seconds == 0:
    print(hours, '{:.0f}'.format(minutes), sep=':')
else:
    print(hours, '{:.0f}'.format(minutes), seconds, sep=':')

print('''Задание 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. 
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
''')

print("Enter your number for the add+ calculations below")
number = input("Enter your number: ")
interim = number + number
interim2 = number + number + number
result = int(number) + int(interim) + int(interim2)
print("Comulative sum is: ", result)

print(''' Задание 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
''')

userInput = int(input("Enter your number: "))
max = 0
while userInput > 0:
    c = userInput % 10
    if c > max:
        max = c
    userInput //= 10
print("Max number in the array: ", max)

print(''' Задание 5. Запросите у пользователя значения выручки и издержек фирмы. 
Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). 
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
''')

curr = input("Enter your currency: ")
income = int(input("Enter your income value: "))
costs = int(input("Enter your costs value: "))
margine = income - costs
if income > costs:
    print("Company's profit stands at: ", "+", '{:.2f}'.format(100 - (costs / income) * 100), "% and the income value\namount is: ", income - costs, curr)
    rent = '{:.2f}'.format(income / margine)
    print("Company's profit is: ", rent, "%")
    emplShare = int(input("How many employees in your company: "))
    print("Average employee share in the profit: ", '{:.1f}'.format(margine / emplShare), curr, "which is: ", '\n', '{:.1f}'.format(((margine / emplShare) / margine) * 100), "% of the margine")
else:
    print("Company's losses stands at: ", "-", '{:.2f}'.format(100 - (income / costs) * 100), "% and the loss is: ", costs - income, curr)


print('''Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. 
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который 
общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и 
выводить одно натуральное число — номер дня.
''')

km = int(input("Сколько пробежал спортсмен в 1-й день, km?: "))
r = str(km)
day = int(input("Возможный прогресс к n - му дню. Введите номер дня: "))
print("Чтобы узнать сколько дней потребуется бегуну, чтобы достичь определенного километража введите км ниже:")
res = int(input("Введите километраж: "))
j = str(res)
incr = int(input("Процент ежедневного прогресса спортсмена в целых натуральных числах: "))
if km == 0:
    print("Увы! Но наш бегун еще и не пробовал практиковаться:)")
    exit()
elif day == 1:
    print("Уже на:", day, "день он достигнет результата: ", km)
    exit()
else:
    p = incr / 100
    i = 2
    while i <= day:
        d = km * p + km
        km = d
        i += 1
print("На:", day, "день спортсмен достигнет показателя в: ", '{:.1f}'.format(d), "km")
if res == 0:
    print()
    exit()
else:
    t = (incr + 100) / 100
    c = 0
    while res >= int(r):
        s = res / t
        res = s
        c += 1
print("Чтобы достичь показателя в: ", j, "km спортсмену понадобиться", '{:.0f}'.format(c), "дней")

