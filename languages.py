from flask import Flask, render_template

app = Flask(__name__)

#Fake data
language_families = [{'id': 0, 'name': 'Germanic', 'description': 'Germanic languages are so much fun'}, {'id': 1, 'name': 'Romance', 'description': 'Romance languages are so much fun'}, {'id': 2, 'name': 'Slavic', 'description': 'Slavic languages are so much fun'}]
languages = [{'id': 0, 'name': 'English', 'language_family': 0,
            'description': 'English is a super cool and old language',
            'trivia': [
                {'id': 1, 'text': 'some English trivia'},
                {'id': 2, 'text': 'some English trivia'}],
                'tips': [
                {'id': 1, 'text': 'some English tip'},
                {'id': 2, 'text': 'some English tip'}],
                'learning-resources': [
                {'id': 1, 'text': 'some English resource'},
                {'id': 2, 'text': 'some English resource'}]
            },
            {'id': 1, 'name': 'German', 'language_family': 0,
            'description': 'German is a super cool and old language',
            'trivia': [
                {'id': 3, 'text': 'some German trivia'},
                {'id': 4, 'text': 'some German trivia'}],
                'tips': [
                {'id': 3, 'text': 'some German tip'},
                {'id': 4, 'text': 'some German tip'}],
                'learning-resources': [
                {'id': 3, 'text': 'some German resource'},
                {'id': 4, 'text': 'some German resource'}]
            },
            {'id': 2, 'name': 'Italian', 'language_family': 1,
            'description': 'Italian is a super cool and old language',
            'trivia': [
                {'id': 5, 'text': 'some Italian trivia'},
                {'id': 6, 'text': 'some Italian trivia'}],
                'tips': [
                {'id': 5, 'text': 'some Italian tip'},
                {'id': 6, 'text': 'some Italian tip'}],
                'learning-resources': [
                {'id': 5, 'text': 'some Italian resource'},
                {'id': 6, 'text': 'some Italian resource'}]
            },
            {'id': 3, 'name': 'French', 'language_family': 1,
            'description': 'French is a super cool and old language',
            'trivia': [
                {'id': 7, 'text': 'some French trivia'},
                {'id': 8, 'text': 'some French trivia'}],
                'tips': [
                {'id': 7, 'text': 'some French tip'},
                {'id': 8, 'text': 'some French tip'}],
                'learning-resources': [
                {'id': 7, 'text': 'some French resource'},
                {'id': 8, 'text': 'some French resource'}]
            },
            {'id': 4, 'name': 'Russian', 'language_family': 2,
            'description': 'Russian is a super cool and old language',
            'trivia': [
                {'id': 9, 'text': 'some Russian trivia'},
                {'id': 10, 'text': 'some Russian trivia'}],
                'tips': [
                {'id': 9, 'text': 'some Russian tip'},
                {'id': 10, 'text': 'some Russian tip'}],
                'learning-resources': [
                {'id': 9, 'text': 'some Russian resource'},
                {'id': 10, 'text': 'some Russian resource'}]
            },
            {'id': 5, 'name': 'Polish', 'language_family': 2,
            'description': 'Polish is a super cool and old language',
            'trivia': [
                {'id': 11, 'text': 'some Polish trivia'},
                {'id': 12, 'text': 'some Polish trivia'}],
                'tips': [
                {'id': 11, 'text': 'some Polish tip'},
                {'id': 12, 'text': 'some Polish tip'}],
                'learning-resources': [
                {'id': 11, 'text': 'some Polish resource'},
                {'id': 12, 'text': 'some Polish resource'}]
            },
            ]




@app.route('/')
@app.route('/index')
@app.route('/language-families')
def showMainPage():
    return render_template('index.html', language_families=language_families)


@app.route('/language-families/<int:family_id>')
def showLanguageFamily(family_id):
    return render_template('language-family.html', language_families=language_families, family_id=family_id, languages=languages)


@app.route('/language-families/new')
def addLanguageFamily():
    return render_template('addfamily.html')


@app.route('/language-families/<int:family_id>/edit')
def editLanguageFamily(family_id):
    return render_template('editfamily.html', family_id=family_id, language_families=language_families)


@app.route('/language-families/<int:family_id>/delete')
def deleteLanguageFamily(family_id):
    return render_template('deletefamily.html', family_id=family_id, language_families=language_families)


@app.route('/language-families/<int:family_id>/language/<int:language_id>')
def showLanguage(family_id, language_id):
    return render_template('language.html', family_id=family_id, language_id=language_id, languages=languages)


@app.route('/language-families/<int:family_id>/language/new')
def addLanguage(family_id):
    return render_template('addlanguage.html', family_id=family_id)


@app.route('/language-families/<int:family_id>/language/<int:language_id>/edit')
def editLanguage(family_id, language_id):
    return render_template('editlanguage.html', family_id=family_id, language_id=language_id, languages=languages)

@app.route('/language-families/<int:family_id>/language/<int:language_id>/delete')
def deleteLanguage(family_id, language_id):
    return render_template('deletelanguage.html', family_id=family_id, language_id=language_id, languages=languages)


@app.route('/login')
def showLoginPage():
    return render_template('login.html')


if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', port = 5000)
