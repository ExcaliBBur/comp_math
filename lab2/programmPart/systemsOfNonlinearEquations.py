from sympy import *
from matplotlib import pyplot as plt
import sys
import seaborn as sns

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

system = []
numberOfSystem = 0
x = Symbol('x')
y = Symbol('y')
epsilon = 0
x_0, y_0 = 0, 0
solutions = []


def firstPrivateDiff(equation, symbol):
    return diff(equation, symbol)


def getPlot(coordX, coordY, isRoot):
    if (isRoot):
        plot1 = plot_implicit(system[0], aspect_ratio=(1, 1), show=False, line_color="blue",
                          markers=[{'args': [coordX, coordY], 'color': "black", 'marker': "o", 'ms': 5}] )
    else:
        plot1 = plot_implicit(system[0], aspect_ratio=(1, 1), show=False, line_color="blue")
        
    plot2 = plot_implicit(system[1], aspect_ratio=(1, 1), 
                          show=False, line_color="red")
    plot1.append(plot2[0])
    plot1.show()


def chooseSystem():
    global system
    match numberOfSystem:
        case 1:
            system = [x**2 - 2 * y**2 - x * y + 2 * x -
                      y + 1, 2 * x**2 - y**2 + x * y + 3 * y - 5]
        case 2:
            system = [3 * x**2 * y**2 + x**2 - 3 * x * y - 7,
                      10 * x**2 * y**2 + 3 * x**2 - 20 * x * y - 3]
        case 3:
            system = [(x + 2 * y) * (2 * x - y + 1) - 6,
                      (2 * x - y + 1) / (x + 2 * y) - 2 / 3]
        case 4:
            system = [x**2 + y**2 - 4, y - 3 * x**2]


def getInputData():
    global numberOfSystem
    global x_0, y_0
    global epsilon

    print("Доступные системы нелинейных уравнений:")
    print("1: x^2 - 2y^2 - xy + 2x - y + 1 = 0; 2x^2 - y^2 + xy + 3y - 5 = 0")
    print("2: 3x^2 y^2 + x^2 - 3xy - 7 = 0; 10x^2 y^2 + 3x^2 - 20xy - 3 = 0")
    print("3: (x + 2y)(2x - y + 1) - 6 = 0; (2x - y + 1)/(x + 2y) - 2/3 = 0")
    print("4: x^2 + y^2 - 4 = 0; y = 3x^2")
    while (True):
        try:
            numberOfSystem = int(
                input("Выберите систему уравнений, корни которой необходимо вычислить: "))
            if (numberOfSystem < 1 or numberOfSystem > 4):
                raise ValueError
            else:
                chooseSystem()
                break
        except ValueError:
            print("\nВведено неправильное значение, выберите систему от 1 до 4\n")

    getPlot(0, 0, false)
    
    print("\nВведите два начальных приближения через пробел: ")

    while (True):
        try:
            x_0, y_0 = map(float, input(
                "Начальные приближения: ").replace(",", ".").split(" "))
            break
        except ValueError:
            print("\nНедопустимый формат. Введите начальные приближения через пробел\n")

    print("\nВведите погрешность вычислений:")

    while (True):
        try:
            epsilon = float(
                input("Погрешность вычислений: ").replace(",", "."))
            break
        except ValueError:
            print("\nНеверный формат ввода\n")


def newtonMethod():
    global x_0, y_0
    global solutions

    jakobian = [[firstPrivateDiff(system[0], x), firstPrivateDiff(system[0], y)],
                [firstPrivateDiff(system[1], x), firstPrivateDiff(system[1], y)]]
    dx = Symbol("dx")
    dy = Symbol("dy")

    first = jakobian[0][0] * dx + jakobian[0][1] * dy + system[0]
    second = jakobian[1][0] * dx + jakobian[1][1] * dy + system[1]

    counter = 0

    while (True):
        newSystem = [first.subs([(x, x_0), (y, y_0)]),
                     second.subs([(x, x_0), (y, y_0)])]
        try:
            solutions = linsolve(newSystem, (dx, dy)).args[0]
        except IndexError:
            print("При выполнении метода произошла ошибка: невозможно точно вычислить один или два корня.",
                  "Попробуйте выбрать другие начальные приближения")
            sys.exit(0)
            
        x_1 = x_0 + solutions[0]
        y_1 = y_0 + solutions[1]
        counter += 1

        if (abs(max(solutions[0], solutions[1])) <= epsilon or ((abs(x_1 - x_0) <= epsilon) and abs(y_1 - y_0) <= epsilon)):
            break
        if (counter >= 200):
            print("Метод не смог отработать за 200 итераций.")
            sys.exit(0)
        
        x_0 = x_1
        y_0 = y_1

    print("\nМетод отработал за", counter, "итераций")
    print("x =", float(x_0), "; y =", float(y_0))
    r1 = abs(float(system[0].subs([(x, x_0), (y, y_0)])))
    r2 = abs(float(system[1].subs([(x, x_0), (y, y_0)])))
    print("Вектор невязок: r1 =", r1, "; r2 =", r2)
    getPlot(x_0, y_0, true)


getInputData()
newtonMethod()
