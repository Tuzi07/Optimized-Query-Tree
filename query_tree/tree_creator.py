import networkx

from query_tree.relational_algebra import (
    column_reducer,
    tuple_reducer,
    list_converter,
)


class QueryTree:
    def __init__(self, query):
        self.algebra = self.optimized_relational_algebra(query)
        self.tree = networkx.DiGraph()
        self.root = None
        self.build_tree_from_algebra()

    def optimized_relational_algebra(self, query):
        algebra = list_converter.sql_to_relational_algebra(query)
        algebra = tuple_reducer.reduce_tuples(algebra)
        algebra = column_reducer.reduce_columns(algebra)
        return algebra

    def build_tree_from_algebra(self):
        self.root = self.algebra[0]
        del self.algebra[0]

        terms_left = len(self.algebra)
        last_join_used = 0

        if terms_left == 1:
            if self.algebra[0].startswith("π"):
                operations = self.algebra[0].replace(")", "").split("(")
                operations[0] = self.root
                for i in range(1, len(operations)):
                    self.tree.add_edge(operations[i - 1], operations[i])

        else:
            while terms_left != 1:
                current_join = 0
                for index, term in enumerate(self.algebra):
                    if term.startswith("⋈"):
                        current_join += 1
                        if current_join > last_join_used:
                            self.link_neighbors(index)

                            last_join_used += 1
                            terms_left = len(self.algebra)
                            break

            self.tree.add_edge(self.root, self.algebra[0])

    def link_neighbors(self, index):
        if self.algebra[index - 1].startswith("π"):
            self.unpack_projection(index - 1)

        if self.algebra[index + 1].startswith("π"):
            self.unpack_projection(index + 1)

        self.tree.add_edge(self.algebra[index], self.algebra[index - 1])
        self.tree.add_edge(self.algebra[index], self.algebra[index + 1])

        del self.algebra[index + 1]
        del self.algebra[index - 1]

    def unpack_projection(self, index):
        operations = self.algebra[index].replace(")", "").split("(")

        for i in range(1, len(operations)):
            self.tree.add_edge(operations[i - 1], operations[i])

        self.algebra[index] = operations[0]

    def number_execution_order(self):
        operation_number = self.tree.number_of_nodes()
        visited = set()
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                neighbors = list(self.tree.neighbors(node))
                stack.extend(neighbors)
                new_name = f"{operation_number}) {node}"
                if node == self.root:
                    self.root = new_name
                self.tree = networkx.relabel_nodes(
                    self.tree, {node: new_name}, copy=False
                )
                operation_number -= 1
