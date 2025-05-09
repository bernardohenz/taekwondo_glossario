from taekwondo.glossary import Acoes, Bases, Direcoes, PartesCorpo


def main():
    # Exemplo de como listar todas as bases
    print("=== Bases ===")
    for base in Bases.listar_todos():
        print(f"{base['coreano']}: {base['portugues']}")
        print(f"Descrição: {base['descricao']}\n")

    # Exemplo de como listar todas as ações
    print("=== Ações ===")
    for acao in Acoes.listar_todos():
        print(f"{acao['coreano']}: {acao['portugues']}")
        print(f"Descrição: {acao['descricao']}\n")

    # Exemplo de como listar todas as direções
    print("=== Direções ===")
    for direcao in Direcoes.listar_todos():
        print(f"{direcao['coreano']}: {direcao['portugues']}")
        print(f"Descrição: {direcao['descricao']}\n")

    # Exemplo de como listar todas as partes do corpo
    print("=== Partes do Corpo ===")
    for parte in PartesCorpo.listar_todos():
        print(f"{parte['coreano']}: {parte['portugues']}")
        print(f"Descrição: {parte['descricao']}\n")


if __name__ == "__main__":
    main()
