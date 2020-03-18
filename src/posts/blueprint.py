from flask import Blueprint, request, render_template
from .forms import PostForm
from models import Post, Tag

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def posts_page():
    search_value = request.args.get('search', '')

    if search_value:
        posts = Post.query.filter(
            Post.title.contains(search_value) |
            Post.body.contains(search_value)
        ).all()
    else:
        posts = Post.query.all()
    return render_template('posts/posts.html', title='Posts', posts=posts)


@posts.route('/<slug>')
def post_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/post.html', title=post.title, post=post)


@posts.route('/tag/<slug>')
def posts_by_tag(slug):
    tag = Tag.query.filter(Tag.slug == slug).first()
    posts = tag.posts.all()
    return render_template('posts/posts.html', title=tag.name, posts=posts, tag=tag)


@posts.route('/create_post')
def create_post():
    form = PostForm()
    return render_template('posts/create_post.html', title='Create post', form=form)
