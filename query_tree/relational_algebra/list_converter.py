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

    ra_expression = []
    current = "π "

    for attribute in select_clause[1:]:
        current += attribute

    ra_expression.append(current)
    current = ""

    if len(where_clause) > 0:
        current += "σ"
        for condition in where_clause[1:]:
            current += " " + condition

        ra_expression.append(current)
        current = ""

    table = from_clause[1]
    current = table

    ra_expression.append(current)
    current = ""

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
                ra_expression.append(current)
                ra_expression.append(table)
                current = ""
                next_is_table = True
                next_is_condition = False

            elif substring == "on":
                current += "⋈"
                next_is_condition = True

            elif next_is_condition:
                current += " " + substring

        ra_expression.append(current)
        ra_expression.append(table)

    return ra_expression
