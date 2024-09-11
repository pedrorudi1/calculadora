def menu():
    menu = '''
    MENU
    Digite uma das opções abaixo:
    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão (números inteiros)
    5 - Divisão (números reais)
    6 - Sair

    Opção: '''
    return input(menu)
    
    
def soma(input1, input2, solution):
    solution = input1 + input2
    return solution


def subtracao(input1, input2, solution):
    solution = input1 - input2
    return solution


def multiplicacao(input1, input2, solution):
    solution = input1 * input2
    return solution


def divisao_inteiros(input1, input2, solution, resto):
    solution = input1 // input2
    resto = input1 % input2
    return solution, resto


def divisao(input1, input2, solution):
    solution = input1 / input2
    return solution


def main():
    input1 = 0
    input2 = 0
    solution = 0
    resto = 0

    while True:

        opcao = menu()

        if opcao == "1":
            input1 = float(input('Digite o primeiro número da operação: '))
            input2 = float(input('Digite o segundo número da equação: '))
            solution = soma(input1, input2, solution)
            print(f'O resultado da soma é: {solution}')

        elif opcao == "2":
            input1 = float(input('Digite o primeiro número da operação: '))
            input2 = float(input('Digite o segundo número da equação: '))
            solution = subtracao(input1, input2, solution)
            print(f'O resultado da subtração é: {solution}')

        elif opcao == "3":
            input1 = float(input('Digite o primeiro número da operação: '))
            input2 = float(input('Digite o segundo número da equação: '))
            solution = multiplicacao(input1, input2, solution)
            print(f'O resultado da multiplicação é: {solution}')

        elif opcao == "4":
            input1 = int(input('Digite o primeiro número da operação: '))
            input2 = int(input('Digite o segundo número da equação: '))
            solution, resto = divisao_inteiros(input1, input2, solution, resto)
            print(f'O resultado da divisão é: {solution}. O resto da operação é: {resto}.')

        elif opcao == "5":
            input1 = float(input('Digite o primeiro número da operação: '))
            input2 = float(input('Digite o segundo número da equação: '))
            solution = divisao(input1, input2, solution)
            print(f'O resultado da divisão é: {solution}')

        elif opcao == "6":
            break

        else:
            print(f'Opção digitada é inválida.')

main()