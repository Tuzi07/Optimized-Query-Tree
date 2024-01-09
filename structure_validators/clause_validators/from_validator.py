import re


def is_valid_from(expression):
    expression = re.sub(r"\s+", "", expression)

    pattern = r"^[A-Za-z]+;?$"
    if re.match(pattern, expression):
        return True
    else:
        return False
