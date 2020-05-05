# https://dzone.com/articles/strategy-vs-factory-design-pattern-in-java
# https://stackoverflow.com/questions/616796/what-is-the-difference-between-factory-and-strategy-patterns
# https://stackoverflow.com/questions/2386125/real-world-examples-of-factory-method-pattern

from abc import ABCMeta, abstractmethod


class DBTable(metaclass=ABCMeta):
    @abstractmethod
    def create_table(self):
        pass


class PostgreSQL(DBTable):
    def create_table(self):
        print("creating table in postgreSQL")


class MongoDB(DBTable):
    def create_table(self):
        print("creating table in MongoDB")


class DBFactory():
    def __init__(self):
        """
        change this db config in order to change
        the underlying DB
        """
        self.db_config = 'sql'

    def get_database(self):
        if self.db_config == 'sql':
            return PostgreSQL()
        else:
            return MongoDB()


print("creating table in database")
db_factory = DBFactory()
db = db_factory.get_database()
db.create_table()
