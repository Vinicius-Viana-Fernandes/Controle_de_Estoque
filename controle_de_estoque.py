class Produto:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Principal:
    def menu(self):
        print('Menu Principal')
        print('1 - Cadastro')
        print('2 - Movimentação')
        print('3 - Reajuste')
        print('4 - Relatórios')
        print('5 - Sair')
        opcao = int(input('Digite a opção: '))

        if opcao == 1:
            op_cad = Cadastro()
            op_cad.menu()
        elif opcao == 2:
            self.movimentacao()
        elif opcao == 3:
            self.reajuste()
        elif opcao == 4:
            self.gravaRelatorio()
        elif opcao == 5:
            pass
        else:
            print('Opção inválida')
            self.menu()

    def movimentacao(self):
        movimentacao = int(input('Escolha o tipo de movimentação que deseja fazer, [1] para compra, [2] para venda: '))
        prod = input('Qual o produto que deseja movimentar: ')

        for i in ins:
            if prod.lower() == i['nome'].lower():
                qnt = int(input('Quantos {} foram {}: '.format(prod, "comprados" if movimentacao == 1 else "vendidos")))
                if movimentacao == 1:
                    i['quantidade'] += qnt
                else:
                    i['quantidade'] -= qnt

                print(ins)
                self.menu()
                return

        print('Produto não encontrado!')
        self.menu()

    def reajuste(self):
        busca = input('Digite o nome do produto que deseja reajustar: ')
        for i in ins:
            if busca.lower() == i['nome'].lower():
                novo = float(input('Altere o valor de {}, que atualmente é: {} para: '.format(busca, i['preco'])))
                i['preco'] = novo
                print('O preço atual de {}, é: {}'.format(busca, i['preco']))
                self.menu()
                return
        print('Produto não encontrado!')
        self.menu()

    def gravaRelatorio(self):
        total = 0
        with open('../../../../Downloads/relatorio.txt', 'w', encoding='utf-8') as arq:
            arq.write('ACME Inc.                           Lista de produtos\n')
            arq.write('------------------------------------------------------\n')
            arq.write('Descrição         Quantidade             Total\n')
            for i in ins:
                valor = i['quantidade'] * i['preco']
                arq.write(f"{i['nome'].ljust(18)} {str(i['quantidade']).ljust(20)} R${valor:.2f}\n")
                total += i['quantidade'] * i['preco']
            arq.write('\n-------------------------------------------------------\n')
            arq.write('Valor total de produtos R${:.2f}'.format(total))
        self.menu()


class Cadastro(Principal):
    def menu(self):
        print('Menu Cadastro')
        print('1 - Cadastrar novo produto')
        print('2 - Alterar Produto')
        print('3 - Excluir Produto')
        print('4 - Consultar Produto')
        print('5 - Voltar')
        opcao = int(input('Digite a opção: '))
        if opcao == 1:
            self.inserir()
        elif opcao == 2:
            self.alterar()
        elif opcao == 3:
            self.excluir()
        elif opcao == 4:
            self.consultar()
        elif opcao == 5:
            objeto.menu()
        else:
            print('Opção inválida')
            self.menu()

    def inserir(self):
        nome = input('Digite o nome do Produto: ')
        preco = float(input('Digite o preço do produto {}: '.format(nome)))
        quantidade = int(input('Digite a quantidade do produto {}: '.format(nome)))
        ins.append({'nome': nome, 'preco': preco, 'quantidade': quantidade})
        print(ins)
        self.menu()

    def alterar(self):
        busca = input('Digite o nome do produto que está procurando: ')
        for i in ins:
            if busca.lower() == i['nome'].lower():
                novo = input('Altere, {} para: '.format(busca))
                i['nome'] = novo
                print("Alterado com sucesso!")
                self.menu()
                return
        print('Produto não encontrado!')
        self.menu()

    def excluir(self):
        busca = input('Digite o nome do produto que quer excluir: ')
        for i in ins:
            if busca.lower() == i['nome'].lower():
                excluir = str(input('Você tem certeza que quer excluir o item {} ? [sim/nao]'.format(i['nome'])))
                if excluir.lower() == 'sim':
                    ins.remove(i)
                    print('Item {}, removido!'.format(i))
                    print('Lista atual: {}'.format(ins))
                    self.menu()
                elif excluir.lower() == 'nao':
                    self.menu()
                return
        print('Produto não encontrado!')
        self.menu()

    def consultar(self):
        consulta = input('Qual produto deseja consultar? ')
        for i in ins:
            if consulta.lower() == i['nome'].lower():
                print("Produto:", i['nome'], "Preço:", i['preco'], "Quantidade:", i['quantidade'])
                self.menu()
                return
        print('Produto não encontrado!')
        self.menu()


objeto = Principal()
ins = [{'nome': 'tomate', 'preco': 20, 'quantidade': 3}, {'nome': 'maça', 'preco': 20, 'quantidade': 3}]
objeto.menu()
