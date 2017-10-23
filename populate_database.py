from database_setup import Base, LanguageFamily, Language, LanguageTrivium
from database_setup import LearningTip, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

language_families = [
    {'id': 1, 'name': 'Germanic',
        'description': 'Germanic languages are so much fun',
        'creator_id': 1},
    {'id': 2, 'name': 'Romance',
        'description': 'Romance languages are so much fun',
        'creator_id': 1},
    {'id': 3, 'name': 'Slavic',
        'description': 'Slavic languages are so much fun',
        'creator_id': 1}]

languages = [
    {'id': 1, 'name': 'English', 'family_id': 1,
        'description': 'English is a super cool and old language.'
        ' Just don\'t say it in France.', 'creator_id': 1},
    {'id': 2, 'name': 'German', 'family_id': 1,
        'description': 'German comes in many flavours and is an official '
        'language in six countries', 'creator_id': 1},
    {'id': 3, 'name': 'Italian', 'family_id': 2, 'description': 'You '
        'gotta love Italian', 'creator_id': 1},
    {'id': 4, 'name': 'French', 'family_id': 2, 'description': 'French is a '
        'super cool and old language. Just don\'t say it in the UK.',
        'creator_id': 1},
    {'id': 5, 'name': 'Russian', 'family_id': 3, 'description': 'Russian is '
        'the most widely spoken Slavic language in the world. It\'s spoken by '
        '260 million people!', 'creator_id': 1},
    {'id': 6, 'name': 'Polish', 'family_id': 3, 'description': 'Polish is the '
        'most widely spoken West Slavic language ', 'creator_id': 1}]

trivia = [
    {'id': 1, 'text': 'English is a so called "stress-timed" language. It '
        'means that when you say a sentence, certain words are pronounced '
        'louder and clearer - this makes it easy for the other person to hear '
        'the important words in the sentence.', 'language_id': 1,
        'creator_id': 1},
    {'id': 2, 'text': 'Since English was influenced by many languages over '
        'the centuries, it often has synonyms for the same thing or action '
        'that come from different languages. Usually the pairing is such that '
        'the Latin/French word is used in more formal context, and its '
        'synonym is usually shorter, and more common in everyday speech. '
        'Examples: receive - get, aspire - hope, apprehend - stop, '
        'preoccupy - worry. If you think English sometimes doesn\'t make '
        'sense - well, it\'s not supposed to!', 'language_id': 1,
        'creator_id': 1},
    {'id': 3, 'text': 'German spoken in Switzerland is much different from '
        'German spoken in Germany. So much so, that "High German" (i.e. '
        'German from Germany) is taught in Swiss schools as a foreign '
        'language. Most Swiss speakers of German communicate in a dialect '
        'on a daily basis.', 'language_id': 2, 'creator_id': 1},
    {'id': 4, 'text': 'Even though Swiss people usually prefer to use their '
        'own dialect when speaking, almost all Swiss books are written in '
        'High German. The reason for that? Martin Luther, the father of '
        'Protestantism, was German. He also authored one of the first '
        'translations of the Bible from Greek into German (previously bibles '
        'were only available in Greek, Latin and Hebrew, so common people in '
        'Europe could not read them). Since Switzerland was one of the first '
        'countries to convert to this new branch of Christianity, Protestant '
        'bibles were in huge demand. Luther\'s Bible, written in High German, '
        'started the culture of readership in Switzerland - somehow, after '
        'that, the local dialects never managed to catch on as something '
        'people would write books in.', 'language_id': 2, 'creator_id': 1},
    {'id': 5, 'text': 'Even though half of the world uses the Italian '
        'word "Ciao" ("Hello"), Italians have many other informal greetings '
        'such as "Weila" ("Hiya") or "Ehi" ("Hey").', 'language_id': 3,
        'creator_id': 1},
    {'id': 6, 'text': 'Italian comes from Latin and so does Romanian (or '
        'Wallachian as it used to be called back in the day). Both languages '
        'share many similarities because of that. This was apparently a '
        'source of great confusion to medieval Poles: up to this day, even '
        'though the whole world uses some variation of the word "Italian" '
        'or "Italy", Poles say "wloski" and "Wlochy".', 'language_id': 3,
        'creator_id': 1},
    {'id': 7, 'text': 'The throaty "r" sound that French is commonly '
        'associated with didn\'t use to be part of the language. People '
        'started using it only around the 17th century', 'language_id': 4,
        'creator_id': 1},
    {'id': 8, 'text': '''Sometimes on wine bottles from France, you see the '
        'words "Pays d'Oc". This roughly means: "Southern France". More '
        'specifically, it refers to the regions where people say "Oc." to '
        'mean "Yes.". In the north of France, the standard word for "Yes" '
        'is "Oui" (or "Oil", back in the day). Therefore, this part of '
        'France is known as the "Pays d'Oil".''', 'language_id': 4,
        'creator_id': 1},
    {'id': 9, 'text': 'Did you know that the Russian language is related to '
        'Danish? If that seems impossible, look at how both languages '
        'say "down the road". Russian: "Po doroge". Danish: "Pa gade". This '
        'becomes less surprising when you consider that medieval Russia was '
        'founded by traders and warriors from Scandinavia.', 'language_id': 5,
        'creator_id': 1},
    {'id': 10, 'text': 'There\'s a rather bizarre expression in Russian, '
        'namely: "Da nyeeeet!". "Da" means "yes" and "nyet" means "no", but '
        'when combined together in this phrase they mean "But of course not!"',
        'language_id': 5, 'creator_id': 1},
    {'id': 11, 'text': 'The name "Polish" comes from the word "pole" '
        '(pronounced: polleh), which means "field".', 'language_id': 6,
        'creator_id': 1},
    {'id': 12, 'text': 'Even though most of the world calls Germans, '
        'well, "Germans", the Polish word for them is "Niemcy" '
        '- "those who cannot speak."', 'language_id': 6, 'creator_id': 1}
    ]

