'''Crie uma função chamada calcular_area_retangulo que aceite dois parâmetros:
base e altura, ambos com valores padrão iguais a 1. A função deve retornar a área
do retângulo'''


def calcular_area_retangulo(base: int = 1, altura: int = 1):
    return base * altura


base_retangulo = int(input("Informe á base do retangulo: "))
altura_retangulo = int(input("Informe a altura do retangulo: "))

print(calcular_area_retangulo(base=base_retangulo, altura=altura_retangulo))
