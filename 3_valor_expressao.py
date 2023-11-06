#Calcula o resultado da expressão:
#H =1 + 1/2 + 1/3 + 1/4 + ... + 1/n
def f_valor_h(n):
    #Define a variável 'h'
    h = 0.0
    #Repete o cálculo n vezes
    for x in range(1, n+1):
        h += 1/x
    print(f'{h:.4f}')


def main():

    #Entrada de Dados
    n = int(input())

    #Saída de Dados
    f_valor_h(n)


if __name__ == '__main__':
    main()
