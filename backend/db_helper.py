from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://skowser:<hackthevalley>@htv4-b4c1r.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["htv4"]
collection = db["htv4"]

class DBHelper:
    def __init__(self, mongocollection):
        self.mongocollection = mongocollection

    def get_posts(self):
        cursor = self.mongocollection.find({})
        subjects = []

        for post in cursor:
            subjects.append(post)

        return subjects

    def insert_post(self, post):
        self.mongocollection.insert_one(post)

de = DBHelper(collection)
print(de.get_posts())
