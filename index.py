# Tarefa de programação em python, exer. de título nº23 
import datetime

obras = []

def criar_obra(titulo, ano, autor, data_entrada, valor_base, categoria):
    return {
        "categoria": categoria,
        "titulo": titulo,
        "ano": ano,
        "autor": autor,
        "data_entrada": data_entrada,
        "valor_base": valor_base,
    }

def calcular_valor(obra):

    ano_atual = datetime.datetime.now().year

    idade = ano_atual - obra["ano"]

    if 1300 <= obra["ano"] <= 1599 and obra["categoria"] == "Pintura":
        taxa_crescimento = 0.6
    elif 1300 <= obra["ano"] <= 1599 and obra["categoria"] == "Escultura":
        taxa_crescimento = 0.7
    elif 1600 <= obra["ano"] <= 1799 and obra["categoria"] == "Pintura":
        taxa_crescimento = 0.4
    elif 1600 <= obra["ano"] <= 1799 and obra["categoria"] == "Escultura":
        taxa_crescimento = 0.5
    elif 1800 <= obra["ano"] <= ano_atual and obra["categoria"] == "Pintura":
        taxa_crescimento = 0.3
    elif 1800 <= obra["ano"] <= ano_atual and obra["categoria"] == "Escultura":
        taxa_crescimento = 0.2
    else:
        taxa_crescimento = 0.0 
    custo_obra = obra["valor_base"] + (taxa_crescimento * idade)
    resultado = round(custo_obra, 2)
    return resultado

def add_obra():
    titulo = input("Título: ")
    ano = int(input("Ano de realização: "))
    autor = input("Autor: ")
    data_entrada = input("Data de entrada (YYYY-MM-DD): ")
    valor_base = float(input("Valor base: "))
    categoria = input("Categoria (Pintura/Escultura/Raras): ")
    obras.append(criar_obra(titulo, ano, autor, data_entrada, valor_base, categoria))
    print("Obra adicionada com sucesso!")

def modificar_obra():
    titulo = input("Titulo da obra a modificar: ")
    for obra in obras:
        if obra["titulo"] == titulo:
            obra["titulo"] = input(f"Novo título ({obra['titulo']}): ") or obra["titulo"]
            obra["ano"] = int(input(f"Novo ano de realização ({obra['ano']}): ") or obra["ano"])
            obra["autor"] = input(f"Novo autor ({obra['autor']}): ") or obra["autor"]
            obra["data_entrada"] = input(f"Nova data de entrada ({obra['data_entrada']}): ") or obra["data_entrada"]
            obra["valor_base"] = round(float(input(f"Novo valor base ({obra['valor_base']:.2f}): ") or obra["valor_base"]), 2)
            obra["categoria"] = input(f"Nova categoria ({obra['categoria']}): ") or obra["categoria"]
            print("Obra modificada com sucesso!")
            return
    print("Obra não encontrada.")

def remove_obra():
    obra_titulo = input("Título da obra a remover: ")
    global obras
    obras = [obra for obra in obras if obra["titulo"] != obra_titulo]
    print("Obra removida com sucesso!")

def listar_obras_por_tipo():
    categoria = input("Digite o tipo de obra a listar (Pintura/Escultura/Raras): ")
    for obra in obras:
        if obra["categoria"] == categoria:
            print(obra)

def listar_obras_raras():
    for obra in obras:
        if obra["categoria"] == "Raras":
            print(obra)

def top_10_obras_mais_caras():
    categoria = input("Tipo de obra para listar as mais valiosas: ")
    filtered = [obra for obra in obras if obra["categoria"] == categoria]
    ordem_obras = sorted(filtered, key=calcular_valor, reverse=True)[:10]
    for obra in ordem_obras:
        print(obra, calcular_valor(obra))

def top_10_obras_mais_velhas():
    categoria = input("Tipo de obra para listar as mais antigas: ")
    filtered = [obra for obra in obras if obra["categoria"] == categoria]
    ordem_obras = sorted(filtered, key=lambda x: x["ano"], reverse=True)[:10]
    for obra in ordem_obras:
        print(obra)

def valor_total():
    print(f"Valor total das obras: {sum(calcular_valor(obra) for obra in obras):.2f} Kz")

def media_idade():
    ano_actual = datetime.datetime.now().year
    idades = [ano_actual - obra["ano"] for obra in obras]
    print("Idade média das obras:", sum(idades) / len(idades), "ano/s")

def mais_e_menos_valiosa():
    if not obras:
        print("Nenhuma obra disponível.")
        return
    mais_valiosa = max(obras, key=calcular_valor)
    menos_valiosa = min(obras, key=calcular_valor)
    print("Mais valiosa:", mais_valiosa, calcular_valor(mais_valiosa))
    print("Menos valiosa:", menos_valiosa, calcular_valor(menos_valiosa))

def mais_velha_e_mais_jovem():
    if not obras:
        print("Nenhuma obra disponível.")
        return
    mais_velha = min(obras, key=lambda x: x["ano"])
    mais_jovem = max(obras, key=lambda x: x["ano"])
    print("Mais antiga:", mais_velha)
    print("Mais jovem:", mais_jovem)

def main():
    while True:
        print("\nMenu:")
        print("a) Adicionar nova obra")
        print("b) Modificar obra")
        print("c) Eliminar obra")
        print("d) Listar obras por tipo")
        print("e) Listar obras raras")
        print("f) Top 10 obras mais valiosas")
        print("g) Top 10 obras mais antigas")
        print("h) Valor total das obras")
        print("i) Idade média das obras")
        print("j) Mais valiosa e menos valiosa")
        print("k) Mais antiga e mais jovem")
        print("q) Sair")

        choice = input("Escolha uma opção: ").lower()
        if choice == "a":
            add_obra()
        elif choice == "b":
            modificar_obra()
        elif choice == "c":
            remove_obra()
        elif choice == "d":
            listar_obras_por_tipo()
        elif choice == "e":
            listar_obras_raras()
        elif choice == "f":
            top_10_obras_mais_caras()
        elif choice == "g":
            top_10_obras_mais_velhas()
        elif choice == "h":
            valor_total()
        elif choice == "i":
            media_idade()
        elif choice == "j":
            mais_e_menos_valiosa()
        elif choice == "k":
            mais_velha_e_mais_jovem()
        elif choice == "q":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
