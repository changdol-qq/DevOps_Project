from event import db, login_manager
from event import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#다대다 중간 테이블
user_event = db.Table('user_event',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True)
    )

#유저 테이블
class User(db.Model, UserMixin):
    id              = db.Column(db.Integer(), primary_key=True)
    username        = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address   = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash   = db.Column(db.String(length=60), nullable=False)
    count           = db.Column(db.Integer(), nullable=False, default=0) 
    events          = db.relationship('Event', secondary=user_event, back_populates='users')
    owned_events    = db.relationship('Event', backref='owner_user', lazy=True)
    @property
    def prettier_count(self):
        if len(str(self.count)) >= 4:
            return f'{str(self.count)[:-3]},{str(self.count)[-3:]}'
        else:
            return f"{self.count}"
    @property 
    def password(self):
        raise AttributeError('Password is not a readable attribute.')
    # @property 
    # def password(self):
    #     return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

#이벤트 테이블    
class Event(db.Model):
    id          = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date        = db.Column(db.Date(), nullable=False ) 
    name        = db.Column(db.String(length=30), nullable=False, unique=True) 
    location    = db.Column(db.String(length=30), nullable=False) 
    price       = db.Column(db.Integer(), nullable=False) 
    attend      = db.Column(db.String(length=12) )
    description = db.Column(db.String(length=1024)) 
    owner_id    = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False) 
    users       = db.relationship('User', secondary=user_event, back_populates='events')
    def __repr__(self):
        return f'Event {self.name}'
    
    def book(self, user):
        if user not in self.users:
            self.users.append(user)
            user.count += 1
            db.session.commit()


    def cancel(self, user):
        if user in self.users:
            self.users.remove(user)
            user.count -= 1
            db.session.commit()
        
