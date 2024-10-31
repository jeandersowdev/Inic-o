# Código do jogo feito na monitoria 26/10/2024

import random  # 1- Serve para usarmos um comando de pegar um número aleatório no código na linha 57;

partida = (
    0  # 2- Serve para termos noção de quantas vezes jogamos até vencer o computador;
)


def escolha_do_jogador(
    nome, parametro
):  # 3- Função para processar e atribuir uma opção de jogada para quem está jogando;
    if parametro == 1:
        escolha = "Pedra"
        print(f"O {nome} escolheu {escolha}")
    elif parametro == 2:
        escolha = "Papel"
        print(f"O {nome} escolheu {escolha}")
    elif parametro == 3:
        escolha = "Tesoura"
        print(f"O {nome} escolheu {escolha}")
    else:
        print("Jogada inválida!")
        print("Escolha uma opção válida...")
        escolha = input(tela_inicial())
    return escolha


def tela_inicial():  # 4- Função para exibir uma tela de pequenas instruções para o usuário;
    print("-- Jogo Pedra, Papel e Tesoura --")
    print("Instrução: o jogo só termina quando você ganhar do computador!")
    print("\n")
    print("Escolha uma jogada:")
    print("1- para escolher Pedra")
    print("2- para escolher Papel")
    print("3- para escolher Tesoura")


vencedor = "computador"  # 5- Inicializa a variável que servirá no loop <while>;

while vencedor != "jogador":  # 6- Só termina o jogo quando o jogador vencer;
    partida += 1
    print(f"\n--- Partida {partida} ---")
    tela_inicial()  # 7- Chamada da função
    opcao = int(
        input("Qual sua jogada? ")
    )  # 7.1- Interação com usuário para coletar jogada escolhida;
    print("\n")
    if (
        opcao <= 3 and opcao > 0
    ):  # 8- Tratamento de erro: caso jogador digitar um número errado o programa irá se repetir até que o número seja válido;
        print("--- Resultado ---")
        jogador = escolha_do_jogador(
            "Jogador", opcao
        )  # 9- Chamada da função que irá processar e atribuir opção de jogada ao jogador;
        opcao_do_computador = random.randint(
            1, 3
        )  # 10- Interação com computador para coletar jogada escolhida;
        computador = escolha_do_jogador(
            "Computador", opcao_do_computador
        )  # 11- Chamada da função que irá processar e atribuir opção de jogada ao computador;

        # 12- Processamento de informações e gerando o resultado do jogo. Essa etapa só acontece SE a opção escolhida for válida (um número entre 1 e 3);
        if jogador == computador:
            print("--- EMPATE ---")
        else:
            if jogador == "Pedra" and computador == "Papel":
                print("O computador venceu.")
            elif jogador == "Pedra" and computador == "Tesoura":
                print("Parabéns você venceu.")
                vencedor = "jogador"
            elif jogador == "Papel" and computador == "Pedra":
                print("Parabéns você venceu.")
                vencedor = "jogador"
            elif jogador == "Papel" and computador == "Tesoura":
                print("O computador venceu.")
            elif jogador == "Tesoura" and computador == "Pedra":
                print("O computador venceu.")
            elif jogador == "Tesoura" and computador == "Papel":
                print("Parabéns você venceu.")
                vencedor = "jogador"
    else:  # 13- Quando o jogador escolhe um número errado, é aqui que o código notifica o usuário, e o programa se repete;
        print("Opção inválida, faremos uma nova partida...\n")
print("FIM DE JOGO...")
