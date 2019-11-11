import pymysql

class db:
    def __init__(self, host, user, passwd, database):
        self.host     = host
        self.user     = user
        self.passwd   = passwd
        self.database = database
        self.conn     = None
        self.cur      = None

    def connect(self):
        self.conn = pymysql.connect(self.host, self.user,
                                    self.passwd, self.database)
        self.cur  = self.conn.cursor()
        print("Connected to database")

    def disconnect(self):
        self.conn.close()

    def fetch(self, query):
        self.__connect()
        self.cur.execute(query)
        res = self.cur.fetchall()
        self.__disconnect()
        return res

    def execute(self, query):
        self.__connect()
        self.cur.execute(query)
        self.__disconnect()
