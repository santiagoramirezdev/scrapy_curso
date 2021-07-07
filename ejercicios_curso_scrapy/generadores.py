# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def first_one_houndred_numbers(x):
    x+=2
    yield x

if __name__ == '__main__':
    a = 0 #pivote para ir imprimiendo los pares
    i = 0 #contador de la cantidad de impresiones
    while(i<100):
        a = next(first_one_houndred_numbers(a))
        print(a)
        i+=1