import sqlite3

con = sqlite3.connect("bancoDeDados.db")    

cursor = con.cursor()
cursor.execute('''DROP TABLE ALUNO''')
con.commit()

cursor.execute('''CREATE TABLE ALUNO (MATRICULA INTEGER PRIMARY KEY, SENHA VARCHAR(30), CPF INT, NOME VARCHAR(20))''')
con.commit()

cursor.execute("INSERT INTO ALUNO VALUES (20,'TESTE', 1, 'Neto')")
cursor.execute("INSERT INTO ALUNO VALUES (30, 2, 'Costa')") #Não funciona porque não preencheu todas as colunas dessa linha
cursor.execute("INSERT INTO ALUNO (MATRICULA, NOME) VALUES (11, 'Pires')")#Outro modo de inserir valores específicos
con.commit()

cursor.execute("DELETE FROM ALUNO WHERE MATRICULA = 11")
con.commit()

login = input("digite seu nome:")
senha = input("digite sua senha:")
items = {"login": login, "senha": senha}

cursor.execute("SELECT * FROM ALUNO WHERE NOME = :login AND SENHA = :senha", items)
result = cursor.fetchone()
if result:
    print("Você está logado")
else:
    print("Login e senha errados")


# cursor.execute("SELECT * FROM ALUNO")
# result = cursor.fetchall()#Result vai ser uma lista com todas as linhas
# for a in result:
    # print(a)

# result = cursor.fetchmany(5)
# print(result)
'''
cursor.fetchall() fetches all the rows of a query result. It returns all the rows as a list of tuples. An empty list is returned if there is no record to fetch.

cursor.fetchmany(size) returns the number of rows specified by size argument. When called repeatedly, this method fetches the next set of rows of a query result and returns a list of tuples. If no more rows are available, it returns an empty list.

cursor.fetchone() method returns a single record or None if no more rows are available.
'''
cursor.close()
con.close()