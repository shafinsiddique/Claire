from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://skowser:hackthevalley@htv4-b4c1r.mongodb.net/test?retryWrites=true&w=majority")
db = cluster.get_database("recharge-backend")
class DBHelper:
    def __init__(self):
        self.mongocollection = db.posts


    def get_posts(self):
        cursor = self.mongocollection.find({})
        post_objects = []

        for posts in cursor:
            post_object = posts
            del post_object['_id']
            post_objects.append(post_object)

        return post_objects

    def insert_post(self, post):
        self.mongocollection.insert_one(post)

test = DBHelper()
print(test.get_posts())
