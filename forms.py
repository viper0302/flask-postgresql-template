from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import models


class LoginForm(Form):
    email = StringField('Name',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                        validators=[DataRequired(), Length(min=8)])

    def validate(self):
        form_is_valid = super(LoginForm, self).validate()

        if not form_is_valid:
            return False

        user = models.User.get_user_by_email(self.email)

        if user is None:
            self.email.errors.append('Invalid email or password')
            return False

        if not user.check_password(self.password.data):
            self.email.errors.append('Invalid email or password')
            return False

        return True


class RegistrationForm(Form):
    email = StringField('Name', validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=8)])
    confirm = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])

    def validate(self):
        form_is_valid = super(RegistrationForm, self).validate()

        if not form_is_valid:
            return False

        user = models.User.get_user_by_email(self.email)

        if user is not None:
            self.email.errors.append('User with that name already exists')
            return False

        return True
