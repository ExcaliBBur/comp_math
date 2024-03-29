# Лабораторная работа №1

<a href = "https://github.com/ExcaliBBur/comp_math/tree/main/lab1">Репозиторий</a>

«Решение системы линейных алгебраических уравнений СЛАУ методом Гаусса с выбором главного элемента по столбцам»

1. В программе численный метод должен быть реализован в виде отдель-ной подпрограммы/метода/класса, в который исходные/выходные дан-ные передаются в качестве параметров. 
2. Размерность матрицы n<=20 (задается из файла или с клавиатуры - по выбору конечного пользователя). 
3. Должна быть реализована возможность ввода коэффициентов матрицы, как с клавиатуры, так и из файла (по выбору конечного пользователя).

Для прямых методов должно быть реализовано:
* Вычисление определителя 
* Вывод треугольной матрицы (включая преобразованный столбец В) 
* Вывод вектора неизвестных: 𝑥1,𝑥2,…,𝑥𝑛 
* Вывод вектора невязок: 𝑟1,𝑟,…,𝑟𝑛

# Лабораторная работа №2

<a href = "https://github.com/ExcaliBBur/comp_math/tree/main/lab2">Репозиторий</a>

«Численное решение нелинейных уравнений и систем»

Вычислительная часть: 
  1. Метод половинного деления 
  2. Метод секущих 
  3. Метод простой итерации.
  
Программная часть: <br/>
 1. Методы для нелинейных уравнений
 * Метод хорд 
 * Метод Ньютона
 * Метод простой итерации
 2. Метод для системы нелинейных уравнений: 
 * Метод Ньютона

<b>Цель работы: изучить численные методы решения нелинейных уравнений и их си-стем, 
найти корни заданного нелинейного уравнения/системы нелинейных уравнений, вы-полнить программную реализацию методов. </b>
<br/>
<b>Лабораторная работа состоит из двух частей: вычислительной и программной. </b>
<b>Вычислительная реализация задачи: </b>
1. Отделить корни заданного нелинейного уравнения графически (вид уравнения представлен в табл. 6)
2. Определить интервалы изоляции корней.
3. Уточнить корни нелинейного уравнения (см. табл. 6) с точностью ε=10-2.
4. Используемые методы для уточнения каждого из 3-х корней многочлена пред-ставлены в таблице 7.
5. Вычисления оформить в виде таблиц (1-5), в зависимости от заданного метода. Для всех значений в таблице удержать 3 знака после запятой. <br/>
a. Для метода половинного деления заполнить таблицу 1. <br/>
b. Для метода секущих заполнить таблицу 4.<br/>
c. Для метода простой итерации заполнить таблицу 5.<br/>
6. Заполненные таблицы отобразить в отчете.

<b> Программная реализация задачи </b>

<i>Для нелинейных уравнений: </i>
1. Все численные методы должны быть реализованы в виде отдельных подпрограмм/методов/классов. 
2. Пользователь выбирает уравнение, корень/корни которого требуется вычислить (3-5 функций, в том числе и трансцендентные), из тех, которые предлагает программа. 
3. Предусмотреть ввод исходных данных (границы интервала/начальное приближение к корню и погрешность вычисления) из файла или с клавиатуры по выбору конечного пользователя. 
4. Выполнить верификацию исходных данных. 
Необходимо анализировать наличие корня на введенном интервале. Если на интервале несколько корней или они отсутствуют – 
выдавать соответствующее сообщение. Программа должна реагировать на некорректные введенные данные. 
5. Для методов, требующих начальное приближение к корню (методы Ньютона, секущих, хорд с фиксированным концом), выбор начального приближения
(а или b) вычислять в программе. 
6. Для метода простой итерации проверять достаточное условие сходимости ме-тода на введенном интервале. 
7. Предусмотреть вывод результатов (найденный корень уравнения, значение функции в корне, число итераций) в файл или на экран по выбору конечного пользователя. 
8. Организовать вывод графика функции, график должен полностью отображать весь исследуемый интервал (с запасом).

<i>Для систем нелинейных уравнений: </i>
1. Пользователь выбирает предлагаемые программой системы двух нелинейных уравнений (2-3 системы). 
2. Организовать вывод графика функций. 
3. Начальные приближения ввести с клавиатуры. 
4. Для метода простой итерации проверить достаточное условие сходимости. 
5. Организовать вывод вектора неизвестных: 𝑥1,𝑥2. 
6. Организовать вывод количества итераций, за которое было найдено решение. 
7. Организовать вывод вектора погрешностей: |𝑥𝑖(𝑘)−𝑥𝑖(𝑘−1)|
8. Проверить правильность решения системы нелинейных уравнений.

