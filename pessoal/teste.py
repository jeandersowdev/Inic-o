# Algoritmo de soma


def soma(a, b):  # Função de soma
    return a + b


# Obtém os valores de  a e b do usúario
a = int(input("Digite um valor para a: "))
b = int(input("Digite um valor para b: "))

resultado = soma(a, b)  # Chamada da função e armazenamento do resultado

print("O resultado da soma é:", resultado)  # Imprime o resultado na tela
