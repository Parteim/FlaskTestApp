from flask import Flask
from src.config import Configuration
from src.posts.blueprint import posts


app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(posts, url_prefix='/blog')