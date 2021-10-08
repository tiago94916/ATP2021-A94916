# -*- coding: utf-8 -*-
print('Vamos jogar ao jogo dos 21 fósforos?')
opção=0
opção=input ('''      s -> SIM
      n -> NÃO
      
      »» ''')
      
if opção == 's':
    print ('E sabes as regras?')
    opt=0
    opt=input('''      s -> SIM
      n -> NÃO
      
      »» ''')
    if opt == 's':
        print('Siga!Começa Tu!')
        fósforos=21
        while True:
            print('Fósforos restantes: ', fósforos)
            fósforos_retirados = int(input('Entre 1 e 4 fósforos quantos tiras?: '))
            if fósforos_retirados < 1 or fósforos_retirados>=5:
                print('ERRO! Vai ver as regras de novo!')
                break
            print('Restam',fósforos-fósforos_retirados,'fósforos!')
            fósforos_pc = 5 - fósforos_retirados
            print('Sendo assim, eu tiro: ' ,fósforos_pc)
            fósforos -=5
            if fósforos==1:
                print('PERDESTE!Ficaste com o último fósforo!')
                break
           
            
    elif opt == 'n':
        print('Então é assim: Temos 21 fósforos e tu só podes tirar entre 1 e 4 fósforos, tu escolhes, depois tiro eu. Quem ficar com o último fósforo perde!')
        print('SIGA JOGAR')
        fósforos=21
        while True:
            print('Fósforos restantes: ', fósforos)
            fósforos_retirados = int(input('Entre 1 e 4 fósforos quantos tiras?: '))
            if fósforos_retirados < 1 or fósforos_retirados>=5:  
                fósforos_pc==0
                print('ERRO! Vai ver as regras de novo!')
                break
            print('Restam',fósforos-fósforos_retirados,'fósforos!')
            fósforos_pc = 5 - fósforos_retirados
            print('Sendo assim, eu tiro: ' ,fósforos_pc)
            fósforos -=5
            if fósforos==1:
                print('PERDESTE!Ficaste com o último fósforo!')
                break
           
    else:
        print('SIM ou NÃO!')
elif opção == 'n':
    print(':(')
else:
    print('Só podes escolher entre sim e não nabo!')
    
    
        
    
      



