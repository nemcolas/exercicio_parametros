'''Crie uma função chamada comprar_produto que aceite dois parâmetros nomeados:
produto e quantidade. O parâmetro produto deve ter um valor padrão de "produto
desconhecido" e o parâmetro quantidade deve ter um valor padrão de 1. A função
deve retornar uma mensagem indicando a compra do produto na quantidade
especificada.'''

def comprar_produto(produto = "Produto desconhecido", quantidade: int=1):
    return f"você comprou {quantidade} de {produto}"

print(comprar_produto())
