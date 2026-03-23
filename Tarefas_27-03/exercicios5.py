cordx=int(input("digite X: "))

cordy=int(input("digite Y: "))

if cordx >=0 and cordx <=10 and cordy >=0 and cordy <=10:
    if cordx==10 or cordy==10:
        print("ta na borda")
    else:
        print("ta dentro")



else:
    print("nao ta dentro")