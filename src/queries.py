
selectFromWhere = ("SELECT {} FROM {} WHERE {}={}")

insertIntoCateg = ("INSERT INTO Categories (categoryName, topic_id) "
                   "VALUES ({}, {})")

deleteFromCateg = ("DELETE FROM Categories WHERE categoryName={} "
                   "AND topic_id={}")


insertIntoTopics = ("INSERT INTO Topics (topicName) VALUES ({})")

deleteFromTopics = ("DELETE FROM Topics WHERE topicName={}")


insertIntoResources = ("INSERT INTO Resources "
                       "(resourceURL, category_id, topic_id) VALUES "
                       "({}, {}, {})")

deleteFromResources = ("DELETE FROM Resources WHERE resourceURL={} "
                       "AND category_id={} AND topic_id={}")



selectAllTopics      = ("SELECT * FROM Topics")

selectFromCategories = ("SELECT * FROM Categories WHERE topic_id={}")

selectFromResources  = ("SELECT * FROM Resources WHERE topic_id={} "
                        "AND category_id={}")
