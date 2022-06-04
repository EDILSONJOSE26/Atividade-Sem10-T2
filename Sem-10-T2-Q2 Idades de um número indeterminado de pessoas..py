pessoas = 0
maior = 0
menor = 0
soma =  0



while True:
    idade = int(input())
    pessoas +=1
    soma +=idade
    tudo = soma
    if idade == 0:
        pessoas -=1
        break
    if pessoas == 1:
        maior = menor = idade
    else:
        if idade > maior:
                maior = idade
        if idade < menor:
            menor = idade
         
           

if pessoas !=0:
    print(pessoas)
    
if pessoas != 0:
    print(f'{soma / pessoas:.2f}')

if pessoas != 0:
    
    print(menor)
if pessoas != 0:
    print(maior)
