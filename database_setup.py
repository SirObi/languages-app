from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

class LanguageFamily(Base):
    __tablename__ = 'language_families'

    id = Column(
    Integer, primary_key = True)

    name = Column(
    String(80), nullable = False)

    description = Column(
    String(1000), nullable = False)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship('users')

class Language(Base):
    __tablename__ = 'languages'

    id = Column(
    Integer, primary_key = True)

    name = Column(
    String(80), nullable = False)

    description = Column(
    String(1000), nullable = False)

    family_id = Column(
    Integer, ForeignKey('language_families.id'))

    family = relationship(LanguageFamily)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship('users')

class LanguageTrivium(Base):
    __tablename__ = 'language_trivia'

    id = Column(
    Integer, primary_key = True)

    text = Column(
    String(400), nullable = False)

    language_id = Column(
    Integer, ForeignKey('languages.id'))

    language = relationship(Language)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship('users')


class LearningTip(Base):
    __tablename__ = 'learning_tips'

    id = Column(
    Integer, primary_key = True)

    text = Column(
    String(400), nullable = False)

    language_id = Column(
    Integer, ForeignKey('languages.id'))

    language = relationship(Language)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship('users')


class LearningResource(Base):
    __tablename__ = 'learning-resources'

    id = Column(
    Integer, primary_key = True)

    text = Column(
    String(80), nullable = False)

    url = Column(
    String(80), nullable = False)

    language_id = Column(
    Integer, ForeignKey('languages.id'))

    language = relationship(Language)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship('users')

class User(Base):
    __tablename__ = 'users'

    id = Column(
    Integer, primary_key = True)

    first_name = Column(
    String(100), nullable = False)

    last_name = Column(
    String(100), nullable = False)

    picture_url = Column(
    String(100), nullable = False)

    password_hash = Column(
    String(100), nullable = False)


engine = create_engine('sqlite:///languages.db')
Base.metadata.create_all(bind=engine)
