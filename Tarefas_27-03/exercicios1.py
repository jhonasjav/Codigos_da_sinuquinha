print("---escolha um caminho---")
continuar=1


while continuar==1:

 primeiro=int(input("1.direita  2.esquerda: "))



#direita
 if primeiro ==1:
     print("voce encontrou uma montanha")
     segundo=int(input("1.subir 2.voltar: "))
     if segundo==1:
        print("voce encontrou um tesouro")
        continuar=0
     else:
        print("voce esta perdido na floresta")

    
#esquerda
 else:
     print("voce encontrou um rio")
     segundo2=int(input("1.atravessar 2.voltar: "))
     if segundo2==1:
        print("voce encontrou uma vila segura")
        continuar=0     
     else:
        print("voce esta perdido na floresta")
    