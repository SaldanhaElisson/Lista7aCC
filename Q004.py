from cgitb import text


meses= ['jane', 'fev', 'marc', 'abril', 'maio', 'jun', 'julh', 'ago', 'set', 'out', 'nov', 'dez']
print("escreve uma data no seguinte formato com as / na seguinte forma : xx/xx/xx")
data = input('Data a ser verificado: ')

def verificandoData(data):
    data.strip()
    texto = data.split("/")
    dia = int(texto[0])
    mes = ((int(texto[1])) - 2)
    ano = len(texto[2])
    anoNumero = texto[2]

    #Verificando se a data é valida
    if dia > 30 and texto < 0:
        print("dataInvalida")
        return
    elif mes > 12 and text <= 0:
        print("dataInvalida")
        return
    elif ano == 3 and texto == 1:
        print("dataInvalida")
        return
    
    print(f'Data Válida, {dia} de {meses[mes]}, de {anoNumero}')

verificandoData(data)