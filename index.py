import tkinter as tk
from tkinter import messagebox
import datetime

# Classe Obra
class Obra:
    def __init__(self, tipo, titulo, autor, ano_realizacao, data_entrada, valor_base):
        self.tipo = tipo
        self.titulo = titulo
        self.autor = autor
        self.ano_realizacao = ano_realizacao
        self.data_entrada = datetime.datetime.strptime(data_entrada, "%Y-%m-%d").date()
        self.valor_base = valor_base

    def idade(self):
        return datetime.date.today().year - self.ano_realizacao

    def custo(self):
        idade = self.idade()
        taxa_crescimento = self.obter_taxa_crescimento()
        return self.valor_base + (taxa_crescimento * idade)

    def obter_taxa_crescimento(self):
        if self.tipo == "Pintura":
            if 1300 >= self.ano_realizacao <= 1599:
                return 0.6
            elif 1600 <= self.ano_realizacao <= 1799:
                return 0.4
            elif self.ano_realizacao >= 1800:
                return 0.2
        elif self.tipo == "Escultura":
            if 1300 <= self.ano_realizacao <= 1599:
                return 0.7
            elif 1600 <= self.ano_realizacao <= 1799:
                return 0.5
            elif self.ano_realizacao >= 1800:
                return 0.3
        return 0.0

# Lista para armazenar as obras
colecao = []

# Funções auxiliares para interagir com Tkinter
def adicionar_obra():
    def confirmar_adicao():
        tipo = entry_tipo.get()
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        ano_realizacao = int(entry_ano_realizacao.get())
        data_entrada = entry_data_entrada.get()
        valor_base = float(entry_valor_base.get())
        nova_obra = Obra(tipo, titulo, autor, ano_realizacao, data_entrada, valor_base)
        colecao.append(nova_obra)
        messagebox.showinfo("Sucesso", "Obra adicionada com sucesso!")
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Adicionar Obra")

    tk.Label(add_window, text="Tipo[Pintura/Escultura/Rara]:").grid(row=0, column=0)
    entry_tipo = tk.Entry(add_window)
    entry_tipo.grid(row=0, column=1)

    tk.Label(add_window, text="Título:").grid(row=1, column=0)
    entry_titulo = tk.Entry(add_window)
    entry_titulo.grid(row=1, column=1)

    tk.Label(add_window, text="Autor:").grid(row=2, column=0)
    entry_autor = tk.Entry(add_window)
    entry_autor.grid(row=2, column=1)

    tk.Label(add_window, text="Ano de Realização:").grid(row=3, column=0)
    entry_ano_realizacao = tk.Entry(add_window)
    entry_ano_realizacao.grid(row=3, column=1)

    tk.Label(add_window, text="Data de Entrada (YYYY-MM-DD):").grid(row=4, column=0)
    entry_data_entrada = tk.Entry(add_window)
    entry_data_entrada.grid(row=4, column=1)

    tk.Label(add_window, text="Valor Base:").grid(row=5, column=0)
    entry_valor_base = tk.Entry(add_window)
    entry_valor_base.grid(row=5, column=1)

    tk.Button(add_window, text="Adicionar", command=confirmar_adicao).grid(row=6, columnspan=2)

def listar_obras():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    def exibir_resultados(tipo, obras):
        lista_window = tk.Toplevel(root)
        lista_window.title(f"Lista de Obras - Tipo: {tipo}")

        for obra in obras:
            texto_obra = f"{obra.tipo} - {obra.titulo} - {obra.autor} - {obra.ano_realizacao}"
            tk.Label(lista_window, text=texto_obra).pack()

    def buscar_obras():
        tipo_selecionado = entry_tipo.get()
        obras_filtradas = [obra for obra in colecao if obra.tipo.lower() == tipo_selecionado.lower()]

        if not obras_filtradas:
            messagebox.showinfo("Erro", f"Nenhuma obra encontrada para o tipo {tipo_selecionado}.")
            return

        exibir_resultados(tipo_selecionado, obras_filtradas)

    selecionar_window = tk.Toplevel(root)
    selecionar_window.title("Selecionar Tipo de Obra")

    tk.Label(selecionar_window, text="Digite o tipo de obra (Pintura/Escultura/Rara):").pack()
    entry_tipo = tk.Entry(selecionar_window)
    entry_tipo.pack()

    tk.Button(selecionar_window, text="Buscar", command=buscar_obras).pack()


def valor_total():
    total = sum(obra.custo() for obra in colecao)
    messagebox.showinfo("Valor Total", f"Valor total das obras: {total:.2f}")

