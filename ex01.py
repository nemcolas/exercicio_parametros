'''Escreva uma função chamada mostrar_informacoes que aceite três parâmetros 
nomeados: nome, idade e cidade. A função deve imprimir uma mensagem 
formatada com essas informações.'''

def mostrar_informacoes(nome, idade, cidade):
    print(f"Seu nome é {nome}, sua idade é {idade} e sua cidade é {cidade}")


sua_cidade = input("Informe a cidade: ")
sua_idade = input ("Informe sua idade: ")
seu_nome = input ("Informe seu nome: ")

mostrar_informacoes(nome=seu_nome, idade=sua_idade, cidade=sua_cidade)