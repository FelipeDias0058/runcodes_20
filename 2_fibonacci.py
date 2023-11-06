#Mostra a sequência de números usando a
#progressão de Fibonacci:
def f_fibonacci(n):

    #Levanta um ValueError se o número não for positivo.
    if not (isinstance(n, int) and n >= 0):
        raise ValueError(f'Digite um valor inteiro positivo.')

    #Define os primeiros números da sequência
    if n in {0, 1}:
        return n

    #Calcula o próximo número da sequência
    n_anterior, n_atual = 0, 1
    for x in range(2, n + 1): 
        n_anterior, n_atual = n_atual, n_atual + n_anterior

    return n_atual
            

def main():
    #Entrada de Dados
    numero = int(input())
    sequencia = [f_fibonacci(numero) for numero in range(numero)]

    #Saída de Dados
    print(str(sequencia)[1:-1])


if __name__ == '__main__':
    main()
