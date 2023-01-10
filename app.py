###1 escrever uma string:
'''
nome = input("fala teu nome")
print(f"salve {nome}!")
'''

###2 pegar um numero transformar em inteiro e dps somar 
'''
idade = int(input("Digite sua idade: ")) #definir a variavel como inteira e nao string
print(idade + 10)
'''
##conversoes:
# bool()
# int()
# float()
# str()


###3 operações matematicas
'''
nota1 = float(input("Digite sua primeira nota"))
nota2 = float(input("Digita sua segunda nota"))
media = (nota1 + nota2)/2
print(f"Sua media é {media}")
'''
##print(f"Sua media é {(nota1 + nota2)/2}")



###4 operadores relacionais ( == > < >= <= )
#teste = 10 > 5
#print(teste)

###5 operadores logicos
# and(os dois iguais retorna true)
# or(um dos dois true retorna true)
# not(invete oq vem dps do not EX: not true = false)

#teste = 5 == 5 and 6 > 10
#print(teste)

##teste com IF usando operadores*(bem simples)

#nota_aluno = int(input('Digite a nota: '))
#nota_minima_recuperacao = 4
#media_escola = 6

#teste = nota_aluno >=4 and nota_aluno < media_escola

#if teste == True:
    #print("recuperacao")


###6 if elif else
## exemplo sistema de notas
'''
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2)/ 2

if media >= 6:
    print("Aprovado")

elif media >= 4:
    print("recuperacao")

else:
    print("reprovado")
'''

###7 estruturas de repeticao
## while: enquanto uma condicao for true
## for: usado quando sabe quantas vezes o laço vai ser executado
#!sintaxe: for (comeco, fim, setep)
'''
i = 0 
while i <= 10:
    print(i)
    i= i + 1 #i +=1
'''

'''
for i in range(1, 11):
    if i % 2 == 0:
        print(f'o numero {i} e par')
    else:
        print(f'o numero {i} nao e par')
'''

##tabuada especifica
'''
for i in range(1, 11):
    print(f"5 X {i} = {i*5}")
'''

###8 Listas
##notas_alunos = [10, 7, 5, 2]
         #posicao: 0  1  2  3
#print(notas_alunos[1]) 

##media de uma turma
'''
qtd_alunos = int(input('Digite o numero de alunos: '))
notas_alunos = []

for i in range(0, qtd_alunos): 
    nota = int(input('Digite a nota: '))
    notas_alunos.append(nota)

soma= 0
quantidade_notas = 0 
for i in notas_alunos:
    soma = soma + i
    quantidade_notas = quantidade_notas + 1

media = soma / quantidade_notas
print(media)
'''

###9 dicionarios
#!sintaxe: var = { 'key': 'value' }

#pessoas =  {'nome': 'dan', 'idade' : '17 anos'}
#print(pessoas['nome'])

'''
pessoas =  {'nome': input("Digite seu nome"), 'idade' : '17 anos'}
print(pessoas['nome'])
'''

###10 funções
'''
def soma_numeros():
    n1 = int(input("Digite um numero"))
    n2 = int(input("Digite um numero"))
    soma = n1 + n2
    print(soma)

soma_numeros()
'''
