import mysql.connector


# main class for sql acesss

class sql:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': 'Ramdas@656463',
            'host': 'localhost',
            'database': 'songwave'
        }
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()

    def Query(self, query, values=None):
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

