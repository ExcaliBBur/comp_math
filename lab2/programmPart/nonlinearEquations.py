import numpy as np
from sympy import *
from prettytable import PrettyTable
from matplotlib import pyplot as plt
import sys
import seaborn as sns
import math

sns.set()
sns.set_style("whitegrid", {'grid.linestyle': '--'})

inputType = 0
numberOfEquation = 0
numberOfMethod = 0
a, b = 0, 0
epsilon = 0
answerMode = 0
equation = ''
phi = ''
x = Symbol('x')
rootsX = []


def digitsAfterPoint(number):
	if (str(number).find(".") == -1):
		return number
	digitsAfter = 6
	number = str(number).split(".")
	return number[0] + "." + number[1][:digitsAfter]


def firstDiff():
	return diff(equation)


def secondDiff():
	return diff(firstDiff())


def checkInputType():
	global inputType

	print("Вы хотите работать с входными данными через консоль или через файл? 1 - консоль; 2 - файл")
	while (True):
		try:
			inputType = int(input("Консоль или файл: "))
			if (inputType != 1 and inputType != 2):
				raise ValueError
			else:
				break
		except ValueError:
			print("\nВведено неправильное значение, введите 1 для работы через консоль и 2 для работы через файл.\n")


def chooseEquation():
	global equation
	match numberOfEquation:
		case 1:
			equation = x**3 - 2.56 * x**2 - 1.325 * x + 4.395
		case 2:
			equation = 0.5 * x**3 - 2.56 * x**2 - 1.35 * x + 4.30
		case 3:
			equation = x**4 + 4 * x**3 - 22 * x**2 - 100 * x - 75
		case 4:
			equation = sin(x) + 0.1 * x**2
		case 5:
			equation = exp(x) * sin(x)
		case 6:
			equation = x**3 - x + 4


def F(param):
	return equation.subs(x, param)


def checkQuantityOfRoots():
	global rootsX
	
	roots = 0
	epsilon = 0.1
	interval = a
	for i in np.arange(a, b, epsilon):
		if (F(i) * F(i+epsilon) < 0):
			rootsX.append(math.floor(interval))
			rootsX.append(math.ceil(i))
			interval = math.ceil(i)
			roots += 1
	return roots


def printAnswer(table, root):
	if (answerMode == 2):
		file = open("output.txt", "w")
		file.write(str(table) + "\n")
		file.write("x = " + str(root))
		file.close()
		print("Ответ успешно записан в файл output.txt")
	else:
		print(table)
		print("x = ", root)


def getPlot(coordX, isRoot):
	plot_range = []
	if (isRoot == false):
		plot_range = [ii/100 for ii in np.arange((-10)*100, (11)*100)]
	else:
		plot_range = [ii/100 for ii in np.arange((a - 1)*100, (b + 1)*100)]
	y = [equation.subs(x, ii) for ii in plot_range]
	plt.plot(plot_range, y)
	plt.xlabel(r'$x$')
	plt.ylabel(r'$f(x)$')
	plt.title(r'График функции на заданном интервале')
	plt.grid(True)
	if (isRoot):
		plt.scatter(coordX,0)
	plt.show()


def printEquation(number):
	match number:
		case 1:
			print("1: x^3 - 2.56x^2 - 1.325x + 4.395")
		case 2:
			print("2: 0.5x^3 - 2.56x^2 - 1.35x + 4.30")
		case 3:
			print("3: x^4 + 4x^3 - 22x^2 - 100x - 75")
		case 4:
			print("4: sin(x) + 0.1x^2")
		case 5:
			print("5: e^x * sin(x)")
		case 6:
			print("6: x^3 - x + 4")


def printMethod(number):
	match number:
		case 1:
			print("1: метод хорд")
		case 2:
			print("2: метод Ньютона")
		case 3:
			print("3: метод простой итерации")


