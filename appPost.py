from database import Database
from models.post import Post
import time

Database.initialize()

post = Post(1,1,"Title 1", "Content 1", "Raúl", time.time())
post2 = Post(2,1,"title el 2", "el content", "Pepe", time.time())
post.save_to_mongo()
post2.save_to_mongo()

posts = []
posts.append(post)
posts.append(post2)
[post.print() for post in posts]


