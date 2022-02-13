print('Digite [+] para somar')
print('Digite [-] para diminuir')
print('Digite [/] para dividir')
print('Digite [*] para mutiplicar')

primeiroNumero = int(input('Digite o primeiro numero: '))
segundoNumero = int(input('Digite o segundo numero: '))
simboloOperation = input('Digite a operação: ')


def operation(n1, n2, simbolo):
    operations = [["+", n1+n2], ["-", n1-n2],["/", n1/n2], ["*", n1*n2]]
    aux = len(operations)
    simbolo.strip()

    ## fazendo a operaçãp
    for s in range(0,  aux):
        if simbolo == operations[s][0]:
            resultado = operations[s][1]
            print(f"o Resulta da operação {primeiroNumero} {simbolo} {segundoNumero} = {resultado}")
            return
    print('Operação invalida')

operation(primeiroNumero, segundoNumero,  simboloOperation)