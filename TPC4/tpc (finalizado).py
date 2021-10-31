# -*- coding: utf-8 -*-
import random


def criarFracao (numerador, denominador):
    return (numerador, denominador)



def verFracao (f):
    return str(f[0])+ '/' + str(f[1])
    

    
def mdc(num,denom):
    if num < denom:
        return mdc(denom,num)
    elif num % denom == 0:
        return denom
    else:
        return mdc(num,num%denom)  



def simplificarFracao(f):
    num,denom = f
    a = mdc (num, denom)
    return (num/a, denom/a)



def somarFracao(f1,f2):
    ((n1,d1))=f1
    ((n2,d2))=f2
    return criarFracao(n1*d2+n2*d1,d1*d2)



def subtrairFracao(f1,f2):
    ((n1,d1)) = f1
    ((n2,d2)) = f2
    return criarFracao(n1*d2-n2*d1,d1*d2)


def multiplicarFracao (f1,f2):
    n1,d1 = f1
    n2,d2 = f2
    return criarFracao(n1*n2,d1*d2)


def dividirFracao(f1,f2):
    
    n1,d1 = f1
    n2,d2 = f2
    return simplificarFracao(criarFracao(n1*d2,d1*n2))


def gerarListaFrac():
    
    n=int(input("Quantas frações queres na tua lista? "))
    L=[]
    for i in range(n):
        num=(random.randint(1,100))
        denom=(random.randint(1,100))
        f = criarFracao(num,denom)
        L.append(f)
    return L


def somarFracLista(L):
    soma=(0,1)
    print('Vais somar todas as frações da lista: '+str(L) + 'que geraste aleatoriamente')
    for elem in L:
        soma = somarFracao(soma,elem)
    print ('A soma de todas as frações é: ' + str(verFracao(simplificarFracao(soma))))
        
        
def maiorFracLista(L):
    max = L[0]
    for i in range (1,len(L)):
        n1,d1 = max
        n2,d2 = L[i]
        if (n1*d2)<(n2*d1):
            max=L[i]
    print('A maior fração da lista é: ' ,max)


def menorFracLista(L):
    min = L[0]
    for i in range (1,len(L)):
        n1,d1 = min
        n2,d2 = L[i]
        if (n1*d2)>(n2*d1):
            min=L[i]
    print('A menor fração da lista é: ' , min)
    
            
        
        
def menu ():
    print ("""
                Bem-vindo ao mundo das Frações! Faz o que te vai na alma!
                
                (1) Criar Fração
                
                (2) Simplificar Fração
                
                (3) Somar Frações
                
                (4) Subtrair Frações
                
                (5) Multiplicar Frações
                
                (6) Dividir Funções
                
                (7) Gerar lista com n frações
                
                (8) Somar as frações da lista
                
                (9) Saber a MAIOR fração da lista
                
                (10) Saber a MENOR fração da lista
                
                (0) SAIR
                
                """)
                


opcao=1              
while opcao !=0: 
    menu()
    opcao=int(input('O que desejas fazer: '))
            
    if opcao == 1:
        print ('----------CRIAR FRAÇÃO---------')
        n1=int(input('Numerador: '))
        d1=int(input('Denominador: '))
        f1 = criarFracao (n1 ,d1)
        print ('Fração: ', verFracao(f1)) 
        
        
        
    elif opcao == 2:
        print('---------SIMPLIFICAR----------')
        n1=int(input('Numerador: '))
        d1=int(input('Denominador: '))
        f2 = criarFracao (n1 ,d1)
        print('Fração: ', verFracao(f2))
        print('Fração Simplificada: ', verFracao(simplificarFracao(f2)))
        
        
    elif opcao == 3:
        print('----------SOMAR----------')
        n1 = int(input('Numerador da primeira fração: '))
        d1 = int(input('Denominador da primeira fração: '))
        f3 = criarFracao(n1,d1)
        print ('Fração 1: ', verFracao(f3))
        n2 = int(input('Numerador da segunda fração: '))
        d2 = int(input('Denominador da segunda fração: '))
        f4=criarFracao(n2,d2)
        print('Fração 2: ', verFracao(f4))
        t = somarFracao(f3,f4)
        print('Soma das Fracções: ', verFracao(simplificarFracao(t)))
        
        
        
    elif opcao == 4:
        print ('----------SUBTRAIR----------')
        n1 = int(input('Numerador da primeira fração: '))
        d1 = int(input('Denominador da primeira fração: '))
        f3 = criarFracao(n1,d1)
        print ('Fração 1: ', verFracao(f3))
        n2 = int(input('Numerador da segunda fração: '))
        d2 = int(input('Denominador da segunda fração: '))
        f4=criarFracao(n2,d2)
        print('Fração 2: ', verFracao(f4))
        t = subtrairFracao(f3,f4)
        print('Subtração das Fracções: ', verFracao(simplificarFracao(t)))
        
        
        
    elif opcao == 5:
        print ('----------MULTIPLICAR----------')
        n1 = int(input('Numerador da primeira fração: '))
        d1 = int(input('Denominador da primeira fração: '))
        f3 = criarFracao(n1,d1)
        print ('Fração 1: ', verFracao(f3))
        n2 = int(input('Numerador da segunda fração: '))
        d2 = int(input('Denominador da segunda fração: '))
        f4=criarFracao(n2,d2)
        print('Fração 2: ', verFracao(f4))
        t = multiplicarFracao(f3,f4)
        print('Fração Mutiplicada: ', verFracao(simplificarFracao(t)))
        
        
        
    elif opcao == 6:
        print ('----------DIVIDIR----------')
        n1 = int(input('Numerador da primeira fração: '))
        d1 = int(input('Denominador da primeira fração: '))
        f3 = criarFracao (n1,d1)
        print ('Fração 1: ', verFracao(f3))
        n2 = int(input('Numerador da segunda fração: '))
        d2 = int(input('Denominador da segunda fração: '))
        f4 = criarFracao(n2,d2)
        print('Fração 2: ', verFracao(f4))
        t = dividirFracao(f3,f4)
        print('Fração Dividida: ', verFracao(simplificarFracao(t)))
        
        
        
    elif opcao == 7:
        print ('----------GERAR LISTA COM FRAÇÕES----------')
        print(gerarListaFrac())
        
        
        
    elif opcao == 8:
        print ('----------SOMAR AS FRAÇÕES DE UMA LISTA----------')
        somarFracLista(gerarListaFrac())
        
        
        
    elif opcao == 9:
        print ('----------SABER A MAIOR FRAÇÃO DE UMA LISTA----------')
        l = gerarListaFrac()
        print('Lista: ', l)
        maiorFracLista(l)
        
    
    
    elif opcao == 10:
        print ('----------SABER A MENOR FRAÇÃO DE UMA LISTA----------')
        t = gerarListaFrac()
        print('Lista: ', t)
        menorFracLista(t)
        
    
        
    elif opcao == 0:
        print('OBRIGADo ;)')
        
    else:
        print('Opção inválida!')
        
        
        
        
        
        
        
        
        
        

        
        
        

























