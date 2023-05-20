from sympy import *
from prettytable import PrettyTable
import seaborn as sns
from sympy.plotting.plot import MatplotlibBackend, Plot
import sys

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def chooseEquation():
    print("Выберите функцию, с помощью которой необходимо исследовать интервал: ")
    print("1 - sin(x)\n2 - x^3")
    number = int(input("Выберите функцию: "))

    while (number != 1 and number != 2):
        print("Введите число от 1 до 2")
        number = int(input("Выберите функцию: "))
    interval = input("\nВведите интервал, на котором будут взяты точки через пробел: ").replace(
        ",", ".").split(" ")
    numberOfDots = int(
        input("\nВведите количество точек на заданном интервале: "))

    while (numberOfDots <= 0):
        print("Количество точек не может быть меньше нуля")
        numberOfDots = int(
            input("Введите количество точек на заданном интервале: "))
    return number, interval, numberOfDots


def getDotsOnInterval(number, interval, numberOfDots):
    interval[0], interval[1] = float(interval[0]), float(interval[1])
    dots = []
    if (interval[1] < interval[0]):
        interval[1], interval[0] = interval[0], interval[1]
    x_0 = interval[0]
    h = (abs(interval[0]) + abs(interval[1])) / numberOfDots
    while (x_0 < interval[1]):
        dots.append(str(x_0) + ' ' + str(F(getEquation(number), x_0)))
        x_0 += h
    return dots


def getEquation(number):
    x = Symbol('x')
    match number:
        case 1:
            equation = sin(x)
        case 2:
            equation = x**3
    return equation


def F(equation, x):
    return equation.subs('x', x)


def chooseInputType():
    type = input(
        "Откуда брать данные о точках? 1 - консоль; 2 - файл; 3 - на основе выбранной функции\n")
    while (type != '1' and type != '2' and type != '3'):
        type = input(
            "Откуда брать данные о точках? 1 - консоль; 2 - файл; 3 - на основе выбранной функции\n")
    return type


def getX():
    return float(input("Введите точку, для которой требуется вычислить приближенное значение: "))


def printDots(dotsX, dotsY):
    table = [['№', 'x_i', 'y_i']]
    table = PrettyTable(table[0])

    for i in range(len(dotsX)):
        row = [i, round(dotsX[i], 3), round(dotsY[i], 3)]
        table.add_row(row)

    print('\nПолученные точки: ')
    print(table)


def getInputDataFromFile():
    file_name = input("Введите имя файла: ")
    try:
        file = open(file_name)
        x = float(file.readline().replace(",", "."))
        data = file.read().replace(",", ".").split("\n")
        for dot in data:
            if len(dot.split(" ")) != 2:
                print(
                    "Предупреждение: при считывании информации о точках из файла произошла ошибка")

        return data, x
    except (FileNotFoundError):
        print("Указанный файл не найден.")
        sys.exit(0)


def getInputDataFromConsole():
    data = []
    n = int(input("Введите количество точек: "))

    for i in range(1, n + 1):
        line = input(
            f"Введите координаты {i:d} точки через пробел: ").replace(",", ".")
        data.append(line)
    x = float(
        input("Введите точку, для которой требуется вычислить приближенное значение: "))
    return data, x


def checkIfDotInBounds(dotsX, x):
    if (x > dotsX[-1] or x < dotsX[0]):
        print("Точка находится вне отрезка")
        return False
    return True


def lagrange(dotsX, dotsY, x_0):
    if (not checkIfDotInBounds(dotsX, x_0)):
        return None, None

    x = Symbol('x')
    ans = []
    for i in range(len(dotsX)):
        numerator = denominator = 1
        for j in range(len(dotsX)):
            if i != j:
                numerator *= x - dotsX[j]
                denominator *= dotsX[i] - dotsX[j]
        res = dotsY[i] * numerator / denominator
        ans.append(res)
    polinom = simplify(sum(ans))

    return polinom.subs(x, x_0), polinom


def checkNewtonIsCorrect(dotsX):
    h = dotsX[1] - dotsX[0]
    epsilon = 10**(-4)
    for i in range(2, len(dotsX) - 1):
        if (abs(dotsX[i + 1] - dotsX[i] - h) > epsilon):
            return False
    return True


def printFiniteDiff(finiteDiff, dotsX):
    table = [['№', 'x_i', 'y_i']]
    for i in range(1, len(dotsX)):
        if i == 1:
            table[0].append(f'delta y_i')
        else:
            table[0].append(f'delta^{i:d} y_i')
    table = PrettyTable(table[0])

    for i in range(len(dotsX)):
        row = [i, round(dotsX[i], 3)]
        for j in range(len(dotsX)):
            if (finiteDiff[i][j] == '0'):
                row.append('')
            else:
                row.append(round(finiteDiff[i][j], 3))
        table.add_row(row)

    print('Таблица конечных разностей: ')
    print(table)


