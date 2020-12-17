######################################################################

             # Nome: Walter Melo ## Data: 16/12/2020

#######################################################################

import random

turmaA = []
turmaB = []
c = 0
d = 0

def media(x=list()):
    valor = 0
    for nota in x:
        valor += nota
    if len(x)!=0:
        unidades = len(x)
    else:
        unidades = 1
    resultado = valor/unidades
    return resultado

def selecionar(x=list()):
    valor = []
    for d in x:
        if d > 5:
            valor.append(d)
    aprovado = valor
    return aprovado

while True:
    notas = random.uniform(0.0,10.0)
    x= round(notas,1)
    turmaA.append(x)
    c+=1
    if c ==10:
        break
while True:
    nota = random.uniform(0.0,10.0)
    y= round(nota,1)
    turmaB.append(y)
    d+=1
    if d ==10:
        break    

mediaA=round(media(turmaA),1)
mediaB=round(media(turmaB),1)
alunoAp = selecionar(turmaA) + selecionar(turmaB)
aprovadosA = selecionar(turmaA)
aprovadosB = selecionar(turmaB)
AlunosAprovadosB = len(aprovadosB)
AlunosAprovadosA = len(aprovadosA)


print(f'A media da turma A {mediaA}')
print(f'A media da turma B {mediaB}')
print(f'O numero de aprovados na turma A foi {AlunosAprovadosA} e o numero de aprovados na turma B foi {AlunosAprovadosB}')
print(f'As notas dos aprovados em ambas as turmas são{alunoAp}')

