# Faça um nmini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. quando o usuário digitar a palavra "FIM", o programa se encerrará.

def help_python():

    while True:

        print(
            'SISTEMA DE AJUDA PYHELP'
            'Consulte o manual de funções e bibliotecas.\n'
            'Após entrar no manual use "Q" para sair do sistema de visualização.\n'
            'Para finalizar o programa basta digitar "sair".\n'
        )

        comando = input('Função ou Biblioteca > ').lower()

        if comando == 'sair':
            print('Finalizado!')
            break
        else:
            print(f"Acessando o manual do comando '{comando}'")
            help(comando)


help_python()
