palavra = []
conrtador=0

for contador in range(5):
    pessoa = input("digite os nome:")
    palavra.append(pessoa)
for pessoa in palavra:
    if pessoa[0]=="a" or pessoa[0]=="A":
        print(pessoa,end= " ")




