from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length


class ClientForm(Form):
     account = StringField(validators=[DataRequired(),
                                       length(min=5,max=32)],
     password = StringField(),
     type = IntegerField()

