from marshmallow import fields  
from app.ext import ma   

class FilmSchema(ma.Schema):     
    id = fields.Integer(dump_only=True)     
    title = fields.String()     
    length = fields.Integer()     
    year = fields.Integer()     
    director = fields.String()   
    cinema_id = fields.Integer(load_only=True)  
    actors = fields.Nested('ActorSchema', many=True)   
    cinema = fields.Nested('CinemaSchema')
    
class ActorSchema(ma.Schema):     
    id = fields.Integer(dump_only=True)     
    name = fields.String() 
    
class CinemaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
