palavra_secret=100
palpite=0
while palpite!= palavra_secret:
    palpite =int(input("digite a num:"))
    if palpite> palavra_secret:
        print("muito alto")
    elif palpite < palavra_secret:
        print("muito baixo")
    else:
        print("acertou")
