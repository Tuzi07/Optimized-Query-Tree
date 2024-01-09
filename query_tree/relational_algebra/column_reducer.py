import re

from database_schema import schema


def reduce_columns(algebra):
    tables = tables_from_algebra(algebra)
    columns = columns_to_select(algebra)
    selected_table_columns = table_columns(tables, columns)
    for index, term in enumerate(algebra):
        if is_table_term(term):
            table = get_table(term)
            columns_of_table = selected_table_columns[table]
            unique_columns = set(columns_of_table)
            columns_array = ",".join(str(element) for element in unique_columns)
            algebra[index] = "π " + columns_array + "(" + term + ")"
    return algebra


def tables_from_algebra(algebra):
    tables = []
    for term in algebra:
        if is_table_term(term):
            tables.append(get_table(term))
    return tables


def columns_to_select(algebra):
    columns = []
    for term in algebra:
        if term.startswith("π "):
            term = term.replace("π ", "")
            projection_columns = term.split(",")

            for column in projection_columns:
                if "." in column:
                    column = column.split(".")[1].lower()
                columns.append(column)

        elif term.startswith("⋈"):
            term = term.replace("⋈ ", "").replace("(", "").replace(")", "")
            join_columns = term.split(" = ")
            for column in join_columns:
                column = column.split(".")[1].lower()
                columns.append(column)

    return columns


def table_columns(tables, columns):
    selected_table_columns = {}

    for table in tables:
        selected_table_columns[table] = []

    for column in columns:
        table = schema.table_of_column(column.lower(), tables)
        selected_table_columns[table].append(column)

    return selected_table_columns


def is_table_term(string):
    return string.startswith("σ") or string.isalpha()


def get_table(string):
    if string.isalpha():
        return string

    if string.startswith("σ"):
        pattern = r"\((\w+)\)"
        matches = re.findall(pattern, string)
        return matches[0]
