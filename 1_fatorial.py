#Calcula o fatorial do número digitado
def f_fatorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


def main():
    #Entrada de Dados
    numero = int(input())
    fatorial = f_fatorial(numero)

    #Saída de Dados
    print(fatorial)


if __name__ == '__main__':
    main()
