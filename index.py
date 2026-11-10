'Crie um menu com while e match-case para registrar itens e seus preços, acumular o total e encerrar ao escolher sair, valide as opções e mostre o total final.'''
 
print("Programa registrador de itens")
 
valorTotalCarrinho = 0
 
escolha = input("Escolha uma opção: \n1-Selecionar item\n0- Sair\n").strip()
#STRIP funciona para excluir os Espaços do início e fim na resposta e fazer funfar
 
match escolha:
    case "0":
        print("Saindo...")
    case "1":
        while True:
            print("Itens disponíveis.")
            print("1 - Mouse gamer\nR$ 150,00")
            print("2 - Memória RAM\nR$ 13000,00")
            print("3 - Cadeira\nR$ 2000,00")
 
            item = int(input("Escolha um item (1, 2 ou 3) ou digite 0 para sair: "))
 
            match item:
                case 0:
                    print("Saindo...")
                    break
                case 1:
                    print("Você selecionou o MOUSE GAMER")
                    preco = 150
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case 2:
                    print("Você selecionou a MEMÓRIA RAM")
                    preco = 13000
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case 3:
                    print("Você selecionou a CADEIRA")
                    preco = 2000
                    quantidade = int(input("Digite a quantidade desejada: "))
                    valorTotalCarrinho += preco * quantidade
                case _:
                    print("Opção Inválida!")
 
    case _:
           print("Opção Inválida!")
 
print(f"Total do carrinho: R${valorTotalCarrinho:.2f}")