def getInputDataFromFile():
	global numberOfEquation, numberOfMethod, a, b, epsilon, answerMode

	while (True):
		try:
			fileName = input("Введите имя файла: ")
			file = open(fileName)
			data = file.read().split("\n")
			numberOfEquation = int(data[0])
			numberOfMethod = int(data[1])
			a = float(data[2].split(" ")[0].replace(",", "."))
			b = float(data[2].split(" ")[1].replace(",", "."))
			if (a > b):
				a, b = b, a
			epsilon = float(data[3])
			answerMode = int(data[4])
			chooseEquation()

			print("\nИнформация о входных данных из файла: \n")

			print("Выбрано уравнение", numberOfEquation)
			printEquation(numberOfEquation)
			print("\n")

			print("Выбран метод", numberOfMethod)
			printMethod(numberOfMethod)
			print("\n")

			print("Выбран интервал от ", a, " до ", b)

			roots = checkQuantityOfRoots()
			if (roots > 1 or roots == 0):
				print("\nНа введённом интервале содержится",
					  roots, "корней, завершаю программу\n")
				for i in range(0, len(rootsX), 2):
					print("Корень находится в точке на интервале (", rootsX[i], ";", rootsX[i+1], ")")
				sys.exit(0)

			print("Выбрана погрешность вычисления", epsilon)
			if (answerMode == 1):
				print("Ответ будет выведен в консоль\n")
			else:
				print("Ответ будет сохранён в файл output.txt\n")

			return
		except FileNotFoundError:
			print("Такого файла не существует. Повторите ввод")
		except ValueError:
			print(
				"Ошибка при чтении из файла. Проверьте формат входных данных. Завершаю программу")
			sys.exit(0)


def getInputDataFromConsole():
	global numberOfEquation
	global numberOfMethod
	global a, b
	global epsilon
	global answerMode
	global rootsX

	print("\nДоступные уравнения: ")
	for i in range(6+1):
		printEquation(i)

	while (True):
		try:
			numberOfEquation = int(
				input("Выберите уравнение, корень которого требуется вычислить: "))
			if (numberOfEquation < 1 or numberOfEquation > 6):
				raise ValueError
			else:
				chooseEquation()
				break
		except ValueError:
			print("\nВведено неправильное значение, выберите уравнение от 1 до 6.\n")
   
	getPlot(0, false)
 
	print("\nДоступные методы для решения уравнения:")
	for i in range(3+1):
		printMethod(i)
	while (True):
		try:
			numberOfMethod = int(
				input("Выберите метод для решения уравнения: "))
			if (numberOfMethod < 1 or numberOfMethod > 3):
				raise ValueError
			else:
				break
		except ValueError:
			print("\nВведено неправильное значение, выберите метод от 1 до 3.\n")

	print("\nВведите границы интервала, на котором будем искать корень")

	while (True):
		try:
			a, b = map(float, input("Границы интервала: ").replace(",",".").split(" "))
			if (a > b):
				a, b = b, a
			roots = checkQuantityOfRoots()

			if (a == b):
				print("\nГраницы интервала совпадают, так делать нельзя.\n")
			elif (roots > 1or roots == 0):
				print("\nНа введённом интервале содержится", roots, "корней\n")
				for i in range(0, len(rootsX), 2):
					print("Корень находится в точке на интервале (", rootsX[i], ";", rootsX[i+1], ")")
				rootsX = []
			else:
				break
		except ValueError:
			print("\nНедопустимый формат. Введите интервал через пробел\n")

	print("\nВведите погрешность вычисления")

	while (True):
		try:
			epsilon = float(
				input("Погрешность вычисления: ").replace(",", "."))
			if (epsilon == 0):
				print("\nПогрешность вычисления не может быть равна нулю\n")
			else:
				break
		except ValueError:
			print("\nНедопустимый формат. Введите число\n")

	print("\nКуда вывести ответ? 1 - в консоль; 2 - в файл output.txt")
	while (True):
		try:
			answerMode = int(input("Куда: "))
			if (answerMode > 2 or answerMode < 1):
				print("\nВведите 1 для вывода в консоль или 2 для вывода в файл\n")
			else:
				break
		except ValueError:
			print("\nНедопустимый формат. Введите число\n")


