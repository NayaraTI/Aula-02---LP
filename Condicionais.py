## IF/ELSE ELIF para mais 1 condição IF

n3 = float(input("Digite o primeiro número: "))
n4 = float(input("Digite o segundo número: "))

if (n3 == 10 and n4 == 10):   ##identação 1 TAB ou 4 espaços para o bloco de código
    print("Números Reservados")

elif (n3>n4): 
    print("Primeiro número maior que o segundo")

elif (n3==n4): 
    print("Números Iguais")

else:
    print("Segundo número maior que o primeiro")