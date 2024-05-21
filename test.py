
# 홈 페이지 라우트
@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')

# 데이터베이스 초기화
with app.app_context():
    db.create_all()

# 이벤트 페이지 라우트
@app.route('/event', methods=['GET', 'POST'])
@login_required
def event_page():
    booking_form = BookEventForm()
    cancel_form = CancelEventForm()
    if request.method == "POST":
        event_action(request)
        return redirect(url_for('event_page'))
    
    events = Event.query.all()
    owned_events = [event for event in events if current_user in event.users]
    return render_template('event.html', events=events, booking_form=booking_form, owned_events=owned_events, cancel_form=cancel_form)

# 이벤트 예약 및 취소 로직 처리
def event_action(request):
    if booked_item := request.form.get('booked_item'):
        process_event(booked_item, 'book', '참석이 등록되었습니다.')

    if cancel_item := request.form.get('cancel_item'):
        process_event(cancel_item, 'cancel', '참석이 취소되었습니다.')

# 이벤트 처리 공통 함수
def process_event(item_name, action, message):
    event_object = Event.query.filter_by(name=item_name).first()
    if event_object:
        getattr(event_object, action)(current_user)
        db.session.commit()
        flash(f"{message} {event_object.name} for {event_object.price}$", category='success')

# 회원가입 페이지 라우트
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        handle_registration(form)
        return redirect(url_for('event_page'))
    handle_form_errors(form)
    return render_template('register.html', form=form)

# 로그인 페이지 라우트
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit() and handle_login(form):
        return redirect(url_for('event_page'))
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
    form = CreateEventForm()
    if form.validate_on_submit():
        create_event(form)
        return redirect(url_for('event_page'))
    handle_form_errors(form)
    return render_template('create.html', form=form)

# 폼 오류 처리
def handle_form_errors(form):
    if form.errors:
        for err_msg in form.errors.values():
            flash(f'오류 발생: {err_msg}', category='danger')

# 회원가입 처리
def handle_registration(form):
    user_to_create = User(username=form.username.data, email_address=form.email_address.data, password=form.password1.data)
    db.session.add(user_to_create)
    db.session.commit()
    login_user(user_to_create)
    flash(f"회원가입이 성공적으로 완료되었습니다. {user_to_create.username} 님 환영합니다.", category='success')

# 로그인 처리
def handle_login(form):
    attempted_user = User.query.filter_by(username=form.username.data).first()
    if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
        login_user(attempted_user)
        flash(f'로그인에 성공하셨습니다. 환영합니다 {attempted_user.username}님.', category='success')
        return True
    flash('아이디와 비밀번호가 다릅니다. 다시 시도 해주세요', category='danger')
    return False

# 이벤트 생성
def create_event(form):
    event_to