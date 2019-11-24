import mysql.connector as sql_
import queries as q

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
        self.conn = sql_.connect(host=self.host,
                                 user=self.user,
                                 password=self.passwd,
                                 database=self.database)
        print("Connected to database")

    def addCatToTopic(self, catName, topicName):
        cursor = self.conn.cursor()
        try:
            # Retrieve the topicId for topicName
            cursor.execute(q.selectFromWhere.format('topicId',
                                                    'Topics',
                                                    'topicName',
                                                    '"' + topicName + '"'))
            # fetchall will be like [(x,)] where x is the topicID
            topicId = cursor.fetchall()[0][0] # Fetch only x, the topicID

            cursor.execute(q.insertIntoCateg.format('"' + catName + '"',
                                                   topicId))
            self.conn.commit()
        except Exception as e:
            print("Error at addCatToTopic: {}".format(e))
            return 1
        finally:
            cursor.close()

    def rmCatFromTopic(self, catName, topicName):
        cursor = self.conn.cursor()
        try:
            # Retrieve the topic Id for the topicName
            cursor.execute(q.selectFromWhere.format('topicId',
                                                    'Topics',
                                                    'topicName',
                                                    '"' + topicName + '"'))
            topicId = cursor.fetchall()[0][0]

            cursor.execute(q.deleteFromCateg.format('"' + catName + '"',
                                                    topicId))
            self.conn.commit()
        except Exception as e:
            print("Error at rmCatFromTopic: {}".format(e))
            return 1
        finally:
            cursor.close()


    def addTopic(self, topicName):
        cursor = self.conn.cursor()
        try:
            cursor.execute(q.insertIntoTopics.format('"' + topicName + '"'))
            self.conn.commit()
        except Exception as e:
            print("Error at addTopic: {}".format(e))
            return 1
        finally:
            cursor.close()

    def rmTopic(self, topicName):
        cursor = self.conn.cursor()
        try:
            cursor.execute(q.deleteFromTopics.format('"' + topicName + '"'))
            self.conn.commit()
        except Exception as e:
            print("Error at rmTopic: {}".format(e))
            return 1
        finally:
            cursor.close()


    def disconnect(self):
        self.conn.close()

    def execute(self, query):
        self.__connect()
        self.cur.execute(query)
        self.__disconnect()
