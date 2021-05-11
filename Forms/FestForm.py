from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import validators
from wtforms.fields.html5 import DateField


class FestForm(FlaskForm):
    fest_name = StringField("Name: ", [
        validators.DataRequired("Please enter name of festival"),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])

    fest_date = DateField("Date: ", [validators.DataRequired("Please, enter the date of festival")])


    submit = SubmitField("Save")

    def validate_date(self):
        return bool(self.fest_date.data.year > 2018)