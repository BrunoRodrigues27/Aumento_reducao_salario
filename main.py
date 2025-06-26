from time import sleep
"""Esse programa serve para controle de aumento e redução de salário."""

"""Essa função exibe o menu e pede uma escolha"""
def menu():
    while True:
        print('|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|')
        print('|                  Controle do Funcionário                  |')
        print('|-----------------------------------------------------------|')
        print('| 1 - Aumento de Salário                                    |')
        print('| 2 - Redução de Salário                                    |')
        print('|-----------------------------------------------------------|')
        try:
            escolha = int(input("| Escolha: "))
            if escolha in [1, 2]:
                print('|-----------------------------------------------------------|')
                return escolha
            else:
                print('| Opção inválida. Por favor, digite 1 ou 2.')
        except ValueError:
            print('| Entrada inválida. Digite apenas números.')
        print('|-----------------------------------------------------------|')


"""Essa função pede o nome do funcionário, e retorna o mesmo"""
def nome_funcionario():
    nome_do_funcionario = str(input("| Nome do funcionário: "))
    sleep(1)
    print('|-----------------------------------------------------------|')
    print('|             informações pessoais do funcionário           |')
    print('|-----------------------------------------------------------|')
    sleep(0.5)
    print(f'| Funcionário: {nome_do_funcionario.strip().title()}')
    print('|-----------------------------------------------------------|')
    sleep(0.5)
    return nome_do_funcionario

def escolha_menu(escolha):
    if escolha == 1:
        print('|-----------------------------------------------------------|')
        print('|                  Menu de aumento salarial                 |')
        print('|-----------------------------------------------------------|')
        sleep(0.5)
        salario_antigo = str(input("| Salário atual: R$"))
        sleep(1)
        salario_antigo_float = float(salario_antigo.replace('.', '').replace(',', '.'))
        por_aumento_num = str(input("| Porcentagem do aumento: "))
        sleep(1)
        por_aumento_num_float = float(por_aumento_num.replace('.', '').replace(',', '.'))
        print('|-----------------------------------------------------------|')
        valor_aumento = por_aumento_num_float / 100 * salario_antigo_float
        valor_aumento_formatado = 'R${:,.2f}'.format(valor_aumento).replace(',', 'v',).replace('.', ',').replace('v', '.')
        novo_salario = salario_antigo_float + valor_aumento
        novo_salario_formatado = 'R${:,.2f}'.format(novo_salario).replace(',', 'v').replace('.', ',').replace('v', '.')
        sleep(0.5)
        print('|-----------------------------------------------------------|')
        print('|                    Detalhes pós aumento                   |')
        print('|-----------------------------------------------------------|')
        print(f'| Porcentagem do aumento: {por_aumento_num}%\n'
              f'| Valor do aumento: {valor_aumento_formatado}\n'
              f'| Salário atualizado {novo_salario_formatado}')
        print('|___________________________________________________________|')
    elif escolha == 2:
        sleep(0.5)
        print('|-----------------------------------------------------------|')
        print('|                  Menu de redução salarial                 |')
        print('|-----------------------------------------------------------|')
        sleep(0.5)
        salario_antigo = str(input("| Salário atual: R$"))
        sleep(1)
        salario_antigo_float = float(salario_antigo.replace('.', '').replace(',', '.'))
        por_reducao_num = str(input("| Porcentagem da redução: "))
        sleep(1)
        por_reducao_num_float = float(por_reducao_num.replace('.', '').replace(',', '.'))
        print('|-----------------------------------------------------------|')
        valor_reducao = por_reducao_num_float / 100 * salario_antigo_float
        valor_reducao_formatado = 'R${:,.2f}'.format(valor_reducao).replace(',', 'v', ).replace('.', ',').replace('v','.')
        novo_salario = salario_antigo_float - valor_reducao
        novo_salario_formatado = 'R${:,.2f}'.format(novo_salario).replace(',', 'v').replace('.', ',').replace('v', '.')
        sleep(0.5)
        print('|-----------------------------------------------------------|')
        print('|                   Detalhes pós redução                    |')
        print('|-----------------------------------------------------------|')
        sleep(0.5)
        print(f'| Porcentagem da redução: {por_reducao_num}%\n'
              f'| Valor da redução: R${valor_reducao_formatado}\n'
              f'| Salário atualizado: R${novo_salario_formatado}')
        print('|____________________________________________________________|')
    else:
        print('| Escolha inválida!')
        print('|------------------------------------------------------------|')



if __name__ == '__main__':
    menu_opc = menu()
    info = nome_funcionario()
    escolha_menu(menu_opc)
    


