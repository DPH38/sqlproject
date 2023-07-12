README

# Descrição do Projeto
Este é um projeto em Python para gerenciamento de um sistema de controle de estoque, vendas e compras. Ele inclui a criação de um banco de dados em MySQL, com tabelas correspondentes a produtos, compras, vendas, estoque, fluxo de clientes e finanças.

# Configuração e Dependências
Este projeto requer uma instalação de Python 3.7 ou superior e as seguintes bibliotecas:

mysql-connector-python
A configuração do banco de dados MySQL (nome de usuário, host, senha) deve ser definida no arquivo config.py. Exemplo de como esse arquivo pode ser estruturado:

user = 'your_mysql_username'
host = 'localhost'
passwd = 'your_mysql_password'

# Como rodar o código

Certifique-se de que o MySQL Server está instalado e rodando em sua máquina.
Configure o arquivo config.py com suas credenciais MySQL.
Execute o script Python para criar e preencher o banco de dados.

Copy code

´python3 seu_script.py´


Estrutura do Banco de Dados
O banco de dados "ESW2023_E3_Ponta_Pedra_Diego" inclui as seguintes tabelas:

produto: armazena a descrição do produto, código de barras e preço de venda.
compra: armazena detalhes sobre compras feitas, incluindo o ID da compra, data da compra, data de validade, quantidade, descrição do produto, preço de compra, código de barras, ID do fornecedor e número do lote.
estoque: armazena o estado atual do estoque, incluindo a descrição do produto, código de barras, quantidade em estoque, data de validade, localizador, número do lote e ID da compra.
venda: registra detalhes sobre as vendas, incluindo ID da venda, data da venda, quantidade, preço de venda, descrição do produto, código de barras e valor total da venda.
fluxo_cliente: registra a entrada e saída de clientes em um determinado horário.
financeiro: registra detalhes financeiros, incluindo IDs de compra e venda, despesa e valor total de vendas.
Cada tabela é criada com chaves primárias e estrangeiras apropriadas, permitindo consultas complexas e relacionais.

Lembre-se: Este é um exemplo simples e direto para gerenciamento de um sistema de controle de estoque. Para um sistema mais robusto e seguro, seria necessário implementar funções de segurança, validação de dados, manipulação de erros e uma interface de usuário adequada.
