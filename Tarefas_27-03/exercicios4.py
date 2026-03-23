usuario="admin"
senha=int(1234)
guest="guest"


tentativa=str(input("usuario: "))






if tentativa==usuario:
    tentativa2=int(input("senha: "))
    if tentativa2==senha:
        print("login bem sucedido")
    else:
        print("senha incorreta")
elif tentativa==guest:
    print("Acesso restrito")


else:
    print("usario desconhecido")



    