import sys, os

prioridade_1 = []
prioridade_2 = []
prioridade_3 = []
prioridade_4 = []
prioridades_possiveis = ["1", "2", "3", "4"]
opcao = ...
opcao_invalida = "Você digitou uma opção invalida ou indisponivel."
pergunta_prioridade = "Qual o nível de prioridade? (1/2/3/4):"
tarefa_inexistente = "A tarefa que você digitou não existe."

def troca_de_prioridade(tarefa, nova_prioridade, prioridade_atual):
  try:
    if prioridade_atual == "1":
      match nova_prioridade:
        case "1":
          prioridade_1.remove(tarefa)
          prioridade_1.append(tarefa)
        case "2":
          prioridade_1.remove(tarefa)
          prioridade_2.append(tarefa)
        case "3":
          prioridade_1.remove(tarefa)
          prioridade_3.append(tarefa)
        case "4":
          prioridade_1.remove(tarefa)
          prioridade_4.append(tarefa)
        case _:
          limpar_tela()
          print(opcao_invalida)
          voltar_menu()
    elif prioridade_atual == "2":
      match nova_prioridade:
        case "1":
          prioridade_2.remove(tarefa)
          prioridade_1.append(tarefa)
        case "2":
          prioridade_2.remove(tarefa)
          prioridade_2.append(tarefa)
        case "3":
          prioridade_2.remove(tarefa)
          prioridade_3.append(tarefa)
        case "4":
          prioridade_2.remove(tarefa)
          prioridade_4.append(tarefa)
        case _:
          limpar_tela()
          print(opcao_invalida)
          voltar_menu()
    elif prioridade_atual == "3":
      match nova_prioridade:
        case "1":
          prioridade_3.remove(tarefa)
          prioridade_1.append(tarefa)
        case "2":
          prioridade_3.remove(tarefa)
          prioridade_2.append(tarefa)
        case "3":
          prioridade_3.append(tarefa)
          prioridade_3.remove(tarefa)
        case "4":
          prioridade_3.remove(tarefa)
          prioridade_4.append(tarefa)
        case _:
          limpar_tela()
          print(opcao_invalida)
          voltar_menu()
    elif prioridade_atual == "4":
      match nova_prioridade:
        case "1":
          prioridade_4.remove(tarefa)
          prioridade_1.append(tarefa)
        case "2":
          prioridade_4.remove(tarefa)
          prioridade_2.append(tarefa)
        case "3":
          prioridade_4.remove(tarefa)
          prioridade_3.append(tarefa)
        case "4":
          prioridade_4.remove(tarefa)
          prioridade_4.append(tarefa)
        case _:
          limpar_tela()
          print(opcao_invalida)
          voltar_menu()
    else:
      print(opcao_invalida)
      voltar_menu()
  except ValueError:
    print(opcao_invalida)
    voltar_menu()
  print("Troca feita com sucesso.")
  voltar_menu()

def voltar_menu():
  print(53*"-")
  opcao = input("Digite [M] para voltar para o menu ou [S] para sair:".center(53))

  if(opcao == "M" or opcao == "m"):
    menu()
  elif(opcao == "s" or opcao == "S"):
    sys.exit()
  else:
    limpar_tela()
    print(opcao_invalida)
    voltar_menu()

def limpar_tela(): 
  os.system("cls")

def executar_opcao(opcao):
  if(opcao == "1"):
    adicionar_tarefa()
  elif(opcao == "2"):
    excluir_tarefa()
  elif(opcao == "3"):
    exibir_lista_de_tarefas()
  elif(opcao == "4"):
    substituir_tarefa()
  elif(opcao == "5"):
    mudar_prioridade_tarefa()
  elif(opcao == "S" or opcao == "s"):
    sys.exit()
  else:
    print(opcao_invalida)
    voltar_menu()

def menu():
  limpar_tela()
  print("O P Ç Õ E S".center(15))
  print(15 * "-")
  print("[1] - Adicionar tarefa")
  print("[2] - Excluir tarefa")
  print("[3] - Exibir sua lista de tarefas")
  print("[4] - Substituir tarefas")
  print("[5] - Mudar a prioridade de uma tarefas", end= "\n\n")
  print("[S] - Sair")
  print(15 * "-")
  opcao = input("Digite o valor correspondente a sua opção:")

  executar_opcao(opcao)

def adicionar_tarefa():
  limpar_tela()
  tarefa = input("Digite uma tarefa: ")
  prioridade = input(pergunta_prioridade)

  if(prioridade == "1"):
    prioridade_1.append(tarefa)
    print(f"Nova tarefa adicionada: Prioridade 1 - {tarefa}")
  elif(prioridade == "2"):
    prioridade_2.append(tarefa)
    print(f"Nova tarefa adicionada: Prioridade 2 - {tarefa}")
  elif(prioridade == "3"):
    prioridade_3.append(tarefa)
    print(f"Nova tarefa adicionada: Prioridade 3 - {tarefa}")
  elif(prioridade == "4"):
    prioridade_4.append(tarefa)
    print(f"Nova tarefa adicionada: Prioridade 4 - {tarefa}")
  else:
    print(opcao_invalida)
    voltar_menu()
 
  voltar_menu()

