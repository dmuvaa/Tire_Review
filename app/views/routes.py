from flask import render_template, request
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
    if request.method == 'POST':
        new_data = Article(content=request.form.get('editordata'))
        db.session.add(new_data)
        db.session.commit()
        return 'Posted Data'
    return render_template('blog.html')

@views.route('/display/<int:id>')
def display(id):
    data = Article.query.get(id)
    print(data.content)
    return render_template('display.html', data=data.content)


@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/dealerships')
def dealerships():
    return render_template('dealerships.html')

@views.route('/learn')
def learn():
    return render_template('learn.html')
