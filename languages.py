from flask import Flask, render_template
from database_setup import Base, LanguageFamily, Language, LanguageTrivium, LearningTip, LearningResource, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)

engine = create_engine('sqlite:///languages.db')

DBsession = sessionmaker(bind=engine)
session = DBsession()


@app.route('/')
@app.route('/index')
@app.route('/language-families')
def showMainPage():
    language_families = session.query(LanguageFamily).all()
    return render_template('index.html', language_families=language_families)


@app.route('/language-families/<int:family_id>')
def showLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    languages = session.query(Language).filter_by(family_id=family_id).all()
    return render_template('language-family.html', family=family, languages=languages)


@app.route('/language-families/new', methods=['GET', 'POST'])
def addLanguageFamily():
    return render_template('addfamily.html')


@app.route('/language-families/<int:family_id>/edit', methods=['GET', 'POST'])
def editLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    return render_template('editfamily.html', family=family)


@app.route('/language-families/<int:family_id>/delete', methods=['GET', 'POST'])
def deleteLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    return render_template('deletefamily.html', family=family)


@app.route('/language-families/<int:family_id>/language/<int:language_id>')
def showLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    tips = session.query(LearningTip).filter_by(language_id=language_id).all()
    trivia = session.query(LanguageTrivium).filter_by(language_id=language_id).all()
    resources = session.query(LearningResource).filter_by(language_id=language_id).all()
    return render_template('language.html', family_id=family_id, language=language, tips=tips, trivia=trivia, resources=resources)


@app.route('/language-families/<int:family_id>/language/new', methods=['GET', 'POST'])
def addLanguage(family_id):
    return render_template('addlanguage.html', family_id=family_id)


@app.route('/language-families/<int:family_id>/language/<int:language_id>/edit', methods=['GET', 'POST'])
def editLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    return render_template('editlanguage.html', family_id=family_id, language=language)

@app.route('/language-families/<int:family_id>/language/<int:language_id>/delete', methods=['GET', 'POST'])
def deleteLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    return render_template('deletelanguage.html', family_id=family_id, language=language)


@app.route('/login')
def showLoginPage():
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
