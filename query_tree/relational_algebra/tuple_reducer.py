import re

from database_schema import schema
from query_tree.relational_algebra.selection_prioritizer import prioritizer


def reduce_tuples(relational_algebra):
    tables = tables_from_algebra(relational_algebra)
    table_indexes = index_of_tables(relational_algebra)
    if relational_algebra[1].startswith("σ"):
        conditions = conditions_of_selection(relational_algebra[1])
        for condition in conditions:
            condition = handle_in_and_not_in(condition)
            column = extract_column(condition)
            table = schema.table_of_column(column, tables)
            table_index = table_indexes[table]
            term = relational_algebra[table_index]
            if term != table:
                relational_algebra[table_index] = prioritizer.add_new_condition(
                    term, condition
                )
            else:
                relational_algebra[table_index] = "σ " + condition + "(" + term + ")"
        del relational_algebra[1]

    return relational_algebra


def conditions_of_selection(selection):
    selection = selection.replace("σ ", "")
    selection = selection.lower()
    return selection.split(" and ")


def tables_from_algebra(algebra):
    tables = []
    for term in algebra:
        if is_table(term):
            tables.append(term)
    return tables


def index_of_tables(relational_algebra):
    table_index = {}
    for index, term in enumerate(relational_algebra):
        if is_table(term):
            table_index[term] = index
    return table_index


def is_table(term):
    return term in schema.tables


def extract_column(condition):
    pattern = r"^[A-Za-z.çã_]+"
    match = re.search(pattern, condition)

    column = match.group(0)
    if "." in column:
        column = column.split(".")[1]
    return column


def handle_in_and_not_in(condition):
    return condition.replace("(", "[").replace(")", "]")
