# Optimized Query Tree

Projeto para estudar processamento e otimização de consultas SQL DQL.

https://github.com/Tuzi07/Optimized-Query-Tree/assets/37273687/4a311ea0-db9d-47d8-82cb-4c11ccf8a58e

https://github.com/Tuzi07/Optimized-Query-Tree/assets/37273687/6f4c1343-4adb-4c00-81b7-9383b5bed878

A query é transformada em uma árvore de consulta expressa em álgebra relacional.

Em seguida, aplicam-se heurísticas para converter a árvore em uma árvore de consulta equivalente, mas que seja mais eficiente na sua execução.

Finalmente é dada a ordem de processamento das consultas.

Validações:
- keyword order
- syntax
- table names and column names

Heurísticas de otimização:
- aplicar primeiro operações que reduzem o tamanho dos resultados intermediários (isto é, operações de seleção, que reduzem o número de tuplas, e operações de projeção, que reduzem o número de atributos)
- aplicar primeiro operações mais restritivas (por exemplo, uma operação de = será feita antes de uma operação de >)
