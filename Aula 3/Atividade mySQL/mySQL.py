import mysql.connector

class Database:
    def __init__(self):
        self.cnx = mysql.connector.connect(
            user='root',
            password='tuv6YWzy0wXiKis8TiBS',
            host='containers-us-west-175.railway.app',
            port=5780,
            database='railway'
        )
        self.cursor = self.cnx.cursor()

    def createTable(self):
        create_table = """
                CREATE TABLE IF NOT EXISTS CLIENTE 
                (NUMCONTA INT AUTO_INCREMENT PRIMARY KEY,
                SALDO FLOAT);
        """
        self.cursor.execute(create_table)
        self.cnx.commit()

    def putAccounts(self, accounts):
        for account in accounts:            
            take_infomation = (f'''
                                SELECT NUMCONTA FROM CLIENTE 
                                WHERE NUMCONTA = {account.numero};
                                ''')
            self.cursor.execute(take_infomation)
            verify_Account = self.cursor.fetchone()
            if verify_Account:
                checking_account = (f'''UPDATE CLIENTE SET SALDO = {account.saldo} 
                                    WHERE NUMCONTA = {account.numero};''')
                self.cursor.execute(checking_account)
            else:
                new_account = (f'''INSERT INTO CLIENTE 
                                    VALUES ({account.numero}, {account.saldo});''')
                self.cursor.execute(new_account)
            
        self.cnx.commit()     

    def loadAccounts(self):
        select_values = """
            SELECT NUMCONTA, SALDO FROM CLIENTE;
        """
        self.cursor.execute(select_values)
        accounts = self.cursor.fetchall()
        customers = []
        for account in accounts:
            accountDictionary = {'NUMCONTA': account[0], 'SALDO': account[1]}
            customers.append(accountDictionary)
        return customers

    def endConnection(self):
        self.cnx.close()

    def excludeTables(self):
        show_tables = "SHOW TABLES"
        self.cursor.execute(show_tables)
        tables = self.cursor.fetchall()
        for table in tables:
            drop_table = f"DROP TABLE {table[0]}"
            self.cursor.execute(drop_table)
            self.cnx.commit()
    

