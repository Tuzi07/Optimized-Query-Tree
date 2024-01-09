import re


def is_valid_where(expression):
    where_tuples = extract_where_tuples(expression)
    for _, condition in where_tuples:
        if not valid_condition(condition):
            return False
    return True


def extract_where_tuples(conditions):
    keyword_expression_tuples = []
    keyword = ""
    expression = ""

    conditions = remove_extra_whitespace(conditions)
    words = conditions.split()

    for word in words:
        if not (word.upper() in ["WHERE", "AND"]):
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


def should_append(keyword, expression):
    return keyword != "" or expression != ""


def valid_condition(condition):
    pattern = r"^(([a-zA-Z_çÇãÃ]+(\.[a-zA-Z_çÇãÃ]+)?)\s*((=|<>|>|<|>=|<=)\s*('[^']*'|-?[0-9]+))|([a-zA-Z_çÇãÃ]+(\.[a-zA-Z_çÇãÃ]+)?\s+(IN|NOT\s+IN)\s*\(\s*'[^']*'(,\s*'[^']*')*\s*\)))\s*;?$"
    if re.match(pattern, condition):
        return True
    else:
        return False
