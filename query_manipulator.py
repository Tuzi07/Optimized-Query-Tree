from structure_validators import (
    clauses_validator,
    keyword_order_validator,
)
from schema_validator import schema_validator

from query_tree.tree_creator import QueryTree
from query_tree import tree_visualizer
from query_tree.relational_algebra import string_converter


def validate_query(query):
    is_keyword_order_valid = keyword_order_validator.is_query_valid(query)
    if not is_keyword_order_valid:
        return "Invalid Keyword Order"

    is_syntax_valid = clauses_validator.validate(query)
    if not is_syntax_valid:
        return "Invalid Syntax"

    are_names_valid = schema_validator.validate(query)
    if not are_names_valid:
        return "Invalid Column or Table Name"

    return "Valid Query!"


def relational_algebra(query):
    return string_converter.sql_to_relational_algebra(query)


def build_and_show_tree(query):
    sql_tree = QueryTree(query)

    tree_visualizer.show_tree(sql_tree)

    sql_tree.number_execution_order()
    tree_visualizer.show_tree(sql_tree)
