from flask_restful import Resource, Api,reqparse,marshal_with,fields
from .models import Ad, Campaign,db
from flask import request
from flask_security import auth_required,roles_required,current_user
from datetime import datetime


api = Api(prefix='/api')



######## for campaign id 

parser = reqparse.RequestParser() #this give a data in dictionary format when client send data , it receive that data and convert it into dictionary

#validating argument of campaign
parser.add_argument('c_name', type=str,
                    help='name is required and should be a string', required=True)
parser.add_argument('description', type=str,
                    help='description is required should be a string', required=True)
parser.add_argument('start_date',type=str,required =True,help='STart date is required')
parser.add_argument('end_date',type=str,help='end date is required',required=True)
parser.add_argument('c_budget',type=int,required=True,help="budget for campaign is required")
parser.add_argument('visibility',type=bool,required=False,default=False,help='visibilty is required')

#### formatting data before getting it
campaign_field_format = {
    'id':fields.Integer,
    'c_name': fields.String,
    'description':fields.String,
    'start_date':fields.String,
    'end_date':fields.String,
    'c_budget':fields.String,
    'visibility': fields.Boolean
}

class CampaignMaterial(Resource):
    @auth_required("token")
    def get(self):
        all_campaign= Campaign.query.all()
        return all_campaign


    #@auth_required('token')  #need to integrate this
    #@roles_required('sponser')  #need to integrate this
    def post(self):
        
        if 'Authentication-Token' not in request.headers:
            return{"error":"Missing Authorization header"},400
        
        token = request.headers.get('Authentication-Token')
        
        
        
        #parse the request argument
        args=parser.parse_args()
        start_date= datetime.strptime(args['start_date'],'%Y-%m-%d').date()
        end_date = datetime.strptime(args['end_date'],'%Y-%m-%d').date()

        #create a new campaign instance
        new_campaign = Campaign(
            c_name=args.get('c_name'),
            description=args.get('description'),
            start_date=start_date,
            end_date=end_date,
            c_budget=args.get('c_budget'),
            visibility=args.get('visibility'))
        #add to session and commit to save data
        db.session.add(new_campaign)
        db.session.commit()
        return {"message":"Campaign created"}






#### for admaterial 

ad_parser = reqparse.RequestParser()
ad_parser.add_argument('campaign_id',type=int,required=True,help='campaign id is must')
ad_parser.add_argument('message',type=str,required =True,help='Message is required'),
ad_parser.add_argument('requirements',type=str,required=True,help="requirements is required"),
ad_parser.add_argument('payment_amount',type=int, required =True,help="payement details are required"),
ad_parser.add_argument('status',type=str,required=False,default='Pending',help="payement status is also required")


ad_field_format ={
    
'id':fields.Integer,
    'message':fields.String,
    'requirements':fields.String,
    'payment_amount':fields.Integer,
    'status':fields.String
}


class AdMaterial(Resource):
    
    @auth_required('token')
    def get(self):
        all_ad = Ad.query.all()

        return all_ad
    @auth_required('token')
    @roles_required('sponser')   
    def post(self):
        args= ad_parser.parse_args()
        campaign_id=args.get('campaign_id')
        print(campaign_id)
        new_ad = Ad(campaign_id=args.get('campaign_id'),
                    influencer_id=current_user.id,
                    message=args.get('message'),
                    requirements = args.get('requirements'),
                    payment_amount = args.get('payment_amount'),
                    status=args.get('status','Pending') 
                    )
        db.session.add(new_ad)
        db.session.commit()


api.add_resource(CampaignMaterial,'/campaign_material')
api.add_resource(AdMaterial,'/ad_material')
    