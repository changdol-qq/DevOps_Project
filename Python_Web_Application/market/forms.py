from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterFrom(FlaskForm):
    def validate_username(self, username_to_ckeck):
        user = User.query.filter_by(username=username_to_ckeck.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='아이디:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='이메일 주소:', validators=[Email(),DataRequired()])
    password1 = PasswordField(label='비밀번호:', validators=[Length(min=6),DataRequired()])
    password2 = PasswordField(label='비밀번호 확인', validators=[EqualTo('password1'),DataRequired()])
    submit = SubmitField(label='계정 생성')


class LoginForm(FlaskForm):
    username =StringField(label='아이디:', validators=[DataRequired()])
    password = PasswordField(label='비밀번호:', validators=[DataRequired()])
    submit =SubmitField(label='로그인')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Purchase Item!')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item!')