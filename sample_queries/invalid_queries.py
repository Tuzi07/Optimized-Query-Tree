invalid_queries = [
    "SELECT idUsuario FROM Usuario; SELECT",
    "idUsuario FROM Usuario; SELECT",
    "SELECT SELECT idUsuario FROM Usuario; SELECT",
    "SELECT idUsuario FROM Usuario WHERE UF 'SP'",
    "SELECT idConta FROM Contas WHERE SaldoInicial >=",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor, Usuario.Nome FROM Movimentacao \nJOIN Usuario ON Movimentacao.Usuario_idUsuario = Usuario.idUsuario;",
    "SELECT idMovimentacao FROM Movimentacao WHERE Valor > 5000 AND NomeColunaInexistente = 'valor alto'",
    "SELECT , SaldoInicial FROM Contas WHERE SaldoInicial >= 1000",
    "SELECT idConta, Descricao, , SaldoInicial FROM Contas WHERE SaldoInicial >= 1000",
    "SELECT idConta, Descircao, SaldoInicial FROM Contas WHERE SaldoInicial >= 1000",
    "SELECT idConta FROM WHERE SaldoInicial >= 1000",
    "SELECT idConta FROM Contaz WHERE SaldoInicial >= 1000",
    "SELECT idConta FROM Contas, Usuario WHERE SaldoInicial >= 1000",
    "SELECT idConta FROM Contas JOIN Usuario ON WHERE SaldoInicial >= 1000",
    "SELECT idConta FROM Contas JOIN Usuarios ON Contas.Usuario_idUsario = Usuarios.idUsario WHERE SaldoInicial >= 1000",
    "SELECT \n    Usuario.Nome\nFROM \n    Usuario \n    JOIN Contas ON (Usuario.idUsuario = Contas.Usuario_idUsuario))",
    "SELECT Nome, Logradouro, Numero, Bairro, CEP, UF, DataNascimento\nFROM Usuario\nWHERE idUsuario IN;",
    "SELECT idUsuario, Nome, Logradouro, Numero, Bairro, CEP, UF, DataNascimento\nFROM Usuario\nWHERE idUsuario NOT IN idConta;",
]
