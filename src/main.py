from src.app import app, db
import src.view

from src.posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    app.run()