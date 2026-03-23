continuar=1


while continuar==1:
  

 ladoa=float(input("lado A: "))
 ladob=float(input("lado B: "))
 ladoc=float(input("lado C: "))

 lados=[ladoa,ladob,ladoc]

 lados.sort()
 menores=lados[0]+lados[1]



 if menores>lados[2]:
    if lados[0]==lados[2]and lados[0]==lados[1]:
     print("é um triando equilatero")
    elif lados[0]==lados[1]or lados[1]==lados[2]:
     print("é um triangulo isosceles")
    else:
     print("é um triangulo escaleno")
 else:
    print("não é triangulo")

 continuar=int(input("1.continuar 0.sair: "))
