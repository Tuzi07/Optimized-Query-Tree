import re

from database_schema import schema


def is_valid_join_on(expression):
    before, after = re.split(r"\b[oO][nN]\b", expression)
    return is_valid_join(before) and is_valid_on(after)


def is_valid_join(expression):
    expression = re.sub(r"\s+", "", expression)
    return expression.lower() in schema.tables


def is_valid_on(expression):
    expression = re.sub(r"\s+", "", expression)
    expression = expression.replace(";", "")
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")

    left_side, right_side = expression.split("=")

    left_table, left_column = left_side.split(".")
    right_table, right_column = right_side.split(".")

    left_table = left_table.lower()
    right_table = right_table.lower()
    left_column = left_column.lower()
    right_column = right_column.lower()

    if left_table in schema.tables:
        if left_column not in schema.table_columns[left_table]:
            return False
    else:
        return False

    if right_table in schema.tables:
        if right_column not in schema.table_columns[right_table]:
            return False
    else:
        return False

    return True


def tables_and_columns(expression):
    before, after = re.split(r"\b[oO][nN]\b", expression)

    table = join_table(before)
    on_tables, columns = on_tables_and_columns(after)

    tables = list(set([table] + on_tables))
    return tables, columns


def join_table(expression):
    expression = re.sub(r"\s+", "", expression)
    return expression


def on_tables_and_columns(expression):
    expression = re.sub(r"\s+", "", expression)
    expression = expression.replace(";", "")
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")

    left_side, right_side = expression.split("=")

    left_table, left_column = left_side.split(".")
    right_table, right_column = right_side.split(".")

    tables = [left_table, right_table]
    columns = [left_column, right_column]

    return tables, columns
