from sympy import *
from prettytable import PrettyTable
import seaborn as sns
from sympy.plotting.plot import MatplotlibBackend, Plot
import sys
import numpy as np

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})


def getEquation(number):
    x = Symbol('x')
    y = Symbol('y')
    match number:
        case 1:
            equation = y + (1+x) * y**2
        case 2:
            equation = y / x
        case 3:
            equation = -2 * y
    return equation


def getAccurate(number, x_0, y_0):
    x = Symbol('x')
    y = Symbol('y')
    match number:
        case 1:
            c = -y_0 * x_0
            equation = -c / x
        case 2:
            try:
                c = y_0 / x_0
            except ZeroDivisionError:
                print("\nНедопустимый интервал, выберите другой")
                sys.exit(0)
            equation = c * x
        case 3:
            c = y_0 / exp(-2 * x_0)
            equation = c * exp(-2 * x)
    return equation


def euler(equation, y_0, h, interval, accurate, epsilon):
    x_0 = interval[0]
    x_n = interval[-1]
    results = []
    table = [['№', 'x_i', 'y_i', 'f(x_i, y_i)', 'Точное решение']]
    table = PrettyTable(table[0])
    counter = 0
    for i in np.arange(x_0, x_n + 0.001, h):
        f = equation.subs([('x', i), ('y', y_0)])
        y_1 = y_0 + h * f
        y_2 = y_0
        p = 2
        if (i != x_0):
            f = equation.subs([('x', i), ('y', y_2)])
            y_2 = y_0 + h / p * f
            while (not runge(y_1, y_2, p, epsilon)):
                p *= 2
                f = equation.subs([('x', i), ('y', y_2)])
                y_2 = y_0 + h / p * f
        
        row = [counter, round(i, 3), round(y_2, 3), round(
            f, 3), round(accurate.subs([('x', i), ('y', y_2)]), 3)]
        table.add_row(row)
        results.append((i, y_2))
        counter += 1
        y_0 = y_1

    print(table)
    return results

def runge(y_1, y_2, p, epsilon):
    return (abs(y_1 - y_2)) / (2**p - 1) <= epsilon

def runge_kutt(equation, y_0, h, interval, accurate, epsilon):
    x_0 = interval[0]
    x_n = interval[-1]
    table = [['№', 'x_i', 'y_i', 'k1', 'k2', 'k3',
        'k4', 'f(x_i, y_i)', 'Точное решение']]
    table = PrettyTable(table[0])
    counter = 0
    results = [] # for plot
    result = [] # for miln
    for i in np.arange(x_0, x_n + 0.001, h):
        k1, k2, k3, k4 = getK(equation, i, h, y_0)

        y_1 = y_0 + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        f = equation.subs([('x', i), ('y', y_0)])
        y_2 = y_0
        p = 2
        if (i != x_0):
            f = equation.subs([('x', i), ('y', y_2)])
            k1, k2, k3, k4 = getK(equation, i / p, h / p, y_2)
            y_2 = y_0 + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            
            while (not runge(y_1, y_2, p, epsilon)):
                p *= 2
                f = equation.subs([('x', i), ('y', y_2)])
                k1, k2, k3, k4 = getK(equation, i / p, h / p, y_2)
                y_2 = y_0 + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                
        acc = (accurate.subs([('x', i), ('y', y_2)]))

        row = [counter, round(i, 3), round(y_2, 3), round(k1, 3), round(k2, 3), round(k3, 3), round(k4, 3), round(f, 3),
        round(acc, 3)]
        result.append((y_2, f))
        results.append((i, y_2))
        table.add_row(row)
        counter += 1
        y_0 = y_1

    print(table)
    return result, results

def getK(equation, i, h, y_0):
    k1 = h * equation.subs([('x', i), ('y', y_0)])
    k2 = h * equation.subs([('x', i + h / 2), ('y', y_0 + k1 / 2)])
    k3 = h * equation.subs([('x', i + h / 2), ('y', y_0 + k2 / 2)])
    k4 = h * equation.subs([('x', i + h), ('y', y_0 + k3)])
    return k1, k2, k3, k4

