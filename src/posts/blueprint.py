from flask import Blueprint
from flask import render_template
from src import static

posts = Blueprint('posts', __name__, template_folder='templates', static_folder=static.__name__)


@posts.route('/')
def posts_page():
    return render_template('posts/posts.html', title='Posts')
