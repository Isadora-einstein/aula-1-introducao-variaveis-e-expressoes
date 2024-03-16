"""
#### Exercício 2

Receba 2 inputs do usuário: O preço de um produto em reais e uma porcentagem de desconto a ser aplicada sobre ele (entre 0 e 100). Devolva o preço final do produto.

Exemplo:

Digite o preço do produtos em reais: 10.5

Digite o desconto a ser aplicado (em porcentagem): 50


Resposta:

O preço final do produto é 5.25
"""
preco_do_produto = float (input("digite o preço do produto"))
desconto = float (input ("digite o desconto(entre 0 e 100)"))
valor_de_desconto = preco_do_desconto *(desconto/100)
valor_final = preco_do_produto - valor_do_desconto print (f"O preço final do produto é {valor_final}")
