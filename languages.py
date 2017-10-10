from flask import Flask, url_for, render_template, request, redirect, jsonify
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
    if request.method == 'POST':
        newFamily = LanguageFamily()
        newFamily.name = request.form['name']
        newFamily.description = request.form['description']
        newFamily.creator_id = 1
        session.add(newFamily)
        session.commit()
        # the above line will have to be changed in the future
        # when we start using the session object
        return redirect(url_for('showMainPage'))
    else:
        return render_template('addfamily.html')


@app.route('/language-families/<int:family_id>/edit', methods=['GET', 'POST'])
def editLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    if request.method == 'POST':
        family.name = request.form['name']
        family.description = request.form['description']
        session.add(family)
        session.commit()
        return redirect(url_for('showLanguageFamily', family_id = family_id))
    else:
        return render_template('editfamily.html', family=family)


@app.route('/language-families/<int:family_id>/delete', methods=['GET', 'POST'])
def deleteLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    if request.method =='POST':
        session.delete(family)
        session.commit()
        return redirect(url_for('showMainPage'))
    else:
        return render_template('deletefamily.html', family=family)

@app.route('/language-families/JSON')
def languageFamiliesJSON():
    families = session.query(LanguageFamily).all()
    return jsonify(LanguageFamilies=[lf.serialize for lf in families])

@app.route('/language-families/<int:family_id>/JSON')
def languageFamilyJSON(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    languages = session.query(Language).filter_by(family_id=family_id).all()
    return jsonify(LanguageFamily=[family.serialize], Languages=[l.serialize for l in languages])

@app.route('/language-families/<int:family_id>/language/<int:language_id>')
def showLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    tips = session.query(LearningTip).filter_by(language_id=language_id).all()
    trivia = session.query(LanguageTrivium).filter_by(language_id=language_id).all()
    resources = session.query(LearningResource).filter_by(language_id=language_id).all()
    return render_template('language.html', family_id=family_id, language=language, tips=tips, trivia=trivia, resources=resources)


@app.route('/language-families/<int:family_id>/language/new', methods=['GET', 'POST'])
def addLanguage(family_id):
    if request.method =='POST':
        new_language = Language()
        new_language.name = request.form['name']
        new_language.description = request.form['description']
        new_language.family_id = family_id
        new_language.creator_id = 1
        session.add(new_language)
        session.commit()
        return redirect(url_for('showLanguageFamily', family_id=family_id))
    else:
        return render_template('addlanguage.html', family_id=family_id)


@app.route('/language-families/<int:family_id>/language/<int:language_id>/edit', methods=['GET', 'POST'])
def editLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    if request.method =='POST':
        language.name = request.form['name']
        language.description = request.form['description']
        session.add(language)
        session.commit()
        return redirect(url_for('showLanguageFamily', family_id=family_id))
    else:
        return render_template('editlanguage.html', family_id=family_id, language=language)

@app.route('/language-families/<int:family_id>/language/<int:language_id>/delete', methods=['GET', 'POST'])
def deleteLanguage(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    if request.method =='POST':
        session.delete(language)
        session.commit()
        return redirect(url_for('showLanguageFamily', family_id=family_id))
    else:
        return render_template('deletelanguage.html', family_id=family_id, language=language)

@app.route('/language-families/<int:family_id>/language/<int:language_id>/JSON')
def languageJSON(family_id, language_id):
    language = session.query(Language).filter_by(id=language_id).one()
    return jsonify(Language=[language.serialize])

@app.route('/login')
def showLoginPage():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
