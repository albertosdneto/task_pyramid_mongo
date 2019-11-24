# import colander
from wtforms import Form, StringField, IntegerField, validators
from wtforms.widgets import HiddenInput


class TaskForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    active = IntegerField('Active', [validators.InputRequired()])


class TaskUpdateForm(TaskForm):
    id = StringField(widget=HiddenInput())
