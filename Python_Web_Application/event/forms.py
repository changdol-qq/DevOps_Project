from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, TextAreaField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, NumberRange
from event.models import User

# 폼 클래스 정의
class RegisterForm(FlaskForm):
    username = StringField(label='아이디:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='이메일 주소:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='비밀번호:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='비밀번호 확인:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='계정 생성')

    # 사용자명 중복 검사
    def validate_username(self, username_to_check):
        if User.query.filter_by(username=username_to_check.data).first():
            raise ValidationError('아이디가 이미 사용중입니다. 다른 아이디를 사용해주세요')

    # 이메일 주소 중복 검사
    def validate_email_address(self, email_address_to_check):
        if User.query.filter_by(email_address=email_address_to_check.data).first():
            raise ValidationError('이메일주소가 이미 사용중입니다. 다른 이메일 주소를 사용해주세요')

# 이벤트 생성 폼 클래스 정의
class CreateEventForm(FlaskForm):
    date = DateField('Event Date', validators=[DataRequired()])
    name = StringField('Event Name', validators=[DataRequired(), Length(max=30)])
    location = StringField('Location', validators=[DataRequired(), Length(max=30)])
    price = IntegerField('Price', validators=[DataRequired(), NumberRange(min=0)])
    attend = StringField('Barcode', validators=[Length(max=12)])
    description = TextAreaField('Description', validators=[Length(max=1024)])
    submit = SubmitField(label='이벤트 등록')

# 로그인 폼 클래스 정의
class LoginForm(FlaskForm):
    username = StringField(label='아이디:', validators=[DataRequired()])
    password = PasswordField(label='비밀번호:', validators=[DataRequired()])
    submit = SubmitField(label='로그인')

# 이벤트 참석 폼 클래스 정의
class BookEventForm(FlaskForm):
    submit = SubmitField(label='이벤트 참석')

# 이벤트 취소 폼 클래스 정의
class CancelEventForm(FlaskForm):
    submit = SubmitField(label='참석 취소')