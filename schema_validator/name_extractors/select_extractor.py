import re

from database_schema import schema


def is_valid_select(expression):
    col = columns(expression)
    for column in col:
        if not schema.is_column(column):
            return False
    return True


def columns(expression):
    expression = re.sub(r"\s+", "", expression)
    return expression.split(",")
