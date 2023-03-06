from prettytable import PrettyTable

# Правый корень

def F(x):
    return x**3 - 2.56 * x**2 - 1.325 * x + 4.395

def phi(x):
    return -0.0969462 * x**3  + 0.248182 * x**2 + 1.12845 * x - 0.426

def digitsAfterPoint(number):
    if (str(number).find(".") == -1):
        return number
    digitsAfter = 3                                               # TODO: при сдаче поменять на 3
    number = str(number).split(".")
    return number[0] + "." + number[1][:digitsAfter]

x_0 = 3.0
table = [['№ итерации', 'x_(i)', 'x_(i+1)', 'phi(x_(i+1))', 'F(x_(i+1))' , '|x_(i+1) - x_(i)|']]
table = PrettyTable(table[0])
epsilon = 0.01
counter = 0
x_1 = 0
while (True):
    x_1 = phi(x_0)
    row = [digitsAfterPoint(counter), digitsAfterPoint(x_0), digitsAfterPoint(x_1), digitsAfterPoint(phi(x_1)), 
           digitsAfterPoint(F(x_1)), digitsAfterPoint(abs(x_1 - x_0))]
    table.add_row(row)
    counter += 1
    if (abs(x_0 - x_1) <= epsilon):
        break
    x_0 = x_1
print("Метод простой итерации:")
print(table)
print("x = ", x_1)