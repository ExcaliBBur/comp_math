from sympy import *
from prettytable import PrettyTable
import seaborn as sns
from sympy.plotting.plot import MatplotlibBackend, Plot
import sys

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

FILE_OUT = "output.txt"
output = ''
dots = []
a, b, c, d, x= symbols("a b c d x")
A, B = symbols("A B")

first = a * x + b
second = a * x**2 + b * x + c
third = a * x ** 3 + b * x ** 2 + c * x + d
fourth = a * x ** b
linFourth = A + b * log(x)
fifth = a * exp(b * x)
linFifth = A + b * x
sixth = a * log(x) + b

minDelta = 10**12
minExpr = ''
plt = plot(show=False, legend = True)

def chooseInputType():
    type = input("Откуда брать данные о точках? 1 - консоль; 2 - файл\n")
    while (type != '1' and type != '2'):
        type = input("Откуда брать данные о точках? 1 - консоль; 2 - файл\n")
    return type

def getInputDataFromFile():
    global output
    
    file_name = input("Введите имя файла: ")
    try:
        file = open(file_name)
        output = file.readline().strip()
        data = file.read().replace(",", ".").split("\n")
        for dot in data:
            if len(dot.split(" ")) != 2:
                print("Предупреждение: при считывании информации о точках из файла произошла ошибка")
                
        if (len(data) < 8):
            print("Предупреждение: количество точек должно быть больше или равно 8")
            
        if (len(data) > 12):
            print("Предупреждение: количество точек должно быть меньше или равно 12")
        return data
    except (FileNotFoundError):
        print("Указанный файл не найден.")
        sys.exit(0)
    
def getInputDataFromConsole():
    global output
    
    data = []
    n = int(input("Введите количество точек: "))
    if (n < 8):
        print("Предупреждение: количество точек должно быть больше или равно 8")
    if (n > 12):
        print("Предупреждение: количество точек должно быть меньше или равно 12")
    for i in range(1, n + 1):
        line = input(f"Введите координаты {i:d} точки через пробел: ").replace(",", ".")
        data.append(line)
    output = input("Куда выводить результаты? 1 - консоль; 2 - файл output.txt\n")
    while (output != '1' and output != '2'):
        output = input("Куда выводить результаты? 1 - консоль; 2 - файл output.txt\n")
    return data
    
    
def linAppr(expression, x, y):
    
    s = sum([(expression.subs('x', float(x[i])) - float(y[i]))**2 for i in range(len(x))])
    
    derivative = []
    for i in s.free_symbols:
        derivative.append(s.diff(i))
    
    symbols = tuple(s.free_symbols)
    params = list(linsolve(derivative, symbols))
    
    ans = []
    for i in range (len(symbols)):
        s = s.subs(symbols[i], params[0][i])
        ans.append(symbols[i])
        ans.append(params[0][i])
    
    return ans
    
    
def printResults(expression, answer, x, y, file):
    global minDelta
    global minExpr
    
    for i in range(0, len(answer), 2):
        expression = expression.subs(answer[i], round(answer[i+1], 4))
    table = [['№ итерации', 'x', 'y', expression, 'epsilon']]
    table = PrettyTable(table[0])
    counter = 1
    for i in range(len(x)):
        row = [counter, x[i], y[i], round(expression.subs('x', x[i]), 4), round(expression.subs('x', x[i]) - float(y[i]), 4)]
        counter += 1
        table.add_row(row)
    if (output == '1'):
        print()
        print(table)
    else:
        file.write("\n")
        file.write(str(table) + '\n')
    
    s = sum([(expression.subs('x', float(x[i])) - float(y[i]))**2 for i in range(len(x))])

    if (output == '1'):
        print(f"S = {round(s, 4):f}")
    else:
        file.write(f"S = {round(s, 4):f}\n")
    delta = round((s / len(x))**0.5, 4)
    
    if (delta < minDelta):
        minDelta = delta
        minExpr = expression
    if (output == '1'):
        print(f"delta = {delta:f}\n")
    else:
        file.write(f"delta = {delta:f}\n")
    
    
