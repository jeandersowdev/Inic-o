print("\nOlá! Seja bem-vindo(a)!")
idade = int(input("\nPor favor, digite sua idade: "))
carteira_motorista = int(
    input("\nVocê possui carteira de motorista? Digite 1 para Sim e 2 para Não: ")
)
pode_dirigir = False

if carteira_motorista == 1:
    pode_dirigir = True
if idade >= 18 and pode_dirigir:
    print("Você pode dirigir!")
else:
    print("Você não pode dirigir!")
