from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin,RoleMixin
import uuid

db = SQLAlchemy()


#establishing many to many relationship between roles and users
class RolesUsers(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    user_id = db.Column('user_id',db.Integer(),db.ForeignKey('user.id'))
    role_id=db.Column('role_id',db.Integer,db.ForeignKey('role.id'))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True,nullable= False)
    password = db.Column(db.String(255))
    name = db.Column(db.String,nullable=True)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    company_name = db.Column(db.String(255),nullable=True)
    industry= db.Column(db.String(255),nullable=True)
    category = db.Column(db.String(255),nullable=True)
    niche = db.Column(db.String(255),nullable=True)
    reach = db.Column(db.Integer,nullable=True)
    flag=db.Column(db.Boolean,default=False)
    roles = db.relationship("Role",secondary='roles_users',backref=db.backref('users',lazy='dynamic'))
    


   
class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    

class Campaign(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    c_name = db.Column(db.String(255),unique=True,nullable=False)
    description = db.Column(db.String(255),nullable = False)
    start_date = db.Column(db.Date,nullable=False)
    end_date = db.Column(db.Date,nullable= False) 
    c_budget = db.Column(db.Integer,nullable = False)
    flag=db.Column(db.Boolean,default=False)
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    visibility = db.Column(db.Boolean(),default=False)# False for public, 0 for public
    campaign_ads = db.relationship("Ad",backref='campaign')


class Ad(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    campaign_id = db.Column(db.Integer,db.ForeignKey('campaign.id'))
    creator_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    influencer_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    message = db.Column(db.String(255),nullable = True)
    requirements = db.Column(db.String(255),nullable = False)
    payment_amount=db.Column(db.Integer,nullable = False)
    status = db.Column(db.String(255),nullable = False, default="Pending")
    flag=db.Column(db.Boolean,default=False)

   