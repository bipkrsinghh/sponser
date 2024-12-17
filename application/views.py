import os
from flask import current_app as app,jsonify,request,render_template
from flask_security import auth_required,roles_required
from .models import db,User, Campaign,Ad
from flask_restful import marshal_with,fields,marshal
from .sec import datastore
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import datetime,date
from .tasks import say_hello
import flask_excel as excel





@app.get('/')
def home():
    #automating the process of files rendering
    transpile_dir = os.path.join(app.static_folder,'assets','assets')
    files = os.listdir(transpile_dir)

    #filter javascript and css files
    js_files = [f  for f in files if f.endswith('.js')]
    css_files = [f for f in files if f.endswith('.css')]


    #sort files by modification time

    js_files.sort(key=lambda f: os.path.getmtime(os.path.join(transpile_dir,f)),reverse=True)
    css_files.sort(key=lambda f:os.path.getmtime(os.path.join(transpile_dir,f)),reverse=True)


    #get the latest javascript and css files

    latest_js_file = js_files[0] if js_files else None
    latest_css_file = css_files[0] if css_files else None
    return render_template("index.html",js_file=latest_js_file or '',css_file = latest_css_file or '') 
    


@app.get('/admin')
@auth_required("token")
@roles_required("admin")
def admin():
    return "hello admin"

# actiavting user

@app.get('/activate/sponser_or_influncer/<int:sponser_id>')
@auth_required("token")
@roles_required("admin")
def activate_sponser(sponser_id):
    sponser = User.query.get(sponser_id)

    if not sponser or "sponser" not in sponser.roles:
        return jsonify({"message":"Sponser not found"}),404
    
    sponser.active=True
    db.session.commit()
    return jsonify({"message":"sponser activated"})

## deactivating sponser or we can generalize to user

@app.get('/deactivate/<int:id>')
@auth_required('token')
@roles_required("admin")
def deactivate(id):
    user = User.query.get(id)
    if not user :
        return jsonify({"message":"user not found"})
    
    if "sponser" not in user.roles:
        return jsonify({"message":"User is not sponser, you can't deactive it"})
        
    
    user.active = False
    db.session.commit()
    return jsonify({"message":"Sponser deactivated Successfully "})

## user login

@app.route('/user-login', methods=['POST'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message":"email not provided"}),404
    user = datastore.find_user(email=email)
    if not user:
        return jsonify({"message":"User not found"}),404
    
    if check_password_hash(user.password,data.get('password')):
        return {"token":user.get_auth_token(),"email":user.email,"role":user.roles[0].name}
    else:
        return jsonify({"message":"Wrong password"}),404
    
# user registration

@app.route('/user-register',methods=['POST'])
def registration():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({'message':'email is required for registration'}),404

    user = datastore.find_user(email=email)
    if user :
        return jsonify({"message":"this email is already registered"}),404
    
    if data.get('role')=='sponser':
        active=False
    else:
        active=True

    if not user :
        datastore.create_user(email=email,username=data.get('username'),name=data.get('name'),active=active,
                              roles=[data.get('role')],company_name= data.get('company_name'),
                              industry=data.get('industry_type'),category=data.get('category'),
                              niche=data.get('niche'),reach=data.get('reach'),password=generate_password_hash(data.get('password')))   
        db.session.commit()
        return jsonify({"message":"Successfully registered"}),200
    

#getting all user to displayed
user_fields = {
    "id":fields.Integer,
    "email":fields.String,
    "active": fields.Boolean,
    "username":fields.String,
    "company_name":fields.String,
    "industry":fields.String,
    "category":fields.String,
    "niche":fields.String,
    "reach":fields.Integer,
    "flag":fields.Integer,


}

@app.get('/users')
@auth_required("token")
@roles_required("admin")
def all_users():
    users = User.query.all()
    if len(users) == 0:
        return jsonify({"message":"no user found"})
    return marshal(users,user_fields)


campaign_fields ={
    'id':fields.Integer,
    'c_name':fields.String,
    'description':fields.String,
    'start_date':fields.DateTime,
    'end_date':fields.DateTime,
    'c_budget':fields.Integer,
    'visibility':fields.Boolean,
}
# Convert date to datetime before marshaling
def convert_date_to_datetime(date_obj):
    return datetime.combine(date_obj, datetime.min.time())


#Querying all the campaign data

@app.get('/allCampaign')
@auth_required('token')
def all_campaign():
    campaigns = Campaign.query.all()
    if len(campaigns) == 0:
        return jsonify({"message":"no campaign found"})
    else:
        for campaign in campaigns:
            if isinstance(campaign.start_date, date):
                campaign.start_date = datetime.combine(campaign.start_date,datetime.min.time())
            if isinstance(campaign.end_date, date):
                campaign.end_date = datetime.combine(campaign.end_date,datetime.min.time())


        return marshal(campaigns,campaign_fields)
    

### creating the campaign in background


@app.route('/create_campaign',methods=['POST'])
@auth_required('token')
@roles_required('sponser')
def campaigncreation():
    data = request.get_json()
    start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
    end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')
    new_campaign = Campaign(
            c_name=data.get('c_name'),
            description=data.get('description'),
            start_date=start_date,
            end_date=end_date,
            c_budget=data.get('c_budget'),
            visibility=data.get('visibility'))
        #add to session and commit to save data
    db.session.add(new_campaign)
    db.session.commit()
        
    return jsonify({"message":"Successfully created campaign"}),200

@app.get('/say-hello')
def say_hello_view():
    t = say_hello.delay()
    return jsonify({"task-id":t.id})


@app.get('/download-csv')
def download_csv():
    camp = Campaign.query.with_entities(Campaign.c_name,Campaign.c_budget,Campaign.description).all()

    csv_output = excel.make_response_from_query_sets(camp,["campaign name","Campaign Budget","Campaign Description"],"csv",filename="test1.csv")
    return csv_output