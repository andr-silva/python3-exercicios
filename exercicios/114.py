# Crie um código em puthon que teste se o site Pudim está acessivel pelo computador usado.

import requests

try:
    site = requests.get('https://google.com.br')
except:
    print('A URL informada não está acessível!\n'
        'Verifique os dados informados.'
    )
else:
    print('A URL informada está acessível!')
