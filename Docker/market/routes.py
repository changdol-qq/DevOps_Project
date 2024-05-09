from market import app, db
from market.models import Item, User
from flask import render_template, redirect, url_for, flash, request
from market.forms import RegisterFrom, LoginForm, PurchaseItemForm, SellItemForm
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home/')
def home_page():
    return render_template('home.html')

with app.app_context():
    db.create_all()

@app.route('/market', methods=['GET', 'POST'])
@login_required
def market_page():
    purchase_form = PurchaseItemForm()
    selling_form = SellItemForm()
    if request.method == "POST":
        #Purchase Item Logic
        purchased_item = request.form.get('purchased_item')
        p_item_object = Item.query.filter_by(name=purchased_item).first()
        if p_item_object: 
            p_item_object.buy(current_user)
            flash(f"이벤트 참석이 등록되었습니다. {p_item_object.name} for {p_item_object.price}$", category='success')
            
        #Sell Item Logic
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            #s_item_object.sell(current_user)
            flash(f"이벤트 참석이 취소되었습니다. {s_item_object.name} back to market!", category='success')

        return redirect(url_for('market_page'))
    
    if request.method == "GET":
        items = Item.query#.filter_by(owner=None)
        owned_items = Item.query.filter_by(owner=current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, owned_items=owned_items, selling_form = selling_form)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterFrom()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"회원가입이 성공적으로 완료되었습니다. {user_to_create.username} 님 환영합니다.")
        return redirect(url_for('market_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'유저를 생성하는데 에러가 발생했습니다.:{err_msg}', category='danger')
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form =LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'로그인에 성공하셨습니다. 환영합니다 {attempted_user.username}님.', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('아이디와 비밀번호가 다릅니다. 다시 시도 해주세요', category= 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("로그아웃 되었습니다.", category='info')
    return redirect(url_for("home_page"))
