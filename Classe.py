from datetime import datetime
import os

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor):
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.transacoes.append(f"{tipo}: R${valor:.2f} - {data_hora}")

    def mostrar_extrato(self):
        if not self.transacoes:
            print("Nenhuma transação realizada.")
        else:
            for transacao in self.transacoes:
                print(transacao)

class Conta:
    def __init__(self, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.historico = Historico()
        self.transacoes_diarias = 0
        self.valor_sacado_diario = 0.0

    def sacar(self, valor):
        if self.transacoes_diarias >= 10:
            print("Erro! Número de transações diárias atingido.")
            return False
        if valor > 500:
            print("Erro! Valor não permitido por saque.")
            return False
        if self.valor_sacado_diario + valor > 1500:
            print("Erro! Valor de saque diário atingido.")
            return False
        if valor <= 0:
            print("Erro! Valor não permitido.")
            return False
        if valor > self.saldo:
            print("Erro! Saldo insuficiente.")
            return False

        self.saldo -= valor
        self.transacoes_diarias += 1
        self.valor_sacado_diario += valor
        self.historico.adicionar_transacao("Saque", valor)
        print(f"Saque realizado! Saldo atual: R${self.saldo:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        return True

    def depositar(self, valor):
        if self.transacoes_diarias >= 10:
            print("Erro! Transação diária atingida.")
            return False
        if valor <= 0:
            print("Erro! Valor não permitido.")
            return False

        self.saldo += valor
        self.transacoes_diarias += 1
        self.historico.adicionar_transacao("Depósito", valor)
        print(f"Depósito realizado! Saldo atual: R${self.saldo:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        return True

    def ver_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

class Cliente:
    def __init__(self, cpf, nome, email, telefone, endereco):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, numero, agencia):
        conta = Conta(numero, agencia)
        self.contas.append(conta)
        print(f"Conta criada com sucesso! Agência: {agencia}, Nº Conta: {numero}")