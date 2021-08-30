#FRONTEND

Requisitos:
	NodeJs 14.17.3
	Vue@2.6.14

Setup do projeto:
	Executar o comando 'npm install' para baixar as dependências
	
Para realizar o build:
	npm run build

Iniciar servidor:
	npm run serve

Acessar localhost:8080

#BACKEND	

Requisitos: MySql 8.0.26, Python 3.9.6

Baixar as dependências do Python:
	pip install -r requirements.txt

Recriar a base de dados mySQL:
	mysqldump [options] > dump.sql

Para levantar o servidor:
	uvicorn sql_app.main:app --reload


Testes unitários: 
	pytest-v 

#DOCUMENTACAO

http://127.0.0.1:8000/docs