import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
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
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    fecha = Column(Date, nullable=False)

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

class Personaje(Base):
    __tablename__ = 'personajes'
    # Here we define columns for the table personajes.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)

class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table favoritos.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(Users)
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    personaje = relationship(Personaje)

class Planeta(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table planetas.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    description = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table planetas.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    description = Column(String(250), nullable=False)
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    personaje = relationship(Personaje)
    planeta_id = Column(Integer, ForeignKey("planetas.id"))
    planeta = relationship(Planeta)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(Users)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')