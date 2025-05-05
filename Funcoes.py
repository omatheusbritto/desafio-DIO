from Classe import *

usuarios = {}

def cadastrar_usuario():
    cpf = input("Digite o CPF do usuário: ")
    if cpf in usuarios:
        print("Usuário já cadastrado! Deseja atualizar? (s/n)")
        opcao = input()
        if opcao.lower() != 's':
            return

    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    usuarios[cpf] = Cliente(cpf, nome, email, telefone, endereco)
    print("Usuário cadastrado com sucesso!")

def criar_conta():
    cpf = input("Digite o CPF do titular: ")
    if cpf not in usuarios:
        print("Usuário não encontrado! Cadastre o usuário primeiro.")
        return
    
    agencia = input("Digite a agência: ")
    numero_conta = input("Digite o número da conta: ")

    usuarios[cpf].adicionar_conta(numero_conta, agencia)

def listar_usuarios():
    cpf = input("Digite o CPF para listar os dados: ")
    if cpf in usuarios:
        usuario = usuarios[cpf]
        print(f"Nome: {usuario.nome}\nEmail: {usuario.email}\nTelefone: {usuario.telefone}\nEndereço: {usuario.endereco}")
        if usuario.contas:
            for conta in usuario.contas:
                print(f"Conta - Agência: {conta.agencia}, Nº: {conta.numero}, Saldo: R${conta.saldo:.2f}")
    else:
        print("Usuário não encontrado!")

def menu_principal():
    while True:
        print("""
| ============== MENU PRINCIPAL =========== |
| PARA FUNÇÕES BANCÁRIAS -------------- [1] |
| PARA CADASTRAR USUÁRIOS ------------- [2] |
| PARA CRIAR CONTA -------------------- [3] |
| PARA LISTAR USUÁRIOS ---------------- [4] |
| PARA SAIR --------------------------- [0] |
| ========================================= |
        """)
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            menu_bancario()
        elif opcao == "2":
            cadastrar_usuario()
        elif opcao == "3":
            criar_conta()
        elif opcao == "4":
            listar_usuarios()
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

def menu_bancario():
    cpf = input("Digite seu CPF: ")
    if cpf in usuarios and usuarios[cpf].contas:
        conta = usuarios[cpf].contas[0]
        while True:
            print("""
| ============ FUNÇÕES BANCÁRIAS ========== |
| Para SACAR -------------------------- [1] |
| Para DEPOSITAR ---------------------- [2] |
| Para SALDO -------------------------- [3] |
| Para EXTRATO ------------------------ [4] |
| Para VOLTAR AO MENU PRINCIPAL ------- [5] |
            """)
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                valor = float(input("Valor a sacar R$: "))
                conta.sacar(valor)
            elif opcao == "2":
                valor = float(input("Valor a depositar R$: "))
                conta.depositar(valor)
            elif opcao == "3":
                conta.ver_saldo()
            elif opcao == "4":
                conta.historico.mostrar_extrato()
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")
    else:
        print("Usuário não encontrado ou sem conta.")