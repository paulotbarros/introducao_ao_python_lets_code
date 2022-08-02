# > ESTRUTURAS CONDICIONAIS

idade = 18

if idade >= 18:
    print('Você é maior de idade!')
else:
    print('Você é menor de idade!')

"""
    Imagine  que você imprimir "Aprovada(o)", caso o estudante tenha uma média superior
    ou igual a 7, e "Reprovado", caso a média seja inferior a 7.
"""

"""media = float(input('Informe a média do estudante: '))

    if media >= 7:
        print('Você foi Aprovada(o).')
    elif media >= 5 :
        print('Você esta de Recuperação.')
    else:
        print('Você foi Reprovada(o).')"""

media = 5
presenca = 50

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else :
    print('Reprovado')