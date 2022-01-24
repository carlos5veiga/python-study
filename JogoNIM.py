def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    
    if escolha==1:
        print("Você escolheu uma partida!")
        partida()
    if escolha==2:
        print("Você escolheu um campeonato!")
        n=1
        while n<=3:
            print("**** Rodada", n, "****")
            partida()
            n=n+1
        print("**** Final do campeonato! ****")
        print("Placar: Você 0 X 3 Computador")

def computador_escolhe_jogada(n,m):
    quant = m
    if n==1:
        return 1
    else:
        if n<=m:
            return n
        else:
            while quant>=1:
                if ((n-quant)%(m+1)==0):
                    return quant
                quant = quant - 1
        return m

def usuario_escolhe_jogada(n,m):
    while True:
        jogada = int(input("Quantas peças você vai tirar?"))
        if (jogada > 0 and jogada <= m and jogada<=n):
            return jogada
        else:
            print("Oops! Jogada inválida! Tente de novo.")

def resta(resto):
    if resto == 0:
        return True
    else:
        if resto == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
        else:
            print("Agora restam", resto, "peças no tabuleiro.")
        return False

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    voce = True
    gameOver = False
    if (n%(m+1)==0):
        print("Voce começa!")
        voce = True
    else:
        print("Computador começa!")
        voce = False
    while not gameOver:
        if voce:
            retirada = usuario_escolhe_jogada(n,m)
            if retirada == 1:
                print("Você tirou uma peça.")
            else:
                print("Voce tirou", retirada, "peças.")
            voce = False
        else:
            retirada = computador_escolhe_jogada(n,m)
            if retirada == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", retirada, "peças.")
            voce = True
        n = n - retirada
        if resta(n)==True:
            gameOver = True
            print("Fim do jogo! O computador ganhou!")
            
            
main()   
            
            
            
            
            