def excluir_tarefa():
  limpar_tela()
  tarefa = input("Digite o nome da tarefa que deseja excluir: ")
  excluir_quantas = input("Deseja excluir [T]odas as tarefas com esse nome ou apenas [1]?")
  prioridade = input(pergunta_prioridade)

  if(excluir_quantas == "1"):
    if(prioridade == "1" and tarefa in prioridade_1):
      prioridade_1.remove(tarefa)
      print(f"Tarefa removida: Prioridade 1 - {tarefa}")
    elif(prioridade == "2" and tarefa in prioridade_2):
      prioridade_2.remove(tarefa)
      print(f"Tarefa removida: Prioridade 2 - {tarefa}")
    elif(prioridade == "3" and tarefa in prioridade_3):
      prioridade_3.remove(tarefa)
      print(f"Tarefa removida: Prioridade 3 - {tarefa}")
    elif(prioridade == "4" and tarefa in prioridade_4):
      prioridade_4.remove(tarefa)
      print(f"Tarefa removida: Prioridade 4 - {tarefa}")
    else:
      print(opcao_invalida)
    voltar_menu()
  elif(excluir_quantas == "T" or excluir_quantas == "t"):
    if(prioridade == "1" and tarefa in prioridade_1):
      while(tarefa in prioridade_1):
        prioridade_1.remove(tarefa)
      print(f"Tarefa removida completamente: Prioridade 1 - {tarefa}")
      voltar_menu()
    if(prioridade == "2" and tarefa in prioridade_2):
      while(tarefa in prioridade_2):
        prioridade_2.remove(tarefa)
      print(f"Tarefa removida completamente: Prioridade 2 - {tarefa}")
      voltar_menu()
    if(prioridade == "3" and tarefa in prioridade_3):
      while(tarefa in prioridade_3):
        prioridade_3.remove(tarefa)
      print(f"Tarefa removida completamente: Prioridade 3 - {tarefa}")
      voltar_menu()
    if(prioridade == "4" and tarefa in prioridade_4):
      while(tarefa in prioridade_4):
        prioridade_4.remove(tarefa)
      print(f"Tarefa removida completamente: Prioridade 4 - {tarefa}")
      voltar_menu()
    else:
      print(opcao_invalida)
      voltar_menu()
  else:
      print(opcao_invalida)
      voltar_menu()


def substituir_tarefa():
  limpar_tela()
  print("S U B S T I T U I R  T A R E F A".center(34))
  print(34 * "-")
  tarefa = input("Digite o nome da tarefa que deseja substituir: ")
  prioridade = input(pergunta_prioridade)
  nova_tarefa = input("Digite a tarefa que ficará no lugar da antiga: ")

  if(prioridade == "1" and tarefa in prioridade_1):
    for i in prioridade_1:
      if i == tarefa:
        prioridade_1.insert(prioridade_1.index(i), nova_tarefa)
        prioridade_1.remove(i)
        print(f"Nova tarefa implementada: Prioridade 1 - {tarefa}")
        break
  elif(prioridade == "2" and tarefa in prioridade_2):
    for i in prioridade_2:
      if i == tarefa:
        prioridade_2.insert(prioridade_2.index(i), nova_tarefa)
        print(f"Nova tarefa implementada: Prioridade 2 - {tarefa}")
        break
  elif(prioridade == "3" and tarefa in prioridade_3):
    for i in prioridade_3:
      if i == tarefa:
        prioridade_3.insert(prioridade_3.index(i), nova_tarefa)
        print(f"Nova tarefa implementada: Prioridade 3 - {tarefa}")
        break
  elif(prioridade == "4" and tarefa in prioridade_4):
    for i in prioridade_4:
      if i == tarefa:
        prioridade_4.insert(prioridade_4.index(i), nova_tarefa)
        print(f"Nova tarefa implementada: Prioridade 4 - {tarefa}")
        break
  else:
    print(opcao_invalida)
    voltar_menu()
    
  voltar_menu()

def mudar_prioridade_tarefa():
  limpar_tela()
  print("M U D A R  P R I O R I D A D E".center(32))
  print(32*"-")
  tarefa = input("Que tarefa deseja trocar de prioridade? ")
  prioridade_atual = input(pergunta_prioridade)
  nova_prioridade = input("Qual a nova prioridade da tarefa? ")

  try:
    if(prioridade_atual in prioridades_possiveis):
      troca_de_prioridade(tarefa, nova_prioridade, prioridade_atual)
  except NameError:
    print(opcao_invalida)
    voltar_menu
  
  else:
    print(opcao_invalida)
    voltar_menu()

def exibir_lista_de_tarefas():
  limpar_tela()
  print("T A R E F A S".center(15))
  print(15*"-")
  
  for i in prioridade_1:
    print("1 - ", i)
  for i in prioridade_2:
    print("2 - ", i)
  for i in prioridade_3:
    print("3 - ", i)
  for i in prioridade_4:
    print("4 - ", i)

  voltar_menu()

menu()