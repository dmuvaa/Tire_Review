from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class ArticleForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    slug = StringField('Slug', validators=[DataRequired(), Length(max=255)])
    meta_description = TextAreaField('Meta Description', validators=[Length(max=255)])
