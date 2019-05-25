from database import Database


class Post:

    def __init__(self, id, blog_id, title, content, author, date):
        self.id = id
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date

    def print(self):
        print(self.title + " " + self.content + " " + self.author)

    def save_to_mongo(self):
        Database.insert('posts', self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @staticmethod
    def from_mongo(id):
            data = Database.findOne('posts', query={'id', id})

    @staticmethod
    def from_blog(id):
            data = Database.findOne('posts', query={'blog_id', id})
