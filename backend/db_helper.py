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

    def get_sentiment(self):
        cursor = self.mongocollection.find({})
        sentiments = []

        for posts in cursor:
            pair = []
            senti = posts['sentiment']
            date = str(posts['date'])

            pair.append(date)
            pair.append(senti)
            sentiments.append(pair)

        return sentiments

    def get_latest_id(self):
        posts = self.get_posts()
        ids = []
        for i in posts:
            ids.append(int(i['post_id']))

        return max(ids)+1


d = DBHelper()
print(d.get_latest_id())


