def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        troca = False
        for j in range(0, n - 1 - i):  # Corrigido o intervalo
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                troca = True  # Define troca como True se ocorrer uma troca
        if not troca:
            break  # Sai se nenhuma troca ocorreu, significando que a lista está ordenada

    return vetor  # Retorna a lista ordenada


vetor = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]
print("Bubble Sort otimizado!")
vetor_ordenado = bubble_sort(vetor.copy())
print(vetor_ordenado)
