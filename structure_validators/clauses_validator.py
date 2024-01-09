import re
from structure_validators.clause_validators import (
    from_validator,
    join_on_validator,
    select_validator,
    where_validator,
)

keywords = ["SELECT", "FROM", "WHERE", "JOIN"]


def validate(query):
    sql_tuples = extract_sql_tuples(query)
    for keyword, expression in sql_tuples:
        if keyword == "SELECT":
            if not select_validator.is_valid_select(expression):
                return False
        elif keyword == "FROM":
            if not from_validator.is_valid_from(expression):
                return False
        elif keyword == "JOIN":
            if not join_on_validator.is_valid_join_on(expression):
                return False
        elif keyword == "WHERE":
            if not where_validator.is_valid_where("WHERE " + expression):
                return False
    return True


def extract_sql_tuples(sql_query):
    keyword_expression_tuples = []
    keyword = ""
    expression = ""

    sql_query = remove_extra_whitespace(sql_query)
    words = sql_query.split()

    for word in words:
        if not is_keyword(word):
            expression += word + " "
        else:
            if should_append(keyword, expression):
                keyword_expression_tuples.append((keyword.upper(), expression.strip()))
                expression = ""
            keyword = word

    if should_append(keyword, expression):
        keyword_expression_tuples.append((keyword.upper(), expression.strip()))

    return keyword_expression_tuples


def remove_extra_whitespace(string):
    return re.sub(r"\s+", " ", string).strip()


def is_keyword(word):
    return word.upper() in keywords


def should_append(keyword, expression):
    return keyword != "" or expression != ""
