import sqlite3

# conexão com o banco de dados 

conn =sqlite3.connect('alunos_python.db')

#Criar umma tabela 
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS alunos(id INTEGER PRIMARY KEY, nome TEXT, nota REAL)')

# adicionar dados na tabela = CREATE

cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (1, "Leandro", 8.5)')
cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (2,"Laise", 9.0)')
cursor.execute('INSERT INTO alunos (id, nome, nota) VALUES (3,"Michele", 7.0)')

# visualizar os dados da tabela = READ

cursor.execute ('SELECT * FROM alunos')
alunos = cursor.fetchall()
print(alunos)

#Atualizar os dados da tabela = UPDATE

cursor.execute('UPDATE alunos SET nota = 9.5 WHERE id = 1')

cursor.execute ('SELECT * FROM alunos WHERE id = 1')
alunos = cursor.fetchall()
print(alunos)

#Apagar dados da tabela = DELETE

cursor.execute('DELETE FROM alunos WHERE id = 2')

cursor.execute ('SELECT * FROM alunos')
alunos = cursor.fetchall ()
print(alunos)

#Fim do código





