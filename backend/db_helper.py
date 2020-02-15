from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://skowser:<hackthevalley>@htv4-b4c1r.mongodb.net/test?retryWrites=true&w=majority")
db = cluster['htv4']
collection = db['htv4']

class DBHelper:
    def __init__(self, mongocollection):
        self.mongocollection = mongocollection


    def get_posts(self):
        cursor = self.mongocollection.find({})
        post_objects = []

        for posts in cursor:
            post_objects.append(posts)

        return post_objects

    def insert_post(self, post):
        self.mongocollection.insert_one(post)

test = DBHelper(collection)
print(test.get_posts())
