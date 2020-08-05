#1. Задание "Матрица"

class Matrix:

    def __init__(self, l1, l2):
        self.l1 = l1
        self.l2 = l2

    def __add__(self):
        mtx = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]

        for i in range(len(self.l1)):

            for f in range(len(self.l2[i])):
                mtx[i][f] = self.l1[i][f] + self.l2[i][f]

        return str('\n'.join('\t'.join(str(f) for f in i) for i in mtx))

    def __str__(self):
        mtx = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
        for i in range(len(self.l1)):

            for f in range(len(self.l2[i])):
                mtx[i][f] = self.l1[i][f] + self.l2[i][f]
        return str('\n'.join('\t'.join(str(f) for f in i)for i in mtx))

mx = Matrix([[1, 2, 3, 4], [4, 5, 6, 4], [7, 8, 9, 4]], [[2, 3, 4, 4], [5, 6, 7, 4], [8, 9, 10, 4]])
print(mx.__add__())
#print(mx.__str__())


#Задание 2 Пальто и костюм

class Clothes:

    def __init__(self, coat, suit):
        self.coat = coat
        self.suit = suit

class Materials(Clothes):

    def mtr_coat(self):
        return f'Subtotal for the coat is:\n{round((self.coat / 6.5 + 0.5), 2)}'

    def mtr_suit(self):
        return f'Subtotal for the suit is:\n{round((2 * self.suit + 0.3), 2)}'

    @property
    def mat_count(self):
        return f"Total textile materials used for producing is:\n" \
               f"{round((self.coat / 6.5 + 0.5) + (2 * self.suit + 0.3), 2)}"

cl = Materials(2, 1.8)
print(cl.mat_count)
print(cl.mtr_coat())
print(cl.mtr_suit())


#3 Органические клетки и работа с ними

class OrgCell:

    def __init__(self, qty):
        self.qty = int(qty)

    def __add__(self, other):
        return self.qty + other.qty

    def __str__(self):
        return f'Result of string method: {self.qty * "*"}'

    def __sub__(self, other):
        return self.qty - other.qty if (self.qty - other.qty) > 0 else print("Deduction is impossible")

    def __mul__(self, other):
        return int(self.qty * other.qty)

    def __truediv__(self, other):
        return int(self.qty // other.qty)

    def make_order(self, cellr):
        r = ''
        for i in range(int(self.qty / cellr)):
            r += f'{"*" * cellr} \\n'
        r += f'{"*" * (self.qty % cellr)}'
        return r

cells1 = OrgCell(50)
cells2 = OrgCell(60)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(9))
print(cells1.make_order(5))
print(cells1 / cells2)



