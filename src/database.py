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

    def disconnect(self):
        self.conn.close()


    def getTopicIdFromName(self, topicName):
        try:
            cursor = self.conn.cursor()
            cursor.execute(q.selectFromWhere.format('topicId',
                                                    'Topics',
                                                    'topicName',
                                                    '"' + topicName + '"'))
            topicId = cursor.fetchall()[0][0]
            cursor.close()
            return topicId
        except Exception:
            raise

    def getCategIdFromName(self, categName):
        try:
            cursor = self.conn.cursor()
            cursor.execute(q.selectFromWhere.format('categoryId',
                                                    'Categories',
                                                    'categoryName',
                                                    '"' + categName + '"'))
            categId = cursor.fetchall()[0][0]
            cursor.close()
            return categId
        except Exception:
            raise


    def rmAddTop(self, topicName, order, topicDesc=None):
        try:
            cursor = self.conn.cursor()
            if order == "add":
                if topicDesc == None:
                    return # TODO: Throw Exception
                cursor.execute(q.insertIntoTopics.format("'" + topicName + "'",
                                                         "'" + topicDesc + "'"))
            elif order == "rm":
                cursor.execute(q.deleteFromTopics.format('"' + topicName + '"'))
            else:
                raise ValueError("Second argument must be either 'add' or 'rm'")
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print("Exception: {}".format(e))
            raise

    def rmAddCat(self, topicName, categName, order):
        try:
            topicId = self.getTopicIdFromName(topicName)
            cursor  = self.conn.cursor()
            if order == "add":
                cursor.execute(q.insertIntoCateg.format('"' + categName + '"',
                                                        topicId))
            elif order == "rm":
                cursor.execute(q.deleteFromCateg.format('"' + categName + '"',
                                                        topicId))
            else:
                raise ValueError("Third argument must be either 'add' or 'rm'")
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise

    def rmAddRes(self, topicName, categName, url, order):
        try:
            topicId = self.getTopicIdFromName(topicName)
            categId = self.getCategIdFromName(categName)

            cursor  = self.conn.cursor()
            if order == "add":
                cursor.execute(q.insertIntoResources.format('"' + url + '"',
                                                            categId,
                                                            topicId))
            elif order == "rm":
                cursor.execute(q.deleteFromResources.format('"' + url + '"',
                                                            categId,
                                                            topicId))
            else:
                raise ValueError("Fourth argument must be either 'add' or 'rm'")
            self.conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            raise



    def getTopics(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(q.selectAllTopics)
            topics = cursor.fetchall()
            cursor.close()
            return topics
        except Exception:
            raise

    def getCategories(self, topicName):
        try:
            topicId = self.getTopicIdFromName(topicName)

            cursor = self.conn.cursor()
            cursor.execute(q.selectFromCategories.format(topicId))
            cats   = cursor.fetchall()
            cursor.close()
            return cats
        except Exception:
            raise

    def getResources(self, topicName, categName):
        try:
            topicId = self.getTopicIdFromName(topicName)
            categId = self.getCategIdFromName(categName)

            cursor = self.conn.cursor()
            cursor.execute(q.selectFromResources.format(topicId, categId))
            res    = cursor.fetchall()
            cursor.close()
            return res
        except Exception:
            raise
