from cgitb import text


meses= ['jane', 'fev', 'marc', 'abril', 'maio', 'jun', 'julh', 'ago', 'set', 'nov', 'dez']
print("escreve uma data no seguinte formato com as / na seguinte forma : xx/xx/xx")
data = input('Data a ser verificado: ')

def verificandoData(data):
    data.strip()
    texto = data.split("/")
    dia = int(texto[0])
    mes = int(texto[1])
    ano = len(texto[2])

    #Verificando se a data é valida
    if dia > 30 and texto < 0:
        print("dataInvalida")
    elif mes > 12 and text <= 0:
        print("dataInvalida")
    elif ano == 3 and texto == 1:
        print("dataInvalida")
    
    print(f'Data Válida, {dia} de {meses[mes-1]}, de {ano}')

verificandoData(data)