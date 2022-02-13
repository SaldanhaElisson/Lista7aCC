print('Calculo do IMC')
print()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua Altura: '))
print()
def IMC(peso, altura):
    valor = peso/ (altura * altura)
    print(f'IMC {valor:,.2f}')
    if valor < 18.5:
        print('Classificação: MAGREZA')
        print('Graude de Obesidade: 0')
    elif valor >= 18.5 and valor <= 24.9:
        print('Classificação: NORMAL')
        print('Graude de Obesidade: 0')
    elif valor >= 25.0 and valor <= 29.9:
        print('Classificação: SOBREPESO')
        print('Graude de Obesidade: 1')
    elif valor >= 30 and valor <= 39.9:
        print('Classificação: OBESIDADE')
        print('Graude de Obesidade: 2')
    elif valor > 40:
        print('Classificação: OBESIDADE GRAVE')
        print('Graude de Obesidade: 3')
    else:
        print('INVALIDO')

IMC(peso, altura)