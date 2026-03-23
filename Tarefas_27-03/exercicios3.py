ano=int(input("digite um ano: "))

if ano%4==0 and not ano%100==0 or ano%400==0:
    print("é bissexto")
else:
    print("não é bissesto")