tips = [
    {'id': 1, 'text': 'Do you struggle with the "a" sound in English, like '
        'in "had" or "pack"? Say "eh" a couple of times, like in the '
        'words "head" or "peck". Now say "head" and "peck "again, but this '
        'time, open your mouth much wider when you say the word. You should '
        'hear "had" and "pack" now!', 'language_id': 1, 'creator_id': 1},
    {'id': 2, 'text': 'Jus enjoy studying it. It\'s a fantastic, immensely '
        'expressive language', 'language_id': 1, 'creator_id': 1},
    {'id': 3, 'text': 'The German sound "ch", as in "ich" or "Milch" is '
        'sometimes difficult to say. However, there\'s one tip that makes it '
        'easier. You just need to remember that the German "ch" sound is the '
        'same as the "y" sound in English ("young", "Roy"), just without the '
        'vibration in your throat. It\'s the same kind of difference as '
        'between "t" and "d".', 'language_id': 2, 'creator_id': 1},
    {'id': 4, 'text': 'Germans don\'t use the future tense as often as '
        'English speakers do. Intentions and plans are usually expressed in '
        'the present tense. If you want tell someone "I will come tomorrow", '
        'you can simply say "Ich komme morgen" (lit. "I come tomorrow").',
        'language_id': 2, 'creator_id': 1},
    {'id': 5, 'text': 'If English is your native language, you probably know '
        'more Italian words than you realize. Try to guess the meaning of the '
        'following words "citta", "occupato", "aeroporto".', 'language_id': 3,
        'creator_id': 1},
    {'id': 6, 'text': '''If you want to learn to roll your "r's" like '
        'Italians do, take the first sound of the English word "day", and '
        'pronounce it many times as fast as you can. With some luck, you'll '
        'hear your tongue flap at some point, producing the "r" sound.''',
        'language_id': 3, 'creator_id': 1},
    {'id': 7, 'text': 'I honestly don\'t know much about the French language',
        'language_id': 4, 'creator_id': 1},
    {'id': 8, 'text': 'If you\'re a student of French, or a French speaker, '
        'could you teach me something interesting?', 'language_id': 4,
        'creator_id': 1},
    {'id': 9, 'text': 'Russian language does not require its speakers to use '
        'the verb "to be". "I am hungry" is expressed as "Ya goloden" '
        '(lit. "I hungry"). "Is he here?" also requires only two '
        'words: "On zdes?" (lit. "He here?"). Neat, isn\'t it? ',
        'language_id': 5, 'creator_id': 1},
    {'id': 10, 'text': 'Na zdorovye!', 'language_id': 5, 'creator_id': 1},
    {'id': 11, 'text': 'While Polish may be easier to learn for native '
        'speakers of other Slavic languages, sometimes having similar words '
        'in your language can lead to funny misunderstandings. If a Russian '
        'person walks into a bakery in Poland and asks for fresh ("cherstvy") '
        'bread, the baker is likely to be delighted - not many people want to '
        'buy stale ("czerstwy") bread these days. ', 'language_id': 6,
        'creator_id': 1},
    {'id': 12, 'text': 'Polish words may look scary at first, with all '
        'the "z" letters in weird places. They become much easier to read '
        'out loud if you realize "cz" is the same as the '
        'English "ch" and "sz" is just a good old "sh". ', 'language_id': 6,
        'creator_id': 1}
    ]


engine = create_engine('postgresql:///languages')

DBsession = sessionmaker(bind=engine)

session = DBsession()


def makeInitialUser():
    user = User(first_name='John', last_name='Smith',
                picture_url='#', password_hash='12345')
    session.add(user)
    session.commit()


def populateLanguageFamilies():
    for family in language_families:
        lf = LanguageFamily()
        lf.name = family['name']
        lf.description = family['description']
        lf.creator_id = family['creator_id']
        session.add(lf)
        session.commit()


def populateLanguages():
    for language in languages:
        l = Language()
        l.name = language['name']
        l.description = language['description']
        l.family_id = language['family_id']
        l.creator_id = language['creator_id']
        session.add(l)
        session.commit()


def populateTrivia():
    for trivium in trivia:
        t = LanguageTrivium()
        t.text = trivium['text']
        t.language_id = trivium['language_id']
        t.creator_id = trivium['creator_id']
        session.add(t)
        session.commit()


def populateTips():
    for tip in tips:
        lt = LearningTip()
        lt.text = tip['text']
        lt.language_id = tip['language_id']
        lt.creator_id = tip['creator_id']
        session.add(lt)
        session.commit()

makeInitialUser()
populateLanguageFamilies()
populateLanguages()
populateTrivia()
populateTips()

print "database populated"
