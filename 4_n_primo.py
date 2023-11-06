#Determina se o número é primo, retornando 'True' ou 'False'
def f_primo(n):
    eh_primo = 0
    if n > 1:
        for x in range(2, n):
            if (n % x == 0):
                return False
                eh_primo = 1
                break
        if eh_primo == 0:
            return True
            

def main():
    #Entrada de Dados
    numero = int(input())
    primo = f_primo(numero)

    #Saída de Dados
    print(primo)


if __name__ == '__main__':
    main()
