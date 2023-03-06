from prettytable import PrettyTable

# Левый корень

def F(x):
    return x**3 - 2.56 * x**2 - 1.325 * x + 4.395

def digitsAfterPoint(number):
    if (str(number).find(".") == -1):
        return number
    digitsAfter = 3                                                # TODO: при сдаче поменять на 3
    number = str(number).split(".")
    return number[0] + "." + number[1][:digitsAfter]

a = -2.0
b = -1.0
epsilon = 0.01
x = 0
table = [['№ итерации', 'a', 'b', 'x', 'F(a)', 'F(b)', 'F(x)', '|a-b|']]
table = PrettyTable(table[0])
counter = 0
while (True):
    x = (a+b) / 2
    resA = F(a)
    resB = F(b)
    resX = F(x)
    row = [digitsAfterPoint(counter), digitsAfterPoint(a), digitsAfterPoint(b), digitsAfterPoint(x),
           digitsAfterPoint(resA), digitsAfterPoint(resB), digitsAfterPoint(resX), digitsAfterPoint(abs(a-b))]
    if (resA * resX < 0):
        b = x
    else:
        a = x
    if (abs(a-b) <= epsilon):
        break
    counter += 1
    table.add_row(row)
print(table)
