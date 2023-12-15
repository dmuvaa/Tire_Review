from flask import render_template, redirect, url_for, request
from ..forms import ArticleForm
from . import views
from ..models import Article
from .. import db


@views.route('/')
@views.route('/home')
def index():
    return render_template('index.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/article')
def article():
    return render_template('article1.html')

@views.route('/blog', methods=['GET', 'POST'])
def blog():
    form = ArticleForm()
    if request.method == 'POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        description = request.form.get('meta_description')
        content=content=request.form.get('editordata')
        article = Article(title=title, slug=slug, content=content, meta_description=description)

        db.session.add(article)
        db.session.commit()
        return redirect(url_for('views.display', slug=article.slug))
    return render_template('blog.html', form=form)

@views.route('/display/<slug>')
def display(slug):
    data = Article.query.filter_by(slug=slug).first()
    print(data.slug)
    if data:
        return render_template('display.html', article=data)
    return render_template('display.html')
    


@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/dealerships')
def dealerships():
    return render_template('dealerships.html')

@views.route('/learn')
def learn():
    return render_template('learn.html')