def getPirson(x, y):
    meanX = sum([float(i) for i in x]) / len(x)
    meanY = sum([float(i) for i in y]) / len(y)
    
    numerator = 0
    for i in range(len(x)):
        numerator += (float(x[i]) - meanX) * (float(y[i]) - meanY)
        
    denominator = (sum([(float(i) - meanX)**2 for i in x]) * sum([(float(i) - meanY)**2 for i in y]))**0.5
    return numerator / denominator
    
    
def getPlot(expression, answer, x):
    global plt
    
    for i in range(0, len(answer), 2):
        expression = expression.subs(answer[i], round(answer[i+1], 4))
    
    p1 = plot(expression, ('x', float(min(x)), float(max(x)) + 2), show=False, label = expression)
    plt.append(p1[0])
    
    
def get_sympy_subplots(plot):
    
    backend = MatplotlibBackend(plot)
    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt


def transformA(answer):
    for i in range(0, len(answer) - 1, 2):
        if (str(answer[i]) == 'A'):
            answer[i + 1] = exp(answer[i + 1])
            answer[i] = Symbol('a')
    return answer


def main():
    
    type = chooseInputType()
    if (type == '1'):
        dots = getInputDataFromConsole()
    else:
        dots = getInputDataFromFile()
    x = [dot.split(" ")[0] for dot in dots]
    y = [dot.split(" ")[1] for dot in dots]
    file = ''
    if (output != '1'):
        file = open(FILE_OUT, 'w', encoding='utf8')
        
    firstAns = linAppr(first, x, y)
    printResults(first, firstAns, x, y, file)
    if (output == '1'):
        print(f"Коэффициент корреляции Пирсона = {getPirson(x, y):f}")
    else:
        file.write(f"Коэффициент корреляции Пирсона = {getPirson(x, y):f}\n")
    getPlot(first, firstAns, x)
    
    secondAns = linAppr(second, x, y)
    printResults(second, secondAns, x, y, file)
    getPlot(second, secondAns, x)


    thirdAns = linAppr(third, x, y)
    printResults(third, thirdAns, x, y, file)
    getPlot(third, thirdAns, x)
    
    transformedY = [log(i) for i in y]
    try:
        fourthAns = linAppr(linFourth, x, transformedY)
        fourthAns = transformA(fourthAns)
        printResults(fourth, fourthAns, x, y, file)
        getPlot(fourth, fourthAns, x)
    except (Exception):
        if (output == '1'):
            print(50*'-')
            print(f"Невозможно найти функцию вида {str(fourth):s}")
            print(50*'-')
        else:
            file.write(50*'-')
            file.write(f"Невозможно найти функцию вида {str(fourth):s}")
            file.write(50*'-')
    
    try:
        fifthAns = linAppr(linFifth, x, transformedY)
        fifthAns = transformA(fifthAns)
        printResults(fifth, fifthAns, x, y, file)
        getPlot(fifth, fifthAns, x)
    except (Exception):
        if (output == '1'):
            print(50*'-')
            print(f"Невозможно найти функцию вида {str(fifth):s}")
            print(50*'-')
        else:
            file.write(50*'-')
            file.write(f"Невозможно найти функцию вида {str(fifth):s}")
            file.write(50*'-')
    
    sixthAns = linAppr(sixth, x, y)
    printResults(sixth, sixthAns, x, y, file)
    getPlot(sixth, sixthAns, x)
    
    if (output == '1'):
        print(f"Наименьшее среднеквадратичное отклонение delta = {minDelta:f} у функции {str(minExpr):s}")
    else:
        file.write(f"Наименьшее среднеквадратичное отклонение delta = {minDelta:f} у функции {str(minExpr):s}\n")
        print("Результаты успешно записаны в файл output.txt")
        file.close()
    
    plt1 = get_sympy_subplots(plt)
    for i in range(len(x)):
        plt1.plot(float(x[i]), float(y[i]), "o", color = 'black')
    plt1.show()
    
main()