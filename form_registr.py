from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from models import User


class RegistrationForm(FlaskForm):
    first_name = StringField('Имя', validators=[DataRequired()])
    last_name = StringField('Фамилия', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])

    def validate_email(self, email):
        if self.submit.data:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Этот email уже занят')

    password = PasswordField('Пароль', validators=[DataRequired(), EqualTo('confirm_password',
                                                                           message='Пароли должны совпадать')])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')
