"""
2. Realizar un programa que imprima en pantalla cien veces la suma de
los cuadrados de los números pares entre el 50 y 100.
"""


def print_squares():
    sum = 0
    for value in range(1, 101):
        if value >= 50 and value <= 100 and value % 2 == 0:
            sum += value ** 2
    print_100(sum)


def print_100(value):
    print('*' * 25)
    for _ in range(1, 101):
        print(f"{_}: valor: [{value}]")


print_squares()
