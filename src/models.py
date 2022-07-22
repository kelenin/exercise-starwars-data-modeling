import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table users
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    fecha = Column(String(10), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    users_id = Column(Integer, ForeignKey('users.id'))
    users = relationship(Users)

class DatosInformation(Base):
    __tablename__ = 'datos_information'
    # Here we define columns for the table datos_information.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    planeta_id = Column(Integer, ForeignKey("planetas.id"))
    FavoritesPersonajes = Column(String(1), nullable=False)
    users = relationship(Users)

class Personaje(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table personajes.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    datosinformation = relationship(DatosInformation)

class Planeta(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table planetas.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    datosinformation = relationship(DatosInformation)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram-person-actualizada-5.png')