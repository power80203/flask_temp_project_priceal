import pymongo

class Database:
    uri = "mongodb://127.0.0.1:27017/pricing"
    DATABASE = pymongo.MongoClient(uri).get_database()

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.uri)
        Database.DATABASE =client['mydatabase']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, qury):
        return Database.DATABASE[collection].find(qury)

    @staticmethod
    def find_one(collection, qury):
        return Database.DATABASE[collection].find_one(qury)
    

    

if __name__ == '__main__':
    print(Database.initialize())
    