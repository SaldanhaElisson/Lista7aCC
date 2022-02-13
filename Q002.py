mediaFinal = float(input('Digite a Media final do Aluno: '))

def conceitoDoAluno(mediaFinal):
    if mediaFinal >= 0.0 and mediaFinal<= 4.9:
        print('O conceito do seu aluno foi D')
    elif mediaFinal >= 5.0 and mediaFinal <= 6.9:
        print('O conceito do seu aluno foi C')
    elif mediaFinal >= 7.00 and mediaFinal <= 8.9:
        print('O conceito do seu aluno foi B')
    elif mediaFinal >= 9.00 and mediaFinal <= 10.00:
        print('O conceito do seu aluno foi A')
    else:
        print('Invalido')

conceitoDoAluno(mediaFinal)