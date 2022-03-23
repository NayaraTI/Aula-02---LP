## Entrada de Dados com a função input 

nome = input("Digite o seu nome: ")
print(nome)


n1 = int(input("Digite o primeiro número: "))       ## não aceita número quebrados, exemplo: 45.50
n2 = float(input("Digite o segundo número: "))
print("A soma é: ", n1+n2)

idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))
idade3 = int(input("Digite a terceira idade: "))

print("O total das idades é: ", (idade1+idade2+idade3))
print("A média das idades é: ", (idade1+idade2+idade3)/3)
