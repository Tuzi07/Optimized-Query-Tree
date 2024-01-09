import re


def is_query_valid(query):
    is_valid = True
    keywords = extract_keywords(query)
    if len(keywords) < 2:
        return False

    for index, keyword in enumerate(keywords):
        if index == 0 and keyword.upper() != "SELECT":
            is_valid = False
        elif index == 1 and keyword.upper() != "FROM":
            is_valid = False
        elif index > 1:
            if keyword.upper() not in ("JOIN", "WHERE"):
                is_valid = False
    return is_valid


def extract_keywords(sql_query):
    keywords = []

    sql_query = remove_extra_whitespace(sql_query)
    words = sql_query.split()

    for word in words:
        if is_keyword(word):
            keywords.append(word)

    return keywords


def remove_extra_whitespace(string):
    return re.sub(r"\s+", " ", string).strip()


def is_keyword(word):
    return word.upper() in ["SELECT", "FROM", "WHERE", "JOIN"]
