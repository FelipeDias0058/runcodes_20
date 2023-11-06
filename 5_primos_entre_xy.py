#Determina se um número é primo ou não;
#imprime na tela caso seja
def f_primo(x, y):
    for n in range(x, y + 1):
        if n > 1:
            for i in range(2, int(n**0.5) + 1):
                if (n % i) == 0: break
            else:
               print(n)

    
def main():

    #Entrada de Dados
    x = int(input())
    y = int(input())

    #Saída de Dados
    f_primo(x, y)
    

if __name__ == '__main__':
    main()
