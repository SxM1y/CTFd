from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import InputRequired

from CTFd.forms import BaseForm


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
