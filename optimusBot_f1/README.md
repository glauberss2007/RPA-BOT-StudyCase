## F1 BOT
![image](https://user-images.githubusercontent.com/22028539/123629107-3ff0d900-d7ea-11eb-93d0-317eb5da44a9.png)
A FIA (Federação Internacional de Automobilismo) deseja construir um banco de dados sobre o campeonato de Fórmula 1. 

Para isso contratou uma consultoria de software e você foi alocado no projeto como analista de sistemas responsável pelo projeto conceitual do banco de dados.

Após um levantamento de requisitos você identificou as informações relevantes abaixo:
- Os contrutores contratam pilotos
- Os construtores contratam fabricantes de motores
- Os circuitos recebem os grandes prêmios
- Os grandes prêmios possuem a seguinte pontuação:
1°	2°	3°	4°	5°	6°	7°	8°	9°	10°	
25	18	15	12	10	8	6	4	2	1

Caso o piloto faça a volta mais rápida e termine entre os 10 primeiros, o mesmo ganha um ponto adicional.

O pódio é formado pelos 3 primeiros colocados.
![image](https://user-images.githubusercontent.com/22028539/123629214-69116980-d7ea-11eb-90a5-4a1e8b102c52.png)

Cada grande prêmio possui um treino classificatório, que decide o Grid de largada.

Dadas as informações acima, pede-se:
1 - Modelar o banco de dados e criar um MER.

2 - Criar o banco de dados conforme o MER (tabelas, chaves, etc.).

3 - Criar um projeto de RPA que realiza o carregamento destes dados, conforme orientações abaixo:
	Usar a fonte API para os dados de resultados.
	Usar a fonte arquivo CSV presente no FTP para os dados de pilotos.
	Usar o banco de dados SQL Server para os dados de circuitos.

4 - Criar consultas SQL que retornem os seguintes resultados
		Top 10 pilotos com mais poles (primeiro lugar nos treinos classificatórios).
		Top 10 circuitos com mais grandes prêmios.
		Quantidade de grandes prêmios vencidos por Construtoras.
		Quantidade de pódios por piloto.
		Média de pontos por temporada por construtora.
	
Fontes:
API - https://documenter.getpostman.com/view/11586746/SztEa7bL

CSV - Servidor FTP: ip do server 
	  Usuário FTP: nome do usuário
	  Senha FTP: ***
	  Nome do arquivo: pilotos.csv

Banco de Dados:
	  SGBD: SQL Server
	  Servidor: ip do server 
	  Porta: 1481
	  usuário: nome do usuário
	  Senha: **


Dados de Pilotos (FTP)
Server: 135.181.213.93
Port: 4022
User: ftpusr.rpa
Password: &F#hFe8GM8IAmfou
File: drivers.csv

Dados de Circuitos (SQL Server)
Server: 135.181.213.93
Port: 1481
Database: db_TurmaRPA
User: usr.turma.rpa
Pass: Z8@cDi9wgi#eq7&q
Tabela: circuits
