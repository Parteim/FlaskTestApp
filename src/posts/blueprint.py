from flask import Blueprint, request, render_template, redirect, url_for
from .forms import PostForm
from models import Post, Tag
from app import db

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
        posts = Post.query.order_by(Post.created.desc()).all()
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


@posts.route('/create_post', methods=['POST', 'GET'])
def create_post():
    form = PostForm()

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        if title or body == '':
            return render_template('posts/create_post.html', title='Create post', form=form)

        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Something wrong')

            slug = Post.all()[-1].slug
            print(slug)

        return redirect(url_for('posts_detail', slug=slug))
    return render_template('posts/create_post.html', title='Create post', form=form)
