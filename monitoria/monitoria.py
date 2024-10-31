def menu():
    print("Oque deseja comprar? \n")
    print("1- Roupa\n")
    print("2- Comida\n")
    print("3- Computador\n")
    print("4- Assinatura\n")
    print("Escreva a opção desejada: \n")


# float dinheiro
# int opcao
dinheiro = float(input("Quanto eu tenho de dinheiro na carteira? \n"))
menu()

opcao = int(input("Qual a opção desejada? "))
if dinheiro > 100:
    print("Você possui na sua carteira ", dinheiro, " reais\n")
    print("Você pode comprar qualquer coisa da lista!\n")

elif dinheiro > 30:
    print("Você pode comprar: x coisas")
else:
    print("Infelizmente, tu tá duro!")
