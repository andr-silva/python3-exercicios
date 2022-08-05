# Crie um programa que tenha uma tupla única com nomes de produtos e seus repectivos preços, na sequencia. No final, mostre uma listage, de preços, organizando os dados.py de forma tabular.

itens = ("Lápis", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

border = '-' * 30
f = ('^30','.<21','7.2f')

print(
    f'{border}\n'
    f'{"Listagem de preços":{f[0]}}\n'
    f'{border}'
    )

for item in range(0, len(itens), 2):
    
    product = itens[item]
    price = itens[item+1]

    print(f'{product:{f[1]}}R${price:{f[2]}}')

print(border)
