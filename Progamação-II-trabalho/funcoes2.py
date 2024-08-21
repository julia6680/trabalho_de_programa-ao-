import funcoes2
def adicionar_medicamento(estoque, nome, quantidade):
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    return f"Medicamento {nome} adicionado com {quantidade} unidades."
def remover_medicamento(estoque, nome, quantidade):
    if nome in estoque and estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        if estoque[nome] == 0:
            del estoque[nome]
        return f"Medicamento {nome} removido com {quantidade} unidades."
    else:
        return "Medicamento não encontrado ou quantidade insuficiente."
def buscar_medicamento(estoque, nome):
    return estoque.get(nome, "Medicamento não encontrado.")

def listar_estoque(estoque):
    if estoque:
        return "\n".join([f"{nome}: {quantidade} unidades" for nome, quantidade in estoque.items()])
    else:
        return "Estoque vazio."
def vender_medicamento(estoque, nome, quantidade):
    if nome in estoque and estoque[nome] >= quantidade:
        estoque[nome] -= quantidade
        return f"Venda realizada: {quantidade} unidades de {nome}."
    else:
        return "Medicamento não encontrado ou quantidade insuficiente."
