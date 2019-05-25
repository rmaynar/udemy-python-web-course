from database import Database
from models.post import Post

Database.initialize()

# post = Post(1,"Title 1342432", "Content 1", "Raúl")
# post2 = Post(1,"title el 234243", "el content", "Pepe")
# post.save_to_mongo()
# post2.save_to_mongo()

posts = Post.from_blog(1)
if posts is None:
    print("No existen")
else:
    print(posts.size)