def simpleIterationMethod():
	global phi

	first = firstDiff()
	x_0 = a if (abs(float(first.subs(x, a))) >
				abs(float(first.subs(x, b)))) else b
	lambd = - 1 / first.subs(x, x_0)
	phi = x + lambd * equation
	phiDiffA = abs(diff(phi).subs(x,a))
	phiDiffB = abs(diff(phi).subs(x, b))
	print("phi`(a) = ", phiDiffA)
	print("phi`(b) = ", phiDiffB)
	if (phiDiffA< 1 and phiDiffB < 1):
		print("Достаточное условие сходимости метода простой итерации выполнение");
	else:
		print("Достаточное условие сходимости метода итерации не выполнено.")
	table = [['Iteration', 'x_(i)', 'x_(i+1)', 'phi(x_(i+1))',
			  'F(x_(i+1))', '|x_(i+1) - x_(i)|']]
	table = PrettyTable(table[0])
	counter = 0
	x_1 = 0
	print("Вычисленное начальное приближение x_0 = ", x_0)
	while (True):
		x_1 = phi.subs(x, x_0)
		row = [digitsAfterPoint(counter), digitsAfterPoint(x_0), digitsAfterPoint(x_1), digitsAfterPoint(phi.subs(x, x_1)),
			   digitsAfterPoint(F(x_1)), digitsAfterPoint(abs(x_1 - x_0))]
		table.add_row(row)
		counter += 1
		if (abs(x_0 - x_1) <= epsilon):
			break
		x_0 = x_1
	printAnswer(table, x_1)
	getPlot(x_1, true)


def newtonMethod():
	first = firstDiff()
	second = secondDiff()
	if (first == 0):
		print("Производная равна нулю. Метод Ньютона не работает")
		return
	x_0 = a if (equation.subs(x, a) * second.subs(x, a) > 0) else b
	table = [['Iteration', 'x_n',
			  'F(x_n)', 'F`(x_n)', 'x_(n+1)', '|x_(n+1) - x_(n)|']]
	table = PrettyTable(table[0])
	counter = 0
	x_1 = 0
	print("Вычисленное начальное приближение x_0 = ", x_0)
	while (True):
		x_1 = x_0 - (equation.subs(x, x_0))/(first.subs(x, x_0))
		row = [digitsAfterPoint(counter), digitsAfterPoint(x_0), digitsAfterPoint(F(x_0)), digitsAfterPoint(first.subs(x, x_0)),
			   digitsAfterPoint(x_1), digitsAfterPoint(abs(x_1 - x_0))]
		table.add_row(row)
		counter += 1
		if (abs(x_1 - x_0) <= epsilon and (abs(F(x_0)/(first.subs(x, x_0))) <= epsilon) and (abs(F(x_0)) <= epsilon)):
			break
		x_0 = x_1
	printAnswer(table, x_1)
	getPlot(x_1, true)


def chordMethod():
	table = [['Iteration', 'a', 'b', 'x',
			  'F(a)', 'F(b)', 'F(x)', '|x_(n+1) - x_n|']]
	table = PrettyTable(table[0])
	counter = 0
	a_0 = a
	b_0 = b
	x_0 = a_0
	while (True):
		x_1 = x_0
		x_0 = a_0 - (b_0 - a_0)/(equation.subs(x, b_0) -
								 equation.subs(x, a_0)) * equation.subs(x, a_0)
		row = [digitsAfterPoint(counter), digitsAfterPoint(a_0), digitsAfterPoint(b_0), digitsAfterPoint(x_0),
			   digitsAfterPoint(F(a_0)), digitsAfterPoint(F(b_0)), digitsAfterPoint(F(x_0)), digitsAfterPoint(abs(x_0 - x_1))]
		table.add_row(row)
		if (abs(x_0 - x_1) <= epsilon or abs(F(x_0)) <= epsilon):
			break
		counter += 1
		if (F(a_0) * F(x_0) < 0):
			b_0 = x_0
		else:
			a_0 = x_0
	printAnswer(table, x_0)
	getPlot(x_0, true)


def startComputing():
	match numberOfMethod:
		case 1:
			chordMethod()
		case 2:
			newtonMethod()
		case 3:
			simpleIterationMethod()


checkInputType()
if (inputType == 1):
	getInputDataFromConsole()
	startComputing()
else:
	print("\nПример входных данных из файла можно посмотреть в файле test.txt")
	print("Первая строка - уравнение")
	print("Вторая строка - метод решения")
	print("Третья строка - границы интервала")
	print("Четвёртая строка - погрешность вычисления")
	print("Пятая строка - куда выводить ответ\n")

	getInputDataFromFile()
	startComputing()
