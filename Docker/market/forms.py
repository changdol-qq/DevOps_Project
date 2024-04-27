from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterFrom(FlaskForm):
    def validate_username(self, username_to_ckeck):
        user = User.query.filter_by(username=username_to_ckeck.data).first()
        if user:
            raise ValidationError('아이디가 이미 사용중입니다. 다른 아이디를 사용해주세요')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('이메일주소가 이미 사용중입니다. 다른 이메일 주소를 사용해주세요')

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
    submit = SubmitField(label='이벤트 참석')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='참석 취소')