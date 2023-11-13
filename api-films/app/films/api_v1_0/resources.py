from ...db import db
from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import CinemaSchema, FilmSchema
from ..models import Cinema, Film, Actor, FilmCinema

films_v1_0_bp = Blueprint('films_v1_0_bp', __name__)
film_schema = FilmSchema()
cinema_schema = CinemaSchema()
cinemas_v1_0_bp = Blueprint('cinemas_v1_0_bp', __name__)

api = Api(films_v1_0_bp)


class FilmListResource(Resource):
    def get(self):
        actor_name = request.args.get('actor')
        if actor_name:
            films = Film.query.join(Actor).filter(Actor.name == actor_name).all()
        else:
            films = Film.get_all()
        result = film_schema.dump(films, many=True)
        return result

    def post(self):
        data = request.get_json()
        film_dict = film_schema.load(data)
        film = Film(title=film_dict['title'],
                    length=film_dict['length'],
                    year=film_dict['year'],
                    director=film_dict['director'])
        
        for actor_data in film_dict['actors']:
            actor = Actor(actor_data['name'])
            film.actors.append(actor)
            
        if 'cinemas' in film_dict:
            for cinema_id in film_dict['cinemas']:
                association = FilmCinema(film_id=film.id, cinema_id=cinema_id)
                db.session.add(association)
        film.save()
        resp = film_schema.dump(film)
        return resp, 201

class FilmResource(Resource):
    def get(self, film_id):
        film = Film.get_by_id(film_id)
        resp = film_schema.dump(film)
        return resp

class CinemaListResource(Resource):
    def get(self):
        cinemas = Cinema.get_all()
        result = cinema_schema.dump(cinemas, many=True)
        return result

    def post(self):
        data = request.get_json()
        cinema_dict = cinema_schema.load(data)
        cinema = Cinema(name=cinema_dict['name'])
        cinema.save()
        resp = cinema_schema.dump(cinema)
        return resp, 201

api.add_resource(FilmListResource, '/api/v1.0/films/', endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/v1.0/films/<int:film_id>', endpoint='film_resource')
api.add_resource(CinemaListResource, '/api/v1.0/cinemas/', endpoint='cinema_list_resource')

