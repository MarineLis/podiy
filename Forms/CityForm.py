from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField
from wtforms import validators


class CityForm(FlaskForm):
    city_name = StringField("Name: ", [
        validators.DataRequired("Please enter city name."),
        validators.Length(3, 20, "Name should be from 3 to 20 symbols")
    ])
    city_population = IntegerField("City population: ", [
        validators.DataRequired("Please enter city."),
    ])
    city_balance = IntegerField("Balance: ", [
        validators.DataRequired("Please enter balance.")
    ])

    city_government = StringField("Government: ", [
        validators.DataRequired("Please enter government."),
        validators.Length(3, 15, "Name should be from 3 to 15 symbols")
    ])

    submit = SubmitField("Save")

    def check_balance_on_submit(self):
        return bool(self.city_balance.data > 0)

    def check_population_on_submit(self):
        return bool(0 < self.city_population.data < 100)
