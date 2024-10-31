nome_comuns = ["Ana", "Lucas", "Maria", "João", "Pedro"]
print("Olá! Seja bem-vindo(a)!")
nome = input("\nPor favor, digite seu nome: ")
print("\n O que existe no vetor: ")
print("\n", nome_comuns)

if (
    (nome == nome_comuns[0])
    or (nome == nome_comuns[1])
    or (nome == nome_comuns[2])
    or (nome == nome_comuns[3])
    or (nome == nome_comuns[4])
):
    print("\n")
    nome = input("\n Que", nome, "nome comum...")
    print("\n")  # Espaço apenas estético

else:
    print("\n")  # Espaço apenas estético
    print("\n Nossa", nome, "que nome lindo e diferente!")
    print("\n")  # Espaço apenas estético
