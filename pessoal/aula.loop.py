# Loops- Repetição com while e for

# Imprimindo números de 1 a 5 usando while

contador = 1

while contador <= 5:
    print(contador)
    contador += 1

numero = int(input("Digite um número positivo: "))

while numero <= 0:
    print("Número inválido. Tente novamente.")
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)

# Função range().
# Imprimindo números de 0 a 4 usando for e range

for i in range(5):
    print(i)

# Loop for com Intervalo e Passo
# Imprimindo números de 1 a 10, pulando de 2 em 2
for i in range(1, 11, 2):
    print(i)


# Inteirando sobre uma Lista com for
# Lista de frutas

frutas = ["maçã", "banana", "laranja"]
# Iterando lista
for fruta in frutas:
    print(fruta)

# Imprimindo números de 1 a 15, pulando o número 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
