from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators


class SearchForm(FlaskForm):
    type_field = SelectField('Choose field', choices=[
        ('fest_name', 'fest_name'),
        ('fest_date', 'fest_date'),
    ])
    search_value = StringField("Value: ", [validators.DataRequired('shouldnt be empty value')])

    submit = SubmitField("Search")