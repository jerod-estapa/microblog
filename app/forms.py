from flask.ext.wtf import Form
from wtforms import Textfield, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):

    openid = Textfield('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)