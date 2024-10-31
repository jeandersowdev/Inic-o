def bubble_sort_otimizado(vetor):
    n = len(vetor)

    for i in range(n):

        maior_indice = 0

        for j in range(1, n - i):
            if vetor[j] > vetor[maior_indice]:
                maior_indice = j

        vetor[maior_indice], vetor[n - i - 1] = vetor[n - i - 1], vetor[maior_indice]

    return vetor


vetor = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]


print("Bubble Sort Otimizado:")
vetor_ordenado_otimizado = bubble_sort_otimizado(
    vetor.copy()
)  # Aplica a versão otimizada
print(vetor_ordenado_otimizado)
