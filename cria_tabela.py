# %%
#importar as funcoes necessarias

import mysql.connector
from mysql.connector import errorcode
import config # arquivo que carrega as credenciais de acesso ao banco de dados

# %%
#Cria conexão com o BD
cnx = mysql.connector.connect(user=config.user,
        host=config.host,
        password=config.passwd)
    
cursor = cnx.cursor()

# %%
#Definização do BD com as tabelas, tipos e restrições
DB_NAME = "SEU_BANCO_DE_DADOS"

TABLES = {}
TABLES['produto'] = (
    "CREATE TABLE `produto` ("
    "  `descricao` varchar(50) NOT NULL,"
    "  `cod_barras` int(10) NOT NULL,"
    "  `preco_venda` float(10) NOT NULL,"
    "  PRIMARY KEY (`descricao`), UNIQUE KEY `cod_barras` (`cod_barras`)"
    ") ENGINE=InnoDB")

TABLES['compra'] = (
    "CREATE TABLE `compra` ("
    "  `id_compra` int(11) NOT NULL AUTO_INCREMENT,"
    "  `data_compra` date NOT NULL,"
    "  `dta_validade` date NOT NULL,"
    "  `qtdade` int(10) NOT NULL,"
    "  `descricao` varchar(50) NOT NULL,"
    "  `preco_compra` float(6) NOT NULL,"
    "  `cod_barras` int(10) NOT NULL,"
    "  `id_fornecedor` int(10) NOT NULL,"
    "  `lote` varchar(10) NOT NULL,"
    "   KEY `descricao` (`descricao`),"
    "   KEY `cod_barras` (`cod_barras`),"
    "   PRIMARY KEY (`id_compra`), KEY `id_compra` (`id_compra`),"
    "   CONSTRAINT `compra_ibfk_1` FOREIGN KEY (`descricao`)"
    "      REFERENCES `produto` (`descricao`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

TABLES['estoque'] = (
    "CREATE TABLE `estoque` ("
    "  `descricao` varchar(50) NOT NULL,"
    "  `cod_barras` int(10) NOT NULL,"
    "  `qtdade` int(10) NOT NULL,"
    "  `dta_validade` date NOT NULL,"
    "  `localizador` varchar(10) NOT NULL,"
    "  `lote` varchar(10) NOT NULL,"
    "  `id_compra` int(11),"
    "   KEY `cod_barras` (`cod_barras`),"
    "   KEY `id_compra` (`id_compra`),"
    "   PRIMARY KEY (`descricao`), KEY `descricao` (`descricao`),"
    "   CONSTRAINT `estoque_ibfk_1` FOREIGN KEY (`descricao`) "
    "      REFERENCES `produto` (`descricao`) ON DELETE CASCADE,"
    "   CONSTRAINT `estoque_ibfk_2` FOREIGN KEY (`id_compra`) "
    "      REFERENCES `compra` (`id_compra`) ON DELETE CASCADE"
    ")  ENGINE=InnoDB")

TABLES['venda'] = (
    "CREATE TABLE `venda` ("
    "  `id_compra` int(11),"
    "  `id_venda` int(11) NOT NULL AUTO_INCREMENT,"
    "  `data` date NOT NULL,"
    "  `qtdade` int(10) NOT NULL,"
    "  `preco_venda` float(10) NOT NULL,"
    "  `descricao` varchar(50) NOT NULL,"
    "  `cod_barras` int(10) NOT NULL,"
    "  `valor_total` float(10) NOT NULL,"
    "   KEY `id_compra` (`id_compra`),"
    "   KEY `descricao` (`descricao`),"
    "   KEY `cod_barras` (`cod_barras`),"
    "   KEY `preco_venda` (`preco_venda`),"
    "  PRIMARY KEY (`id_venda`), KEY `emp_no` (`id_venda`),"
    "  CONSTRAINT `venda_ibfk_1` FOREIGN KEY (`id_compra`) "
    "     REFERENCES `compra` (`id_compra`) ON DELETE CASCADE,"
    "  CONSTRAINT `sale_ibfk_2` FOREIGN KEY (`descricao`) "
    "     REFERENCES `produto` (`descricao`) ON DELETE CASCADE" 
    ") ENGINE=InnoDB")

TABLES['fluxo_cliente'] = (
    "  CREATE TABLE `fluxo_cliente` ("
    "  `datetime` timestamp NOT NULL,"
    "  `qt_entrada` int(10) NOT NULL,"
    "  `qt_saida` int(10) NOT NULL,"
    "  PRIMARY KEY (`datetime`), KEY `datetime` (`datetime`)"
    ") ENGINE=InnoDB")

TABLES['financeiro'] = (
    "CREATE TABLE `financeiro` ("
    "  `id_compra` int(11) NOT NULL,"
    "  `id_venda` int(11) NOT NULL,"
    "  `despesa` float(10),"
    "  `valor_vendas` float NOT NULL,"
    "   KEY `id_compra` (`id_compra`),"
    "   KEY `id_venda` (`id_venda`),"
    "  PRIMARY KEY (`id_compra`,`id_venda`),"
    "  CONSTRAINT `financial_ibfk_1` FOREIGN KEY (`id_compra`) "
    "    REFERENCES `compra` (`id_compra`) ON DELETE CASCADE,"
    "  CONSTRAINT `financial_ibfk_2` FOREIGN KEY (`id_venda`) "
    "    REFERENCES `venda` (`id_venda`) ON DELETE CASCADE"
    ") ENGINE=InnoDB")

# %%
#função para criar um novo banco de dados, depois da criação do novo a cursor é conectado ao novo banco agora criado
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Falha na criacao do banco de dados: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("banco de dados {} nao existente.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("banco de dados {} criado com sucesso .".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)

# %%
#linhas de código que depois de criado e conectado ao novo banco de dados faz a criação das tabelas em acordo com a especificação do dicionário
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

cursor.close()
cnx.close()


