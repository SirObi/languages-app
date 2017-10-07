from database_setup import Base, LanguageFamily, Language, LanguageTrivium, LearningTip, LearningResource, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



language_families = [
    {'id': 1, 'name': 'Germanic', 'description': 'Germanic languages are so much fun',
    'creator_id': 1},
    {'id': 2, 'name': 'Romance', 'description': 'Romance languages are so much fun',
    'creator_id': 1},
    {'id': 3, 'name': 'Slavic', 'description': 'Slavic languages are so much fun',
    'creator_id': 1}]

languages = [{'id': 1, 'name': 'English', 'family_id': 1,
            'description': 'English is a super cool and old language',
            'creator_id': 1},
            {'id': 2, 'name': 'German', 'family_id': 1,
            'description': 'German is a super cool and old language',
            'creator_id': 1},
            {'id': 3, 'name': 'Italian', 'family_id': 2,
            'description': 'Italian is a super cool and old language',
            'creator_id': 1},
            {'id': 4, 'name': 'French', 'family_id': 2,
            'description': 'French is a super cool and old language',
            'creator_id': 1},
            {'id': 5, 'name': 'Russian', 'family_id': 3,
            'description': 'Russian is a super cool and old language',
            'creator_id': 1},
            {'id': 6, 'name': 'Polish', 'family_id': 3,
            'description': 'Polish is a super cool and old language',
            'creator_id': 1}]

trivia = [
    {'id': 1, 'text': 'some English trivia', 'language_id': 1, 'creator_id': 1},
    {'id': 2, 'text': 'some English trivia', 'language_id': 1, 'creator_id': 1},
    {'id': 3, 'text': 'some German trivia', 'language_id': 2, 'creator_id': 1},
    {'id': 4, 'text': 'some German trivia', 'language_id': 2, 'creator_id': 1},
    {'id': 5, 'text': 'some Italian trivia', 'language_id': 3, 'creator_id': 1},
    {'id': 6, 'text': 'some Italian trivia', 'language_id': 3, 'creator_id': 1},
    {'id': 7, 'text': 'some French trivia', 'language_id': 4, 'creator_id': 1},
    {'id': 8, 'text': 'some French trivia', 'language_id': 4, 'creator_id': 1},
    {'id': 9, 'text': 'some Russian trivia', 'language_id': 5, 'creator_id': 1},
    {'id': 10, 'text': 'some Russian trivia', 'language_id': 5, 'creator_id': 1},
    {'id': 11, 'text': 'some Polish trivia', 'language_id': 6, 'creator_id': 1},
    {'id': 12, 'text': 'some Polish trivia', 'language_id': 6, 'creator_id': 1}
    ]

tips = [
    {'id': 1, 'text': 'some English tip', 'language_id': 1, 'creator_id': 1},
    {'id': 2, 'text': 'some English tip', 'language_id': 1, 'creator_id': 1},
    {'id': 3, 'text': 'some German tip', 'language_id': 2, 'creator_id': 1},
    {'id': 4, 'text': 'some German tip', 'language_id': 2, 'creator_id': 1},
    {'id': 5, 'text': 'some Italian tip', 'language_id': 3, 'creator_id': 1},
    {'id': 6, 'text': 'some Italian tip', 'language_id': 3, 'creator_id': 1},
    {'id': 7, 'text': 'some French tip', 'language_id': 4, 'creator_id': 1},
    {'id': 8, 'text': 'some French tip', 'language_id': 4, 'creator_id': 1},
    {'id': 9, 'text': 'some Russian tip', 'language_id': 5, 'creator_id': 1},
    {'id': 10, 'text': 'some Russian tip', 'language_id': 5, 'creator_id': 1},
    {'id': 11, 'text': 'some Polish tip', 'language_id': 6, 'creator_id': 1},
    {'id': 12, 'text': 'some Polish tip', 'language_id': 6, 'creator_id': 1}
    ]

learning_resources = [
    {'id': 1, 'text': 'some English resource', 'url': '#', 'language_id': 1, 'creator_id': 1},
    {'id': 2, 'text': 'some English resource', 'url': '#', 'language_id': 1, 'creator_id': 1},
    {'id': 3, 'text': 'some German resource', 'url': '#', 'language_id': 2, 'creator_id': 1},
    {'id': 4, 'text': 'some German resource', 'url': '#', 'language_id': 2, 'creator_id': 1},
    {'id': 5, 'text': 'some Italian resource', 'url': '#', 'language_id': 3, 'creator_id': 1},
    {'id': 6, 'text': 'some Italian resource', 'url': '#', 'language_id': 3, 'creator_id': 1},
    {'id': 7, 'text': 'some French resource', 'url': '#', 'language_id': 4, 'creator_id': 1},
    {'id': 8, 'text': 'some French resource', 'url': '#', 'language_id': 4, 'creator_id': 1},
    {'id': 9, 'text': 'some Russian resource', 'url': '#', 'language_id': 5, 'creator_id': 1},
    {'id': 10, 'text': 'some Russian resource', 'url': '#', 'language_id': 5, 'creator_id': 1},
    {'id': 11, 'text': 'some Polish resource', 'url': '#', 'language_id': 6, 'creator_id': 1},
    {'id': 12, 'text': 'some Polish resource', 'url': '#', 'language_id': 6, 'creator_id': 1}
    ]


engine = create_engine('sqlite:///languages.db')

DBsession = sessionmaker(bind=engine)

session = DBsession()



user = User(
        first_name = 'John', last_name = 'Smith',
        picture_url = '#', password_hash = '12345')
session.add(user)
session.commit()


for family in language_families:
    lf = LanguageFamily()
    lf.name = family['name']
    lf.description = family['description']
    lf.creator_id = family['creator_id']
    session.add(lf)
    session.commit()

for language in languages:
    l = Language()
    l.name = language['name']
    l.description = language['description']
    l.family_id = language['family_id']
    l.creator_id = language['creator_id']
    session.add(l)
    session.commit()

for trivium in trivia:
    t = LanguageTrivium()
    t.text = trivium['text']
    t.language_id = trivium['language_id']
    t.creator_id = trivium['creator_id']
    session.add(t)
    session.commit()

for tip in tips:
    lt = LearningTip()
    lt.text = tip['text']
    lt.language_id = tip['language_id']
    lt.creator_id = tip['creator_id']
    session.add(lt)
    session.commit()

for resource in learning_resources:
    lr = LearningResource()
    lr.text = resource['text']
    lr.url = resource['url']
    lr.language_id = resource['language_id']
    lr.creator_id = resource['creator_id']
    session.add(lr)
    session.commit()

print "database populated"
