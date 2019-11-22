import mysql.connector as sql

class db:
    
    host     = ""
    user     = ""
    passwd   = ""
    database = ""
    conn     = None
    cur      = None

    def __init__(self, host, user, passwd, database):
        self.host     = host
        self.user     = user
        self.passwd   = passwd
        self.database = database
        self.conn     = None
        # self.cur      = None # We'll have one cursor per query

    def connect(self):
        self.conn = sql.connect(host=self.host,
                                user=self.user,
                                password=self.passwd,
                                database=self.database)
        print("Connected to database")

    def createTable(self, tableName):
        cursor = sql.cursor()
        try:
            cursor.execute("CREATE TABLE {}".format(tableName))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            return 1

    def disconnect(self):
        self.conn.close()

    def execute(self, query):
        self.__connect()
        self.cur.execute(query)
        self.__disconnect()
