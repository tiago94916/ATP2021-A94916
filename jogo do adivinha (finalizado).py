# -*- coding: utf-8 -*-
print('----------------------------------')
print('    Vamos jogar ao adivinha')
print('----------------------------------')

numero = int(input('Escolhe um número de 0-100:  '))
tentativa=0

if numero > 100 or numero < 0:
    print('ERRO!')
else:
    def jogo():
        a=0
        b=100
        c=100/2
        tentativa=1
        print("Este é o teu numero?: ",c)
        resposta=input("SIM OU NAO?: ")
        resposta=resposta.upper()
        while(resposta == "NAO"):
            resposta1=input("O numero que pensaste é maior(+) ou menor(-)?: ")
            
            if (resposta1 == "-"):
                b = c
                
            elif(resposta1 == "+"):
                a = c  
                
            soma=a+b
            c=int(soma/2)   
            print("Este é o teu valor: ", c)
            resposta=input("SIM OU NAO?: ")
            resposta=resposta.upper()
            tentativa+=1
        
        if(resposta=="SIM"):
                print("Consegui!") 
                print('Acertei em ',tentativa,'tentativa/s!')
    jogo()   
            