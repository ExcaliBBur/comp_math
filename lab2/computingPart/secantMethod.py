from prettytable import PrettyTable

# Средний корень

def F(x):
    return x**3 - 2.56 * x**2 - 1.325 * x + 4.395

def digitsAfterPoint(number):
    if (str(number).find(".") == -1):
        return number
    digitsAfter = 3                                                # TODO: при сдаче поменять на 3
    number = str(number).split(".")
    return number[0] + "." + number[1][:digitsAfter]

x_0 = 1
x_1 = 2
table = [['№ итерации', 'x_(i-1)', 'x_(i)', 'x_(i+1)', 'F(x_(i+1))', '|x_(i+1) - x_(i)|']]
table = PrettyTable(table[0])
epsilon = 0.01
x_2 = 0
counter = 0
while (True):
    x_2 = x_1 - (x_1 - x_0) / (F(x_1) - F(x_0)) * F(x_1)
    row = [digitsAfterPoint(counter), digitsAfterPoint(x_0), digitsAfterPoint(x_1), digitsAfterPoint(x_2), 
           digitsAfterPoint(F(x_2)), digitsAfterPoint(abs(x_2 - x_1))]
    table.add_row(row)
    if (abs(x_1 - x_2) <= epsilon):
        break
    x_0 = x_1
    x_1 = x_2
    counter += 1
    
print(table)