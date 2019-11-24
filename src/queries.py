
selectFromWhere = ("SELECT {} FROM {} WHERE {}={}")

insertIntoCateg = ("INSERT INTO Categories (categoryName, topic_id) "
                   "VALUES ({}, {})")

deleteFromCateg = ("DELETE FROM Categories WHERE categoryName={} "
                   "AND topic_id={}")

insertIntoTopics = ("INSERT INTO Topics (topicName) VALUES ({})")

deleteFromTopics = ("DELETE FROM Topics WHERE topicName={}")
