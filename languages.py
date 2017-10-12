from flask import Flask, url_for, render_template, request, redirect, jsonify, flash
from flask import session as login_session
import random, string

from database_setup import Base, LanguageFamily, Language, LanguageTrivium, LearningTip
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Languages App"

engine = create_engine('sqlite:///languages.db')

DBsession = sessionmaker(bind=engine)
session = DBsession()

# the Javascript code on the login page makes a POST request to this route
# in this request, the server receives the authorization code
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

@app.route('/bootstrap')
def showBoostrap():
    if login_session.get('username') != None:
        user_name = login_session['username'].split(' ')[0]
    else:
        user_name = 'Guest'
    language_families = session.query(LanguageFamily).all()
    return render_template('bootstrap-example.html', language_families=language_families, user_name=user_name)

@app.route('/')
@app.route('/index')
@app.route('/language-families')
def showMainPage():
    if login_session.get('username') != None:
        user_name = login_session['username'].split(' ')[0]
    else:
        user_name = 'guest'
    language_families = session.query(LanguageFamily).all()
    return render_template('index.html', language_families=language_families, user_name=user_name)


@app.route('/language-families/<int:family_id>')
def showLanguageFamily(family_id):
    family = session.query(LanguageFamily).filter_by(id=family_id).one()
    languages = session.query(Language).filter_by(family_id=family_id).all()
    return render_template('language-family.html', family=family, languages=languages)


@app.route('/language-families/new', methods=['GET', 'POST'])
def addLanguageFamily():
    if login_session.get('username') == None:
        flash('You need to be logged in to add language families')
        return redirect('/login')
    if login_session.get('username') == None:
        return redirect('/login')
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
    if login_session.get('username') == None:
        flash('You need to be logged in to make changes to your entries')
        return redirect('/login')
    if login_session.get('username') == None:
        return redirect('/login')
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
    if login_session.get('username') == None:
        flash('You need to be logged in to make changes to your entries')
        return redirect('/login')
    if login_session.get('username') == None:
        return redirect('/login')
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
    return render_template('language.html', family_id=family_id, language=language, tips=tips, trivia=trivia)


@app.route('/language-families/<int:family_id>/language/new', methods=['GET', 'POST'])
def addLanguage(family_id):
    if login_session.get('username') == None:
        flash('You need to be logged in to add languages')
        return redirect('/login')
    if login_session.get('username') == None:
        return redirect('/login')
    if request.method =='POST':
        new_language = Language()
        new_language.name = request.form['name']
        new_language.description = request.form['description']
        new_language.creator_id = 1
        new_language.family_id = family_id
        session.add(new_language)
        session.commit()

        # Returns last language added to database
        last_language = session.query(Language).order_by(Language.id.desc()).first()

        new_trivium = LanguageTrivium()
        new_trivium.text = request.form['trivium']
        new_trivium.language_id = last_language.id
        new_trivium.creator_id = 1

        new_tip = LearningTip()
        new_tip.text = request.form['tip']
        new_tip.language_id = last_language.id
        new_tip.creator_id = 1

        session.add(new_trivium)
        session.add(new_tip)
        session.commit()
        return redirect(url_for('showLanguageFamily', family_id=family_id))
    else:
        return render_template('addlanguage.html', family_id=family_id)


@app.route('/language-families/<int:family_id>/language/<int:language_id>/edit', methods=['GET', 'POST'])
def editLanguage(family_id, language_id):
    if login_session.get('username') == None:
        flash('You need to be logged in to make changes to your entries')
        return redirect('/login')
    if login_session.get('username') == None:
        return redirect('/login')
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
    if login_session.get('username') == None:
        flash('You need to be logged in to make changes to your entries')
        return redirect('/login')
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
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.secret_key = 'some_secret_key'
    app.debug = True
    app.run('0.0.0.0', port = 5000)
