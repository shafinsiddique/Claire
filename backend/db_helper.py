from pymongo import MongoClient

class DBHelper:
    def __init__(self, mongocollection):
        self.mongocollection = mongocollection
        pass

    def get_posts(self):
        # cursor = self.mongocollection.find({})
        # post_objects = []
        # for posts in cursor:
        #     post_objects.append()

        # return a list of all the post objects. List of dicitonaries
        # [{"name":"my first blog", "date": "22 Oct, 1999", "id"=1}]
        pass

    def insert_post(self, post):
        # insert <post> into the db.
        pass


    def get_sentiments(self):
        """Return a list of lists [a, b] in which a = date of the post, b = sentiment score
        for that post. One tuple for each post."""
        pass