def miln(h, interval, result, epsilon, equation, accurate):
    y, f = [], []
    y.append(result[0][0])
    y.append(result[1][0])
    y.append(result[2][0])
    y.append(result[3][0])
    
    f.append(result[0][1])
    f.append(result[1][1])
    f.append(result[2][1])
    f.append(result[3][1])
    
    maxEps = -10**6
    x_0 = interval[0]
    x_n = interval[-1]
    counter = 4
    table = [['№', 'x_i', 'y_i', 'f(x_i, y_corr)', 'Точное решение']]
    table = PrettyTable(table[0])
    results = []
    for i in range(4):
        table.add_row([i, round(x_0 + h * i, 3), round(y[i], 3), round(f[i], 3), 
                       round(accurate.subs([('x', x_0 + h * i), ('y', y[i])]), 3)])
        results.append((x_0 + h * i, y[i]))

    for i in np.arange(x_0 + h * 4, x_n + 0.001, h):
        y_progn = y[counter - 4] + 4 * h / 3 * (2 * f[counter - 3] - f[counter - 2] + 2 * f[counter - 1])
        f_progn = equation.subs([('x', i), ('y', y_progn)])
        y_corr = y[counter - 2] + h / 3 * (f[counter - 2] + 4 * f[counter - 1] + f_progn)
        f_corr = equation.subs([('x', i), ('y', y_corr)])
        
        if (i != x_0 + h * 4):
            while (abs(y_corr - y_progn) >= epsilon):
                y_progn = y_corr
                f_progn = equation.subs([('x', i), ('y', y_progn)])
                y_corr = y[counter - 2] + h / 3 * (f[counter - 2] + 4 * f[counter - 1] + f_progn)
                f_corr = equation.subs([('x', i), ('y', y_corr)])
        
        y.append(y_corr)
        f.append(f_corr)
        acc = (accurate.subs([('x', i), ('y', y_corr)]))
        maxEps = max(maxEps, abs(y_corr - acc))
        results.append((i, y_corr))
        row = [counter, round(i, 3), round(y_corr, 3), round(f_corr, 3), round(acc, 3)]
        counter += 1
        table.add_row(row)
    print(table)
    print("\nМаксимальная погрешность maxEps = %0.2f" % (maxEps))
    return results
    
def getInputDataFromConsole():
    print("Выберите дифференциальное уравнение:")
    print("y` = y + (1 + x) * y**2")
    print("y` = y / x")
    print("y` = -2 * y")
    
    number = int(input("Введите номер дифференциального уравнения: "))
    y_0 = float(input("Введите начальное условие (y_0): "))
    interval = input("Введите интервал дифференцирования через пробел: ").replace(",",".").split(" ")
    interval[0], interval[1] = float(interval[0]), float(interval[1])
    h = float(input("Введите шаг h: "))
    epsilon = float(input("Введите точность: "))
    return number, y_0, interval, h, epsilon

def get_sympy_subplots(plot):

    backend = MatplotlibBackend(plot)
    backend.process_series()
    backend.fig.tight_layout()
    return backend.plt

def getPlot(accurate, dotsEuler, dotsRunge_kutt, dotsMiln):

    plt = plot(show=False, legend=True)
    p1 = plot(accurate, ('x', dotsEuler[0][0], dotsEuler[-1][0]),
              show=False, label="accurate")
    plt.append(p1[0])

    plt = get_sympy_subplots(plt)
    for i in range(len(dotsEuler)):
        plt.plot(dotsEuler[i][0], dotsEuler[i][1], "o", color='black')
        plt.plot(dotsRunge_kutt[i][0], dotsRunge_kutt[i][1], "o", color='red')
        plt.plot(dotsMiln[i][0], dotsMiln[i][1], "o", color='green')
    plt.show()


def main():
    number, y_0, interval, h, epsilon = getInputDataFromConsole()
    
    equation = getEquation(number)
    accurate = getAccurate(number, interval[0], y_0)
    
    print("Эйлер: ")
    dotsEuler = euler(equation, y_0, h, interval, accurate, epsilon)
        
    print("Рунге-Кутт: ")
    result, dotsRunge_kutt = runge_kutt(equation, y_0, h, interval, accurate, epsilon)
    
    print('Метод Милна: ')
    dotsMiln = miln(h, interval, result, epsilon, equation, accurate)
    
    getPlot(accurate, dotsEuler, dotsRunge_kutt, dotsMiln)
        
main()