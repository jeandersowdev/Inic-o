def bubble_sort():

    n = len(vetor)


for i in range(n):
    troca = False
for j in range(0, n - 1 - 1):
    if vetor[j] > vetor[j + 1]:
        vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

troca = True
if not troca:
    break
vetor = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]
print("Bubble Sort otimizado!")

vetor_ordenado = bubble_sort(vetor.copy())
print(vetor_ordenado)
