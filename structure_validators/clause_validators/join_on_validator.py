import re


def is_valid_join_on(expression):
    if has_on(expression):
        pattern = r"\b[oO][nN]\b"
        before, after = re.split(pattern, expression)
        if not valid_join(before):
            return False
        if not valid_on(after):
            return False
        return True
    else:
        return False


def has_on(expression):
    pattern = re.compile(r"\b[oO][nN]\b")
    return pattern.search(expression)


def valid_join(expression):
    expression = re.sub(r"\s+", "", expression)

    pattern = r"^[A-Za-z]+$"
    if re.match(pattern, expression):
        return True
    else:
        return False


def valid_on(expression):
    expression = re.sub(r"\s+", "", expression)

    non_parentheses_expression = "".join(
        char for char in expression if char not in "()"
    )
    pattern = r"^\w+\.\w+=\w+\.\w+;?$"

    parentheses_expression = "".join(char for char in expression if char in "()")

    if re.match(pattern, non_parentheses_expression) and is_valid_parentheses(
        parentheses_expression
    ):
        return True
    else:
        return False


def is_valid_parentheses(s):
    pattern = re.compile(r"\(\)")
    while pattern.search(s):
        s = pattern.sub("", s)
    return not s
