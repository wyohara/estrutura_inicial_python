from database.conexoes.sqlite_conn import create_connection

class UserModel:
    def __init__(self, db_file):
        self.conn= create_connection(db_file)
        self.create_table()

    def create_table(self):
        """ Cria a tabela de usuários se não existir """
        try:
            sql_create_users_table = """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            );
            """
            cursor = self.conn.cursor()
            cursor.execute(sql_create_users_table)
        except Exception as e:
            print(e)

    def create_user(self, name, age):
        """ Insere um novo usuário """
        sql = ''' INSERT INTO users(name, age)
                  VALUES(?, ?) '''
        cursor = self.conn.cursor()
        cursor.execute(sql, (name, age))
        self.conn.commit()
        return cursor.lastrowid

    def read_users(self):
        """ Lê todos os usuários """
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()

    def update_user(self, user_id, name, age):
        """ Atualiza um usuário existente """
        sql = ''' UPDATE users
                  SET name = ? ,
                      age = ?
                  WHERE id = ?'''
        cursor = self.conn.cursor()
        cursor.execute(sql, (name, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        """ Deleta um usuário """
        sql = 'DELETE FROM users WHERE id=?'
        cursor = self.conn.cursor()
        cursor.execute(sql, (user_id,))
        self.conn.commit()
