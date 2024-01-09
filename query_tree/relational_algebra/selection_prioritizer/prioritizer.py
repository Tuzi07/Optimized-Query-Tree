import re


def add_new_condition(term, new_condition):
    conditions = conditions_from_term(term)
    table = table_from_term(term)

    conditions_by_priority = [[] for _ in range(5)]

    for condition in conditions:
        priority = condition_priority(condition)
        conditions_by_priority[priority].append(condition)

    new_priority = condition_priority(new_condition)
    conditions_by_priority[new_priority].append(new_condition)

    new_term = table

    for priority in range(5):
        if len(conditions_by_priority[priority]) > 0:
            for condition in conditions_by_priority[priority]:
                new_term = condition + "(" + new_term + ")"

    return "σ " + new_term


def conditions_from_term(term):
    pattern = r"σ.*?\("
    substrings = re.findall(pattern, term)
    for index, substring in enumerate(substrings):
        substrings[index] = substring[:-1].strip()
    return substrings


def table_from_term(term):
    pattern = r"\((\w+)\)"

    matches = re.findall(pattern, term)
    return matches[0]


# MOST RESTRICTIVE
#
# 0 -> =
# 1 -> IN
# 2 -> >, <, <=, >=
# 3 -> Not In
# 4 -> <>
#
# LEAST RESTRICTIVE
def condition_priority(condition):
    if " not in " in condition:
        return 3
    elif " in " in condition:
        return 1
    elif "<>" in condition:
        return 4
    elif ">" in condition or "<" in condition:
        return 2
    elif "=" in condition:
        return 0
