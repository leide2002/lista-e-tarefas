soma=0
for x in range(1,6):
    num=float(input("digite os numeros:"))
    soma+= num
media =soma/5
print(f"{media}")
if media<=4:
    print(f"reprovado")
elif media >=7:
    print(f"aprovado")
else:
    (f"recuperação")
