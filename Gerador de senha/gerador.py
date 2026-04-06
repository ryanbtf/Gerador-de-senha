import random
import string
import json

ARQUIVO = "senhas.json"

def carregar_senhas():
    try:
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    except:
        return []
    
def salvar_senhas(senhas):
    with open(ARQUIVO, "w") as f:
        json.dump(senhas, f, indent=4)

def listar_senhas(senhas):
    for i in enumerate(senhas):
        print(i)


def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

def menu():
    senhas = carregar_senhas()

    while True:
        tamanho = input("Digite o tamanho da senha (0 para fechar o programa ou 1 para listar senhas): ")

        if tamanho == "0":
            break

        if tamanho == "1":
            listar_senhas(senhas)
            continue

        if not tamanho.isdigit():
            print("Digite um número válido!")
            continue

        senha = gerar_senha(int(tamanho))
        print("Senha gerada:", senha)

        senhas.append(senha)

        salvar_senhas(senhas)

menu()