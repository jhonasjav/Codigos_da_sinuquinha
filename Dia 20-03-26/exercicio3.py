idade=int(input("qual sua idade: "))
ingresso=(input("voce tem ingresso: "))

if ingresso=="s":
         ingresso=True
else:
    ingresso=False

if idade >= 18:
      if ingresso==True:
            print("bom filme")
else:
      print("nao deu boa")
      
      


