from wtforms import BooleanField, PasswordField, SelectField, StringField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm
from CTFd.utils.countries import SELECT_COUNTRIES_LIST


class UserSearchForm(BaseForm):
    field = SelectField(
        "Search Field",
        choices=[
            ("name", "Name"),
            ("id", "ID"),
            ("email", "Email"),
            ("affiliation", "Affiliation"),
            ("ip", "IP Address"),
        ],
        default="name",
        validators=[InputRequired()],
    )
    q = StringField("Parameter", validators=[InputRequired()])
    submit = SubmitField("Search")


class UserCreateForm(BaseForm):
    name = StringField("User Name", validators=[InputRequired()])
    email = EmailField("Email", validators=[InputRequired()])
    password = PasswordField("Password")
    website = StringField("Website")
    affiliation = StringField("Affiliation")
    country = SelectField("Country", choices=SELECT_COUNTRIES_LIST)
    type = SelectField("Type", choices=[("user", "User"), ("admin", "Admin")])
    verified = BooleanField("Verified")
    hidden = BooleanField("Hidden")
    banned = BooleanField("Banned")
    submit = SubmitField("Submit")