def newton(dotsX, dotsY, x):
    if (not checkIfDotInBounds(dotsX, x)):
        return None, None

    if (not checkNewtonIsCorrect(dotsX)):
        print("Формула Ньютона неприменима для не равностоящих узлов.")
        return None, None

    h = dotsX[1] - dotsX[0]
    a = [['0'] * len(dotsX) for _ in range(len(dotsX))]

    for i in range(len(dotsX)):
        a[i][0] = dotsY[i]

    for i in range(1, len(dotsX)):
        for j in range(len(dotsX) - i):
            a[j][i] = round(a[j + 1][i - 1] - a[j][i - 1], 3)

    printFiniteDiff(a, dotsX)
    symX = Symbol('x')

    if (x < (dotsX[-1] + dotsX[0]) / 2):
        x_0 = dotsX[-1]
        for i in dotsX:
            if (x > i):
                x_0 = i
            else:
                break

        t = ((symX - x_0) / h)
        print("Исходная точка находится в левой половине отрезка. Применяем интерполирование вперёд")

        print("\nx_0 = %0.2f" % (x_0))
        print("t = %0.2f" % (float(t.subs(symX, x))))
        
        index = dotsX.index(x_0)
        result = a[index][0]

        for i in range(1, len(dotsX)):
            resT = t
            for k in range(1, i):
                resT *= t - k
            result += float(a[index][i]) * resT / factorial(i)
            print('Задействованные конечные разности: %0.2f' % (float(a[index][i])))

    else:
        t = (symX - dotsX[-1]) / h
        result = a[len(dotsX) - 1][0]

        for i in range(1, len(dotsX)):
            resT = t
            for k in range(1, i):
                resT *= t + k
            result += a[len(dotsX) - 1 - i][i] * resT / factorial(i)
        print("Исходная точка находится в правой половине отрезка. Применяем интерполирование назад")
    polinom = simplify(result)
    return polinom.subs(symX, x), polinom


def get_sympy_subplots(plot):

    backend = MatplotlibBackend(plot)
    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt


def getPlot(lagr, newt, dotsX, dotsY):
    lagr1 = lagr
    newt1 = newt
    for a in preorder_traversal(lagr):
        if isinstance(a, Float):
            lagr1 = lagr1.subs(a, round(a, 2))
    for a in preorder_traversal(newt):
        if isinstance(a, Float):
            newt1 = newt1.subs(a, round(a, 2))

    plt = plot(show=False, legend=True)
    p1 = plot(lagr, ('x', dotsX[0], dotsX[-1]),
              show=False, label=str(lagr1) + " lagrange")
    plt.append(p1[0])

    if (newt != None):
        p2 = plot(newt, ('x', dotsX[0], dotsX[-1]),
                  show=False, label=str(newt1) + " newton")
        plt.append(p2[0])
    plt = get_sympy_subplots(plt)
    for i in range(len(dotsX)):
        plt.plot(dotsX[i], dotsY[i], "o", color='black')
    plt.show()


def main():
    numberOfType = chooseInputType()
    match numberOfType:
        case '1':
            dots, x_0 = getInputDataFromConsole()
        case '2':
            dots, x_0 = getInputDataFromFile()
        case '3':
            number, interval, numberOfDots = chooseEquation()
            dots = getDotsOnInterval(number, interval, numberOfDots)
            x_0 = getX()

    x = [float(dot.split(" ")[0]) for dot in dots]
    y = [float(dot.split(" ")[1]) for dot in dots]

    if (numberOfType == '3'):
        printDots(x, y)

    ansLagr, polinomLagr = lagrange(x, y, x_0)
    if (ansLagr != None):
        print("\nМногочлен Лагранжа: приближенное значение функции в точке %0.2f = %0.3f\n" % (
            x_0, ansLagr))

    ansNewt, polinomNewt = newton(x, y, x_0)
    if (ansNewt != None):
        print("Многочлен Ньютона с конечными разностями: " +
              "приближенное значение функции в точке %0.3f = %0.3f\n" % (x_0, ansNewt))

    if (ansLagr != None and ansNewt != None):
        print("Результаты, полученные методом Лагранжа и методом Ньютона отличаются на %0.3f" % (
            abs(ansLagr - ansNewt)))
    if (ansLagr != None):
        getPlot(polinomLagr, polinomNewt, x, y)


main()
