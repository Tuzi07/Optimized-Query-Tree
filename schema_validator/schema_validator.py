from schema_validator.name_extractors import (
    from_extractor,
    join_on_extractor,
    select_extractor,
    where_extractor,
)
from database_schema import schema

from structure_validators import clauses_validator


def validate(query):
    sql_tuples = clauses_validator.extract_sql_tuples(query)

    tables = set()
    columns = set()

    for keyword, expression in sql_tuples:
        if keyword == "SELECT":
            if not select_extractor.is_valid_select(expression):
                return False
            select_columns = select_extractor.columns(expression)
            columns.update(select_columns)

        elif keyword == "FROM":
            if not from_extractor.is_valid_from(expression):
                return False
            from_table = from_extractor.table(expression)
            tables.add(from_table)

        elif keyword == "JOIN":
            if not join_on_extractor.is_valid_join_on(expression):
                return False
            join_tables, join_columns = join_on_extractor.tables_and_columns(expression)
            tables.update(join_tables)
            columns.update(join_columns)

        elif keyword == "WHERE":
            if not where_extractor.is_valid_where(expression):
                return False
            where_columns = where_extractor.columns(expression)
            columns.update(where_columns)

    possible_columns = []
    for table in tables:
        table = table.lower()
        possible_columns = possible_columns + schema.table_columns[table]

    for column in columns:
        column = column.lower()
        if "." in column:
            column = column.split(".")[1].lower()

        if column not in possible_columns:
            return False

    return True


def tables_and_columns(query):
    sql_tuples = clauses_validator.extract_sql_tuples(query)

    tables = set()
    columns = set()

    for keyword, expression in sql_tuples:
        if keyword == "SELECT":
            select_columns = select_extractor.columns(expression)
            columns.update(select_columns)

        elif keyword == "FROM":
            from_table = from_extractor.table(expression)
            tables.add(from_table)

        elif keyword == "JOIN":
            join_tables, join_columns = join_on_extractor.tables_and_columns(expression)
            tables.update(join_tables)
            columns.update(join_columns)

        elif keyword == "WHERE":
            where_columns = where_extractor.columns(expression)
            columns.update(where_columns)

    return tables, columns


def tables_of_query(query):
    sql_tuples = clauses_validator.extract_sql_tuples(query)

    tables = set()

    for keyword, expression in sql_tuples:
        if keyword == "FROM":
            from_table = from_extractor.table(expression)
            tables.add(from_table)

        elif keyword == "JOIN":
            join_tables, _ = join_on_extractor.tables_and_columns(expression)
            tables.update(join_tables)

    return tables
