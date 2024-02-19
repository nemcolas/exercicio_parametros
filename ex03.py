'''Defina uma função chamada soma que aceite dois parâmetros numéricos (a e b) e
retorne a soma desses números. Utilize anotações de tipos para indicar que os
parâmetros e o retorno são do tipo float.'''

def soma(a: float=0, b: float=0):
    return a + b

numero1 = float(input("Informe o primeiro número: "))
numero2 = float(input("Informe o segundo número: "))

print(soma(a=numero1, b=numero2))



