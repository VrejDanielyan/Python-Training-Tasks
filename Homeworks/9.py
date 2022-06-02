'''Implement function to return Ամենափոքր ընդհանուր բազմապատիկ'''

a = -2
b = 6

def amena(a, b):
    for i in range(1,10):
        tiv = a * i
        if tiv % b == 0:
            return tiv

print(amena(a, b))