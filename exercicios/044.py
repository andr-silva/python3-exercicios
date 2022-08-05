# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:

payment = float(input('Qual o valor: R$'))

card_rate_1x = payment * 1.05
card_rate_2x = payment * 1.1
card_rate_3x = payment * 1.15
card_rate_xx = payment * 1.2
tax_in_cash = payment * 0.95
debit_rate = payment * 1.025
pix_rate = payment
installments = ''
form_of_payment = 'Não informado' 
rate = 0

selected = int(input(
    f'Valor de R${payment}\n'
    'Formas de pagamento:\n'
    '[1] À vista  [2] Pix [3] Débito [4] Crédito\n'
    'Selecione uma opção: ')
)
if selected == 1:
    form_of_payment = 'À vista'
    rate = tax_in_cash

elif selected == 2:
    form_of_payment = 'Pix'
    rate =  pix_rate

elif selected == 3:
    form_of_payment = 'Débito'
    rate =  debit_rate

elif selected == 4:
    selected_credit = int(input(
        'Quantas vezes? \n'
        f'[1] 1x R${card_rate_1x:.2f} [2] 2x R${card_rate_2x:.2f} [3] 3x R${card_rate_3x:.2f}\n'
        'Selecione uma opção: ')
    )
    form_of_payment = 'Crédito'

    if selected_credit == 1:
        rate =  card_rate_1x
        
    elif selected_credit == 2:
        rate =  card_rate_2x

    elif selected_credit == 3:
        rate =  card_rate_3x
    else:
        print('opção invalida! Tente novamente!')
        
    installments = f'\n{selected_credit}x de R${rate / selected_credit:.2f}'
else:
    print('opção invalida! Tente novamente!')
    
print(f'Forma de pagamento {form_of_payment}: R$ {rate:.2f} {installments}')
