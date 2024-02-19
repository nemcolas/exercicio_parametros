'''Crie uma função chamada enviar_email que aceite os parâmetros destinatario,
assunto e corpo. O parâmetro assunto deve ter um valor padrão de "Sem assunto".
O parâmetro corpo deve ter um valor padrão de uma string vazia. A função deve
imprimir as informações formatadas. Inclua uma docstring que explique brevemente
o propósito da função.'''

def enviar_email (destinatario, assunto ="Sem Assunto", corpo = "",):
    return f"o destinatãrio é:{destinatario}, o assunto da cartá é: {assunto} e o corpo é {corpo}"

dest = input("Informe o destinatario: ")
assun = input("Informe o assunto da carta: ")
cor = input("Informe o conteúdo da carta: ")

print(enviar_email(dest))




