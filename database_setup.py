from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from sqlalchemy.orm import relationship

Base = declarative_base()

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

    @property
    def serialize(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'picture_url': self.picture_url,
            'password_hash': self.password_hash
        }

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

    creator = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'creator_id': self.creator_id
        }


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

    creator = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'family_id': self.family_id,
            'creator_id': self.creator_id
        }

class LanguageTrivium(Base):
    __tablename__ = 'language_trivia'

    id = Column(
    Integer, primary_key = True)

    text = Column(
    String(1000), nullable = False)

    language_id = Column(
    Integer, ForeignKey('languages.id'))

    language = relationship(Language)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'language_id': self.language_id,
            'creator_id': self.creator_id
        }

class LearningTip(Base):
    __tablename__ = 'learning_tips'

    id = Column(
    Integer, primary_key = True)

    text = Column(
    String(1000), nullable = False)

    language_id = Column(
    Integer, ForeignKey('languages.id'))

    language = relationship(Language)

    creator_id = Column(
    Integer, ForeignKey('users.id'))

    creator = relationship(User)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'language_id': self.language_id,
            'creator_id': self.creator_id
        }

    @property
    def serialize(self):
        return {
            'id': self.id,
            'text': self.text,
            'url': self.url,
            'language_id': self.language_id,
            'creator_id': self.creator_id
        }

engine = create_engine('postgresql:///languages')
Base.metadata.create_all(bind=engine)
