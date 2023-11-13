from marshmallow import fields  
from app.ext import ma   

class FilmSchema(ma.Schema):     
    id = fields.Integer(dump_only=True)     
    title = fields.String()     
    length = fields.Integer()     
    year = fields.Integer()     
    director = fields.String()     
    actors = fields.Nested('ActorSchema', many=True)   
    cinemas = fields.Method("get_cinemas_ids")
    
    def get_cinemas_ids(self, obj):
        return [cinema.cinema_id for cinema in obj.cinema_associations]

    
class ActorSchema(ma.Schema):     
    id = fields.Integer(dump_only=True)     
    name = fields.String() 
    
class CinemaSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
