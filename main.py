# Criar um banco de dados SQLite e uma tabela
import sqlite3

#Criar a conexão com o banco de dados chamado de "escola.db"!!!
conexao = sqlite3.connect("escola.db")

# #Criar o objeto chamado de "Cursor" que será usado para execultar os comandos sql !!!
cursor = conexao.cursor()

# #Criar uma tabela no banco 
# cursor.execute("""
#  CREATE TABLE IF NOT EXISTS alunos(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     idade INTEGER, 
#     curso TEXT               
# )            
#  """)
# nome = input("Digite o nome do aluno: ").lower()
# idade = int(input("Digite a idade do aluno: "))
# curso = input("Digite o curso do aluno: ").lower()

# #Inserir o dado na tabela !!!
# cursor.execute("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)                                
# """,
# (nome, idade, curso )
# )


# #Confirmar as alterações no banco !!!
# conexao.commit()

#Inserir varios alunos de uma só vez!!!

# alunos = [
#     ("Yago", 28, "Direito"),
#     ("Jessica", 24, "Computação"),
#     ("Breno", 52, "Computação")
# ]
# #Executemany permite inserir múltiplas linha de uma só vez!!!

# cursor.executemany ("""
# INSERT INTO alunos (nome, idade, curso)
# VALUES (?,?,?)
# """,
# (alunos)
# )
# conexao.commit()

#!Atualizar dados no banco !!
cursor.execute("""
UPDATE alunos 
SET idade = ?, curso = ?
WHERE id = ?

""", (61, "Medicina", 2)
)
conexao.commit()