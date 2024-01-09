import re


def is_valid_select(expression):
    expression = re.sub(r"\s+", "", expression)

    pattern = r"^(?!.*,$)(?!,$)[^,]+(\.\*|\.[^,]+)*(,[^,]+(\.\*|\.[^,]+)*)*$"
    if re.match(pattern, expression):
        return True
    else:
        return False
