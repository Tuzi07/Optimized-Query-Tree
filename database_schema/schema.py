tables = [
    "usuario",
    "contas",
    "tipoconta",
    "movimentacao",
    "tipomovimento",
    "categoria",
]

usuario_columns = [
    "idusuario",
    "nome",
    "logradouro",
    "numero",
    "bairro",
    "cep",
    "uf",
    "datanascimento",
]

contas_columns = [
    "idconta",
    "descricao",
    "tipoconta_idtipoconta",
    "usuario_idusuario",
    "saldoinicial",
]

tipoconta_columns = ["idtipoconta", "descriçao"]

movimentacao_columns = [
    "idmovimentacao",
    "datamovimentacao",
    "descricao",
    "tipomovimento_idtipomovimento",
    "categoria_idcategoria",
    "contas_idconta",
    "valor",
]

tipomovimento_columns = ["idtipomovimento", "descmovimentacao"]

categoria_columns = ["idcategoria", "desccategoria"]

table_columns = {
    "usuario": usuario_columns,
    "contas": contas_columns,
    "tipoconta": tipoconta_columns,
    "movimentacao": movimentacao_columns,
    "tipomovimento": tipomovimento_columns,
    "categoria": categoria_columns,
}


def is_column(column):
    table = ""
    if "." in column:
        table = column.split(".")[0].lower()
        column = column.split(".")[1].lower()
        if table in tables:
            if column not in table_columns[table]:
                return False
        else:
            return False

    for value in table_columns.values():
        if column.lower() in value:
            return True
    return False


def table_of_column(column, possible_tables):
    for key, columns in table_columns.items():
        if key in possible_tables:
            if column in columns:
                return key
