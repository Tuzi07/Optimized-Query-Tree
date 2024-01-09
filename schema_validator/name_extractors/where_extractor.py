import re

from structure_validators.clause_validators import where_validator
from database_schema import schema


def is_valid_where(expression):
    where_conditions = where_validator.extract_where_tuples(expression)
    for _, condition in where_conditions:
        if not is_valid_condition(condition):
            return False
    return True


def is_valid_condition(condition):
    column = extract_column(condition)
    return schema.is_column(column)


def extract_column(condition):
    if has_not_in(condition):
        index = condition.lower().find(" not in ")
        return condition[:index]

    if has_in(condition):
        index = condition.lower().find(" in ")
        return condition[:index]

    pattern = r"^([^=<>]+)"
    column = re.search(pattern, condition).group(1).strip()
    return column


def has_not_in(condition):
    index = condition.lower().find(" not in ")
    return index != -1


def has_in(condition):
    index = condition.lower().find(" in ")
    return index != -1


def columns(expression):
    columns = set()
    where_conditions = where_validator.extract_where_tuples(expression)
    for _, condition in where_conditions:
        column = extract_column(condition)
        columns.add(column)
    return list(columns)
