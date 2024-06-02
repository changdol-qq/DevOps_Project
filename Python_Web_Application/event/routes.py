from flask import render_template, redirect, url_for, flash, request, current_app as app, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from event import db
from event.models import Event, User
from event.forms import RegisterForm, LoginForm, BookEventForm, CancelEventForm, CreateEventForm



# 데이터베이스 초기화
with app.app_context():
    db.create_all()

# 홈 페이지 라우트 
@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')

# 이벤트 페이지 라우트
@app.route('/event', methods=['GET', 'POST'])
@login_required
def event_page():
    booking_form = BookEventForm() # 이벤트 예약 폼
    cancel_form = CancelEventForm() # 이벤트 취소 폼
    
    if request.method == "POST":
        # 이벤트 예약 처리
        booked_item = request.form.get('booked_item') 
        p_event_object = Event.query.filter_by(name=booked_item).first() 
        if p_event_object: 
            p_event_object.book(current_user)
            if p_event_object:
                p_event_object.book(current_user)
                db.session.commit()  # 데이터베이스에 변경 사항 저장.
                flash(f"이벤트 참석이 등록되었습니다. {p_event_object.name} for {p_event_object.price}$", category='success')

        # 이벤트 취소 처리
        cancel_item = request.form.get('cancel_item')
        s_event_object = Event.query.filter_by(name=cancel_item).first()
        if s_event_object:
            s_event_object.cancel(current_user)
            if s_event_object:
                s_event_object.cancel(current_user)
                db.session.commit()  # 데이터베이스에 변경 사항 저장.
                flash(f"이벤트 참석이 취소되었습니다. {s_event_object.name} back to event!", category='success')

        return redirect(url_for('event_page'))
    
    if request.method == "GET":
        # 이벤트 목록과 사용자가 예약한 이벤트 목록을 불러와 렌더링
        events = Event.query.all()
        owned_events = [event for event in events if current_user in event.users]
        return render_template('event.html', events=events, booking_form=booking_form, owned_events=owned_events, cancel_form = cancel_form)

# 회원가입 페이지 라우트
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm() # 회원가입 폼
    if form.validate_on_submit():
        # 유효성 검사 통과 시 사용자 생성
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"회원가입이 성공적으로 완료되었습니다. {user_to_create.username} 님 환영합니다.")
        return redirect(url_for('event_page'))
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'유저를 생성하는데 에러가 발생했습니다.:{err_msg}', category='danger')
    return render_template('register.html', form=form)

# 로그인 페이지 라우트
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form =LoginForm() # 로그인 폼
    # 유효성 검사 통과 시 로그인 처리
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'로그인에 성공하셨습니다. 환영합니다 {attempted_user.username}님.', category='success')
            return redirect(url_for('event_page'))
        else:
            flash('아이디와 비밀번호가 다릅니다. 다시 시도 해주세요', category= 'danger')

    return render_template('login.html', form=form)

# 로그아웃 페이지 라우트
@app.route('/logout')
def logout_page():
    logout_user()
    flash("로그아웃 되었습니다.", category='info')
    return redirect(url_for("home_page"))

# 이벤트 생성 페이지 라우트
@app.route('/create', methods=['GET', 'POST'])
@login_required
def create_page():
    form = CreateEventForm() # 이벤트 생성 폼
    if form.validate_on_submit():
        # 유효성 검사 통과 시 이벤트 생성
        event_to_create = Event(date = form.date.data, name = form.name.data,
                                location = form.location.data, price = form.price.data,
                                description = form.description.data,
                                owner_id = current_user.id)
        db.session.add(event_to_create)
        db.session.commit()
        flash(f"{event_to_create.name} 이벤트가 성공적으로 등록되었습니다.")
        return redirect(url_for('event_page'))    
    if form.errors != {}: 
        for err_msg in form.errors.values():
            flash(f'유저를 생성하는데 에러가 발생했습니다.:{err_msg}', category='danger')                    
    return render_template('create.html', form=form)


