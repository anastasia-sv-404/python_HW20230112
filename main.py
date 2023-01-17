import numpy
import matplotlib.pyplot as plt

limit = 25
step = 0.01
increase_high = True
color = 'r'
line_style = '-.'

x_change = {-limit: 'inc'}
x = numpy.arange(-limit, limit, step)

a, b, c, d, e = -12, -18, 5, 10, -30


def f(x):
    function = a * x ** 4 * numpy.sin(numpy.cos(x)) + b * x ** 3 + c * x ** 2 + d * x + e
    return function


def switch_color():
    global color
    if color == 'r':
        color = 'b'
    else:
        color = 'r'
    return color


def switch_line():
    global line_style
    if line_style == '-':
        line_style = '-.'
    else:
        line_style = '-'
    return line_style


# Вычисление вершины (экстремумы)

# Вычисление точки минимума на заданном интервале и значение ф-ии в ней
x_min = -limit
y_min = f(x_min)

for x_curr in x:
    if f(x_curr) < y_min:
        x_min = numpy.round(x_curr, 2)
        y_min = numpy.round(f(x_curr), 2)

print(f'Координаты точки минимума ф-ии на заданном отрезке: [{x_min}, {y_min}]')

# Вычисление точки максимума на заданном интервале и значение ф-ии в ней
x_max = -limit
y_max = f(x_max)

for x_curr in x:
    if f(x_curr) > y_max:
        x_max = numpy.round(x_curr, 2)
        y_max = numpy.round(f(x_curr), 2)

print(f'Координаты точки максимума ф-ии на заданном отрезке: [{x_max}, {y_max}]')

for i in range(len(x) - 1):
    if (f(x[i]) > 0 and f(x[i + 1]) < 0) or (f(x[i]) < 0 and f(x[i + 1] > 0)):
        x_change[x[i]] = 'zero'
    if increase_high:
        if f(x[i]) > f(x[i + 1]):
            increase_high = False
            x_change[x[i]] = 'inc'
    else:
        if f(x[i]) < f(x[i + 1]):
            increase_high = True
            x_change[x[i]] = 'inc'

x_change[limit] = 'inc'

x_keys = [x for x in x_change]

x_keys.sort()
print(x_keys)

for i in range(len(x_keys) - 1):
    x_cur = numpy.arange(x_keys[i], x_keys[i + 1] + step, step)
    if x_change.get(x_keys[i]) == 'zero':
        switch_line()
    else:
        switch_color()
    plt.rcParams['lines.linestyle'] = line_style
    plt.plot(x_cur, f(x_cur), color)

plt.show()
