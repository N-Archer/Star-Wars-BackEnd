from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favorite = db.relationship('Favorite', backref='user')

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character', backref='Favorite', lazy=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    planet = db.relationship('Planet', backref='Favorite', lazy=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'))
    vehicle = db.relationship('Vehicle', backref='Favorite', lazy=True)

# Favorite 
# -
# ID PK int
# UserID int FK >- User.UserId
# Entity int 

# User
# -
# UserID PK int 
# UserName string unique
# EmailAddress string unique

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, primary_key=True)
    # favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))

# Character
# -
# ID PK int 
# Favorite int FK -< Favorite.Id
# CharacterName string unique
# Stats string

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, primary_key=True)
    # favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))

# Planet
# -
# ID PK int 
# Favorite int FK -< Favorite.Id
# PlanetName string unique
# Stats string

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    # favorite_id = db.Column(db.Integer, db.ForeignKey('favorite.id'))

# Vehicle
# -
# ID PK int 
# Favorite int FK -< Favorite.Id
# VehicleName string unique
# Stats string












