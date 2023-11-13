from app.db import db, BaseModelMixin   

class Film(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)     
    length = db.Column(db.Integer)     
    year = db.Column(db.Integer)    
    director = db.Column(db.String)     
    actors = db.relationship('Actor', backref='film', lazy=False, cascade='all, delete-orphan')     
    cinema_associations = db.relationship('FilmCinema', back_populates='film')  
      
    def __init__(self, title, length, year, director, actors=[], cinemas=[]):         
        self.title = title         
        self.length = length         
        self.year = year         
        self.director = director         
        self.actors = actors   
        self.cinemas = cinemas   

    def __repr__(self):         
        return f'Film({self.title})'      

    def __str__(self):         
        return f'{self.title}'   

class Actor(db.Model, BaseModelMixin):     
    id = db.Column(db.Integer, primary_key=True)      
    name = db.Column(db.String)     
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), nullable=False)      
    
    def __init__(self, name):         
        self.name = name      
    
    def __repr__(self):         
        return f'Actor({self.name})'      
    
    def __str__(self):         
        return f'{self.name}'
    
class Cinema(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    film_associations = db.relationship('FilmCinema', back_populates='cinema')

    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Cinema({self.name})'

    def __str__(self):
        return self.name
        
class FilmCinema(db.Model, BaseModelMixin):
    film_id = db.Column(db.Integer, db.ForeignKey('film.id'), primary_key=True)
    cinema_id = db.Column(db.Integer, db.ForeignKey('cinema.id'), primary_key=True)
    film = db.relationship('Film', back_populates='cinema_associations')
    cinema = db.relationship('Cinema', back_populates='film_associations')