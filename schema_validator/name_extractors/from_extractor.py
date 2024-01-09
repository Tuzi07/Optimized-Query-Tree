import re

from database_schema import schema


def is_valid_from(expression):
    return table(expression).lower() in schema.tables


def table(expression):
    expression = re.sub(r"\s+", "", expression)
    return expression.replace(";", "")