def mudar_obras():
    def selecionar_obra():
        try:
            indice = int(entry_indice.get()) - 1
            if 0 <= indice < len(colecao):
                obra = colecao[indice]
                editar_obra(obra, indice)
                selecionar_window.destroy()
            else:
                messagebox.showerror("Erro", "Índice inválido.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    def editar_obra(obra, indice):
        def salvar_alteracoes():
            try:
                obra.tipo = entry_tipo.get()
                obra.titulo = entry_titulo.get()
                obra.autor = entry_autor.get()
                obra.ano_realizacao = int(entry_ano_realizacao.get())
                obra.data_entrada = datetime.datetime.strptime(entry_data_entrada.get(), "%Y-%m-%d").date()
                obra.valor_base = float(entry_valor_base.get())
                messagebox.showinfo("Sucesso", "Obra atualizada com sucesso!")
                editar_window.destroy()
            except ValueError:
                messagebox.showerror("Erro", "Dados inválidos. Verifique os campos e tente novamente.")

        editar_window = tk.Toplevel(root)
        editar_window.title("Editar Obra")

        tk.Label(editar_window, text="Tipo[Pintura/Escultura/Rara]:").grid(row=0, column=0)
        entry_tipo = tk.Entry(editar_window)
        entry_tipo.insert(0, obra.tipo)
        entry_tipo.grid(row=0, column=1)

        tk.Label(editar_window, text="Título:").grid(row=1, column=0)
        entry_titulo = tk.Entry(editar_window)
        entry_titulo.insert(0, obra.titulo)
        entry_titulo.grid(row=1, column=1)

        tk.Label(editar_window, text="Autor:").grid(row=2, column=0)
        entry_autor = tk.Entry(editar_window)
        entry_autor.insert(0, obra.autor)
        entry_autor.grid(row=2, column=1)

        tk.Label(editar_window, text="Ano de Realização:").grid(row=3, column=0)
        entry_ano_realizacao = tk.Entry(editar_window)
        entry_ano_realizacao.insert(0, obra.ano_realizacao)
        entry_ano_realizacao.grid(row=3, column=1)

        tk.Label(editar_window, text="Data de Entrada (YYYY-MM-DD):").grid(row=4, column=0)
        entry_data_entrada = tk.Entry(editar_window)
        entry_data_entrada.insert(0, obra.data_entrada.strftime("%Y-%m-%d"))
        entry_data_entrada.grid(row=4, column=1)

        tk.Label(editar_window, text="Valor Base:").grid(row=5, column=0)
        entry_valor_base = tk.Entry(editar_window)
        entry_valor_base.insert(0, obra.valor_base)
        entry_valor_base.grid(row=5, column=1)

        tk.Button(editar_window, text="Salvar Alterações", command=salvar_alteracoes).grid(row=6, columnspan=2)

    if not colecao:
        messagebox.showinfo("Aviso", "Nenhuma obra cadastrada para modificar.")
        return

    selecionar_window = tk.Toplevel(root)
    selecionar_window.title("Selecionar Obra para Modificar")

    tk.Label(selecionar_window, text="Obras disponíveis:").pack()
    for i, obra in enumerate(colecao, start=1):
        texto_obra = f"{i}: {obra.tipo} - {obra.titulo} - {obra.autor} - {obra.ano_realizacao}"
        tk.Label(selecionar_window, text=texto_obra).pack()

    tk.Label(selecionar_window, text="Digite o número da obra que deseja modificar:").pack()
    entry_indice = tk.Entry(selecionar_window)
    entry_indice.pack()

    tk.Button(selecionar_window, text="Selecionar", command=selecionar_obra).pack()


def eliminar_obras():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    def confirmar_exclusao():
        try:
            indice = int(entry_indice.get()) - 1
            if 0 <= indice < len(colecao):
                obra_removida = colecao.pop(indice)
                messagebox.showinfo("Sucesso", f"Obra '{obra_removida.titulo}' removida com sucesso!")
                selecionar_window.destroy()
            else:
                messagebox.showerror("Erro", "Índice inválido.")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido.")

    selecionar_window = tk.Toplevel(root)
    selecionar_window.title("Eliminar Obra")

    tk.Label(selecionar_window, text="Obras disponíveis:").pack()
    for i, obra in enumerate(colecao, start=1):
        texto_obra = f"{i}: {obra.tipo} - {obra.titulo} - {obra.autor} - {obra.ano_realizacao}"
        tk.Label(selecionar_window, text=texto_obra).pack()

    tk.Label(selecionar_window, text="Digite o número da obra que deseja eliminar:").pack()
    entry_indice = tk.Entry(selecionar_window)
    entry_indice.pack()

    tk.Button(selecionar_window, text="Confirmar", command=confirmar_exclusao).pack()


def listar_obras_raras():
    total = sum(obra.custo() for obra in colecao)
    messagebox.showinfo("Valor Total", f"Valor total das obras: {total:.2f}")


def listar_mais_antiga_mais_jovem():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    obra_mais_antiga = min(colecao, key=lambda x: x.ano_realizacao)
    obra_mais_jovem = max(colecao, key=lambda x: x.ano_realizacao)

    resultados_window = tk.Toplevel(root)
    resultados_window.title("Obra Mais Antiga e Mais Jovem")

    tk.Label(resultados_window, text="Obra Mais Antiga:").pack()
    texto_mais_antiga = f"{obra_mais_antiga.tipo} - {obra_mais_antiga.titulo} ({obra_mais_antiga.ano_realizacao})"
    tk.Label(resultados_window, text=texto_mais_antiga).pack()

    tk.Label(resultados_window, text="Obra Mais Jovem:").pack()
    texto_mais_jovem = f"{obra_mais_jovem.tipo} - {obra_mais_jovem.titulo} ({obra_mais_jovem.ano_realizacao})"
    tk.Label(resultados_window, text=texto_mais_jovem).pack()


def indicar_mais_menos_valiosa():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    obra_mais_valiosa = max(colecao, key=lambda x: x.custo())
    obra_menos_valiosa = min(colecao, key=lambda x: x.custo())

    resultados_window = tk.Toplevel(root)
    resultados_window.title("Obra Mais e Menos Valiosa")

    tk.Label(resultados_window, text="Obra Mais Valiosa:").pack()
    texto_mais_valiosa = f"{obra_mais_valiosa.tipo} - {obra_mais_valiosa.titulo} ({obra_mais_valiosa.custo():.2f})"
    tk.Label(resultados_window, text=texto_mais_valiosa).pack()

    tk.Label(resultados_window, text="Obra Menos Valiosa:").pack()
    texto_menos_valiosa = f"{obra_menos_valiosa.tipo} - {obra_menos_valiosa.titulo} ({obra_menos_valiosa.custo():.2f})"
    tk.Label(resultados_window, text=texto_menos_valiosa).pack()


def indicar_idade_media():
    if not colecao:
        messagebox.showinfo("Idade Média", "Nenhuma obra cadastrada.")
        return

    soma_idades = sum(obra.idade() for obra in colecao)
    media_idades = soma_idades / len(colecao)
    messagebox.showinfo("Idade Média", f"A idade média das obras é: {media_idades:.2f} anos.")

def listar_dez_antigas_tipo():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    def exibir_resultados(tipo, obras):
        resultados_window = tk.Toplevel(root)
        resultados_window.title(f"10 Obras Mais Antigas - {tipo}")

        for obra in obras:
            texto_obra = f"{obra.tipo} - {obra.titulo} ({obra.ano_realizacao})"
            tk.Label(resultados_window, text=texto_obra).pack()

    def buscar_obras():
        tipo_selecionado = entry_tipo.get()
        obras_filtradas = [obra for obra in colecao if obra.tipo == tipo_selecionado]

        if not obras_filtradas:
            messagebox.showinfo("Erro", "Nenhuma obra encontrada para o tipo selecionado.")
            return

        obras_ordenadas = sorted(obras_filtradas, key=lambda x: x.ano_realizacao, reverse=True)[:10]
        exibir_resultados(tipo_selecionado, obras_ordenadas)

    selecionar_window = tk.Toplevel(root)
    selecionar_window.title("Selecionar Tipo")

    tk.Label(selecionar_window, text="Digite o tipo de obra (Pintura/Escultura/Rara):").pack()
    entry_tipo = tk.Entry(selecionar_window)
    entry_tipo.pack()

    tk.Button(selecionar_window, text="Buscar", command=buscar_obras).pack()


def listar_dez_maior_valor():
    if not colecao:
        messagebox.showinfo("Erro", "Nenhuma obra cadastrada.")
        return

    obras_ordenadas = sorted(colecao, key=lambda x: x.custo(), reverse=True)[:10]

    resultados_window = tk.Toplevel(root)
    resultados_window.title("10 Obras com Maior Valor")

    for obra in obras_ordenadas:
        texto_obra = f"{obra.tipo} - {obra.titulo} ({obra.custo():.2f})"
        tk.Label(resultados_window, text=texto_obra).pack()

# Interface principal
root = tk.Tk()
root.title("Museu Nacional de Belas Artes")

# Botões do menu
tk.Button(root, text="Adicionar Obra", command=adicionar_obra).pack(fill=tk.X)
tk.Button(root, text="Modificar Obras", command=mudar_obras).pack(fill=tk.X)
tk.Button(root, text="Eliminar Obras", command=eliminar_obras).pack(fill=tk.X)
tk.Button(root, text="Listar Obras Por Tipo", command=listar_obras).pack(fill=tk.X)
tk.Button(root, text="Listar Obras Raras", command=listar_obras_raras).pack(fill=tk.X)
tk.Button(root, text="Listar 10 Obras Maior Valor[Tipo]", command=listar_dez_maior_valor).pack(fill=tk.X)
tk.Button(root, text="Listar 10 Obras + Antigas[Tipo]", command=listar_dez_antigas_tipo).pack(fill=tk.X)
tk.Button(root, text="Indicar Idade Média das Obras", command=indicar_idade_media).pack(fill=tk.X)
tk.Button(root, text="Indicar a + e a - Valiosa das Obras", command=indicar_mais_menos_valiosa).pack(fill=tk.X)
tk.Button(root, text="Listar a + Antiga e a + Jovem", command=listar_mais_antiga_mais_jovem).pack(fill=tk.X)
tk.Button(root, text="Valor Total das Obras", command=valor_total).pack(fill=tk.X)
tk.Button(root, text="Sair", command=root.quit).pack(fill=tk.X)

root.mainloop()
