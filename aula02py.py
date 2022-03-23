## Todo objeto em memória de programação
## Variáveis estruturas de dados começam na posição 0

fruta ="laranja"

print(fruta[5])
print(fruta[0:4])  ##4 não entra na conta, pois é posição de parada = laran
print(fruta[0:5])  

## Tamanho da string ou estrutura de dados

len(fruta)

## Contar objetos de string com a função count

print(fruta.count('a'))         ## quantas letras a tem na palavra laranja

## Replace Mudar valor em memória
print(fruta.replace('laranja', 'abacaxi'))      ## laranja é abacaxi nessa linha
print(fruta)        ## voltou a ser laranja, pois é o valor da variável dela

######################################################################
## Operadores Relacionais

num1 =20
num2 =80

print(num1>num2)     ## True or False - Booleano

## Operadores Lógicos

# AND - Símbolo - and
# OR - Símbolo - or
# NOT - Símbolo - not

num3 =40
num4 =30
num5 =10

## AND
print(num3<=num4 and num3 > num5)  ## todos precisam ser verdadeiros

## OR
print(num3<=num4 or num3< num5)   ## apenas um precisa ser verdadeiro

## NOT
print(num3<=num4 or not num3< num5)  ## é ou não é, exemplo: if cadeira not preta  - testa e valida algo