from database import Database
from models.blog import Blog
from models.post import Post

Database.initialize()

# post = Post(2,"Title lalala", "Content 1", "Raúl")
# post2 = Post(1,"title el 234243", "el content", "Pepe")
# post.save_to_mongo()
# post2.save_to_mongo()


blog = Blog(author="Raúl",
            title="Sample title",
            description="Sample description")

blog.new_post()

blog.save_to_mongo()

print("El blog")
print(blog.json())

# from_database = Blog.from_mongo(blog.id)
#
# blog.get_posts()
