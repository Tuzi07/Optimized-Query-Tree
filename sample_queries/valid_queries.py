valid_queries = [
    "SELECT  name ,  age  FROM  users  WHERE  age  >  18  JOIN  addresses  ON  users.id  =  addresses.user_id ",
    "Select nome, datanascimento, descricao, saldoinicial \nfrom usuario\njoin contas on usuario.idUsuario = contas.Usuario_idUsuario\nwhere saldoinicial >=235 and uf ='ce' and cep <> '62930000';",
    "Select idusuario, nome, datanascimento, descricao, saldoinicial, UF, Descriçao\nfrom usuario\njoin contas on usuario.idUsuario = contas.Usuario_idUsuario\njoin tipoconta on tipoconta.idTipoConta = contas.TipoConta_idTipoConta\nwhere saldoinicial < 3000 and uf = 'ce' and Descriçao <> 'Conta Corrente' and idusuario > 3;",
    "SELECT idUsuario, Nome FROM Usuario;",
    "SELECT idTipoConta, Descriçao FROM TipoConta;",
    "SELECT idTipoMovimento, DescMovimentacao FROM TipoMovimento;",
    "SELECT idConta, Descricao, TipoConta_idTipoConta, Usuario_idUsuario, SaldoInicial, Usuario.Nome FROM Contas \nJOIN Usuario ON Contas.Usuario_idUsuario = Usuario.idUsuario;",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor, Contas.Descricao FROM Movimentacao\nJOIN Contas ON Movimentacao.Contas_idConta = Contas.idConta;",
    "SELECT idCategoria, DescCategoria, Movimentacao.Descricao FROM Categoria \nJOIN Movimentacao ON Categoria.idCategoria = Movimentacao.Categoria_idCategoria;",
    "SELECT idConta, Descricao, TipoConta_idTipoConta, Usuario_idUsuario, SaldoInicial, TipoMovimento.DescMovimentacao FROM Contas \nJOIN TipoMovimento ON Contas.TipoConta_idTipoConta = TipoMovimento.idTipoMovimento;",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor, Contas.idConta FROM Movimentacao \nJOIN Contas ON Movimentacao.Contas_idConta = Contas.idConta;",
    "SELECT idUsuario, Nome FROM Usuario WHERE UF = 'SP';",
    "SELECT idConta, Descricao, TipoConta_idTipoConta, Usuario_idUsuario, SaldoInicial FROM Contas WHERE SaldoInicial >= 1000;",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor FROM Movimentacao WHERE DataMovimentacao > '2022-01-01';",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor FROM Movimentacao WHERE Valor < 0;",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor FROM Movimentacao WHERE TipoMovimento_idTipoMovimento = 2;",
    "SELECT idConta, Descricao, TipoConta_idTipoConta, Usuario_idUsuario, SaldoInicial FROM Contas\nJOIN Usuario ON Contas.Usuario_idUsuario = Usuario.idUsuario\nWHERE Contas.SaldoInicial >= 1000 AND Usuario.Nome = 'John';",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor FROM Movimentacao WHERE DataMovimentacao < '2020-01-01';",
    "SELECT idMovimentacao, DataMovimentacao, Descricao, TipoMovimento_idTipoMovimento, Categoria_idCategoria, Contas_idConta, Valor FROM Movimentacao WHERE Valor > 500 AND Valor < -500;",
    "SELECT \n    Usuario.Nome\nFROM \n    Usuario \n    JOIN Contas ON (Usuario.idUsuario = Contas.Usuario_idUsuario)",
    "SELECT Nome, Logradouro, Numero, Bairro, CEP, UF, DataNascimento\nFROM Usuario\nJOIN Contas ON Usuario.idUsuario = Contas.Usuario_idUsuario\nJOIN TipoConta ON Contas.TipoConta_idTipoConta = TipoConta.idTipoConta\nWHERE TipoConta.Descriçao IN ('Savings', 'Checking');",
    "SELECT Nome, Logradouro, Numero, Bairro, CEP, UF, DataNascimento\nFROM Usuario\nJOIN Contas ON Usuario.idUsuario = Contas.Usuario_idUsuario\nJOIN TipoConta ON Contas.TipoConta_idTipoConta = TipoConta.idTipoConta\nWHERE TipoConta.Descriçao NOT IN ('Credit');",
]