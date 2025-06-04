# 🏦 Sistema Bancário em Python

Este é um sistema bancário simples desenvolvido em Python puro, com interface via terminal. Ele permite realizar operações bancárias básicas como depósito, saque, extrato, criação de contas e cadastro de usuários.

## 💡 Funcionalidades

- Criar usuários com CPF único
- Criar contas bancárias associadas a usuários existentes
- Realizar depósitos e saques com limite por operação e por dia
- Visualizar extrato da conta
- Listar todas as contas cadastradas

## 📋 Menu Principal

=============== MENU ================
[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[4] NOVA CONTA
[5] LISTAR CONTAS
[6] NOVO USUÁRIO
[0] SAIR

## 📌 Regras de Negócio

- Cada usuário é identificado por um **CPF único**
- Cada conta bancária possui:
  - Número da conta (incremental)
  - Agência (fixa como `0001`)
  - Saldo inicial de R$0
- Limite de saque:
  - **R$500 por saque**
  - **3 saques por dia**
- O extrato exibe um histórico de todas as transações realizadas
