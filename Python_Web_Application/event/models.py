from event import db, login_manager
from event import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    count = db.Column(db.Integer(), nullable=False, default=0) #budget
    Events = db.relationship('Event', backref='owned_user', lazy=True)
    @property
    def prettier_count(self):
        if len(str(self.count)) >= 4:
            return f'{str(self.count)[:-3]},{str(self.count)[-3:]}'
        else:
            return f"{self.count}"

    @property 
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
            
    # def can_purchase(self, item_obj):
    #     return self.budget >= item_obj.price
    
    # def can_sell(self, item_obj):
    #     return item_obj in self.items

class Event(db.Model):
    date = db.Column(db.Date(), nullable=False ) #id 
    name = db.Column(db.String(length=30), nullable=False, unique=True, primary_key=True) 
    location = db.Column(db.String(length=30), nullable=False) 
    price = db.Column(db.Integer(), nullable=False) 
    attend = db.Column(db.String(length=12), nullable=False ) #barcode
    description = db.Column(db.String(length=1024), nullable=False) 
    owner = db.Column(db.Integer(), db.ForeignKey('user.id')) 
    def __repr__(self):
        return f'Event {self.name}'
    
    def book(self, user):
        self.owner = user.id
        user.count += self.price  #
        db.session.commit()

    def cancel(self, user):
        self.owner = None
        user.count -= self.price  #
        db.session.commit()
        
