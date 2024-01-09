def sql_to_relational_algebra(query):
    query = query.lower()
    query = query.replace(";", "")
    query_parts = query.split()

    select_clause = []
    from_clause = []
    where_clause = []
    join_clause = []

    is_select = False
    is_from = False
    is_where = False
    is_join = False

    for part in query_parts:
        if part == "select":
            is_select = True
        elif part == "from":
            is_select = False
            is_from = True
        elif part == "where":
            is_from = False
            is_where = True
        elif part == "join":
            is_from = False
            is_where = False
            is_join = True

        if is_select:
            select_clause.append(part)
        elif is_from:
            from_clause.append(part)
        elif is_where:
            where_clause.append(part)
        elif is_join:
            join_clause.append(part)

    ra_expression = "π "

    for attribute in select_clause[1:]:
        ra_expression += attribute

    if len(where_clause) > 0:
        ra_expression += " (σ"
        for condition in where_clause[1:]:
            ra_expression += " " + condition
        ra_expression += " ("

    if ra_expression[-1] != "(":
        ra_expression += " "

    table = from_clause[1]
    ra_expression += table

    if len(join_clause) > 0:
        table = join_clause[1]
        next_is_table = False
        next_is_condition = False

        for substring in join_clause[2:]:
            if next_is_table:
                table = substring
                next_is_table = False
                next_is_condition = False

            elif substring == "join":
                ra_expression += " " + table
                next_is_table = True
                next_is_condition = False

            elif substring == "on":
                ra_expression += " ⋈"
                next_is_condition = True

            elif next_is_condition:
                ra_expression += " " + substring

        ra_expression += " " + table

    if len(where_clause) > 0:
        ra_expression += "))"

    return ra_expression
