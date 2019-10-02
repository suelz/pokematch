"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

app.secret_key = "Aduw\yahuwAHDWUAd21adBHJK"

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from flask_login import LoginManager
login = LoginManager()
login.init_app(app)

from .models import *

db.create_all()

from werkzeug.security import generate_password_hash
"""
{'long':41.8995, 'lat':87.9403},
{'long':41.8898, 'lat':87.9890},
{'long':41.8398, 'lat':87.9536},
{'long':41.8239, 'lat':87.8517}
"""
#1
moltres = User(name="Moltres",
            email="moltres@gmail.com",
            password=generate_password_hash("password"),
            bio="One of the legendary bird Pokémon. It is said that its appearance indicates the coming of spring",
            birthday=datetime(year=1997,month=1,day=1),
            distance=10,
            gender="female",
            preference="male",
            min=40,
            max=100,
            lat=87.9403,
            long=41.8995,
            picture="moltres.jpg")

bulbasaur = User(name="Bulbasaur", 
         email="bulbasuar@gmail.com", 
         password = generate_password_hash("password"),
         bio="A strange seed was planted on its back at birth. The plant sprouts and grows with this POKéMON",
         birthday=datetime(year=1993,month=11,day=12),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.9403,
         long=41.8995,
         picture="bulbasaur.jpg")

pikachu = User(name="Pikachu", 
         email="pikachu@gmail.com", 
         password = generate_password_hash("password"),
         bio="pikapika - Japanese for a ‘sparkle’ sound",
         birthday=datetime(year=1996,month=10,day=18),
         distance=100,
         gender="male",
         preference="both",
         min=18,
         max=100,
         lat=87.9403,
         long=41.8995,
         picture="pikachu.jpg")

charmeleon = User(name="Charmeleon", 
         email="charmeleon@gmail.com", 
         password = generate_password_hash("password"),
         bio="When it swings its burning tail, it elevates the temperature to unbearably high levels.",
         birthday=datetime(year=1997,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat= 87.9890,
         long=41.8898,
         picture="charmeleon.jpg")

blastoise = User(name="Blastoise", 
         email="blastoise@gmail.com", 
         password = generate_password_hash("password"),
         bio="The rocket cannons on its shell fire jets of water capable of punching holes through thick steel.i",
         birthday=datetime(year=2000,month=10,day=18),
         distance=10,
         gender="female",
         preference="both",
         min=40,
         max=100,
         lat= 87.9890,
         long=41.8898,
         picture="blastoise.jpg")

#5
caterpie = User(name="Caterpie", 
         email="caterpie@gmail.com", 
         password = generate_password_hash("password"),
         bio="Its short feet are tipped with suction pads that enable it to tirelessly climb slopes and walls.",
         birthday=datetime(year=1999,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat= 87.9890,
         long=41.8898,
         picture="caterpie.jpg")

butterfree = User(name="Butterfree", 
         email="Butterfree@gmail.com", 
         password = generate_password_hash("password"),
         bio="Water-repellent powder on its wings enables it to collect honey, even in the heaviest of rains",
         birthday=datetime(year=1995,month=10,day=18),
         distance=10,
         gender="male",
         preference="both",
         min=40,
         max=100,
         lat= 87.9890,
         long=41.8898,
         picture="butterfree.jpg")

kakuna = User(name="Kakuna", 
         email="Kakuna@gmail.com", 
         password = generate_password_hash("password"),
         bio="Able to move only slightly. When endangered, it may stick out its stinger and poison its enemy",
         birthday=datetime(year=1991,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.9536,
         long=41.8398,
         picture="kakuna.jpg")

pidgeotto = User(name="Pidgeotto", 
         email="Pidgeotto@gmail.com", 
         password = generate_password_hash("password"),
         bio="It has outstanding vision. However high it flies, it is able to distinguish the movements of its prey",
         birthday=datetime(year=1998,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.9536,
         long=41.8398,
         picture="pidgeotto.jpg")

rattata = User(name="Rattata", 
         email="Rattata@gmail.com", 
         password = generate_password_hash("password"),
         bio="It eats anything. Wherever food is available, it will settle down and produce offspring continuously",
         birthday=datetime(year=1999,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.9536,
         long=41.8398,
         picture="rattata.jpg")

#10
spearow = User(name="Spearow", 
         email="Spearow@gmail.com", 
         password = generate_password_hash("password"),
         bio="t flaps its small wings busily to fly. Using its beak, it searches in grass for prey",
         birthday=datetime(year=1996,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.9536,
         long=41.8398,
         picture="spearow.jpg")

ekans = User(name="Ekans", 
         email="Ekans@gmail.com", 
         password = generate_password_hash("password"),
         bio="A very common sight in grassland, etc. It flicks its tongue in and out to sense danger in its surroundings",
         birthday=datetime(year=1999,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.9536,
         long=41.8398,
         picture="ekans.jpg")

sandshrew = User(name="Sandshrew", 
         email= "Sandshrew@gmail.com", 
         password = generate_password_hash("password"),
         bio="Its body is dry. When it gets cold at night, its hide is said to become coated with a fine dew",
         birthday=datetime(year=1999,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="sandshrew.jpg")

mewtwo = User(name="Mewtwo", 
         email="Mewtwo@gmail.com", 
         password = generate_password_hash("password"),
         bio="Because its battle abilities were raised to the ultimate level, it thinks only of defeating its foes",
         birthday=datetime(year=1999,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="mewtwo.jpg")

machoke = User(name="Machoke", 
         email="Machoke@gmail.com", 
         password = generate_password_hash("password"),
         bio="It happily carries heavy cargo to toughen up. It willingly does hard work for people",
         birthday=datetime.now(),
         distance=10,
         gender="male",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="machoke.jpg")

poliwhirl = User(name="Poliwhirl", 
         email="Poliwhirl@gmail.com", 
         password = generate_password_hash("password"),
         bio="The skin on most of its body is moist. However, the skin on its belly spiral feels smooth",
         birthday=datetime(year=1969,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="poliwhirl.jpg")

psyduck = User(name="Psyduck", 
         email="Psyduck@gmail.com", 
         password = generate_password_hash("password"),
         bio="If its chronic headache peaks, it may exhibit odd powers. It seems unable to recall such an episode",
         birthday=datetime(year=1969,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="psyduck.jpg")

oddish = User(name="Oddish", 
         email="Oddish@gmail.com", 
         password = generate_password_hash("password"),
         bio="If exposed to moonlight, it starts to move. It roams far and wide at night to scatter its seeds",
         birthday=datetime(year=1996,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="oddish.jpg")

wigglytuff = User(name="Wigglytuff", 
         email="Wigglytuff@gmail.com", 
         password = generate_password_hash("password"),
         bio="The rich, fluffy fur that covers its body feels so good that anyone who feels it can’t stop touching it",
         birthday=datetime(year=1995,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="wigglytuff.jpg")

ninetales = User(name="Ninetales", 
         email="Ninetales@gmail.com", 
         password = generate_password_hash("password"),
         bio="Some legends claim that each of its nine tails has its own unique type of special mystical power",
         birthday=datetime(year=1995,month=10,day=18),
         distance=10,
         gender="female",
         preference="male",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="ninetales.jpg")

clefable = User(name="Clefable", 
         email="Clefable@gmail.com", 
         password = generate_password_hash("password"),
         bio="Its very sensitive ears let it distinguish distant sounds. As a result, it prefers quiet places.",
         birthday=datetime(year=1997,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="clefable.jpg")
#19
nidoqueen = User(name="Nidoqueen", 
         email="Nidoqueen@gmail.com", 
         password = generate_password_hash("password"),
         bio="Its body is covered with needle-like scales. It never shows signs of shrinking from any attack",
         birthday=datetime(year=1969,month=10,day=18),
         distance=10,
         gender="male",
         preference="female",
         min=40,
         max=100,
         lat=87.8517,
         long=41.8239,
         picture="nidoqueen.jpg")

db.session.add(moltres)
db.session.add(bulbasaur)
db.session.add(pikachu)
db.session.add(charmeleon)
db.session.add(blastoise)
db.session.add(caterpie)
db.session.add(butterfree)
db.session.add(kakuna)
db.session.add(pidgeotto)
db.session.add(rattata)
db.session.add(spearow)
db.session.add(ekans)
db.session.add(sandshrew)
db.session.add(mewtwo)
db.session.add(machoke)
db.session.add(poliwhirl)
db.session.add(psyduck)
db.session.add(oddish)
db.session.add(wigglytuff)
db.session.add(clefable)
db.session.add(nidoqueen)
db.session.add(ninetales)
db.session.commit()

print(pikachu.id)
print(moltres.id)

db.session.add(Swipe(matcher_id=pikachu.id, matched_id=moltres.id, match = True))
db.session.add(Swipe(matcher_id=pikachu.id, matched_id=charmeleon.id, match = True))
db.session.add(Swipe(matcher_id=pikachu.id, matched_id=blastoise.id, match = True))
db.session.add(Swipe(matcher_id=pikachu.id, matched_id=caterpie.id, match = True))
db.session.add(Swipe(matcher_id=pikachu.id, matched_id=kakuna.id, match = True))
db.session.add(Swipe(matcher_id=nidoqueen.id, matched_id=pikachu.id, match = True))

#m = Match(matcher_id=adam.id, matched_id=mary.id)
#db.session.add(m)
db.session.add(Match(matcher_id=pikachu.id, matched_id=moltres.id))
db.session.add(Match(matcher_id=pikachu.id, matched_id=charmeleon.id))
db.session.add(Match(matcher_id=pikachu.id, matched_id=blastoise.id))
db.session.add(Match(matcher_id=pikachu.id, matched_id=caterpie.id))
db.session.add(Match(matcher_id=pikachu.id, matched_id=kakuna.id))
db.session.add(Match(matcher_id=nidoqueen.id, matched_id=pikachu.id))
db.session.commit()

db.session.add(Swipe(matched_id=pikachu.id, matcher_id=clefable.id, match = True))
db.session.add(Swipe(matched_id=pikachu.id, matcher_id=wigglytuff.id, match = True))
db.session.add(Swipe(matched_id=pikachu.id, matcher_id=bulbasaur.id, match = True))
db.session.add(Swipe(matched_id=pikachu.id, matcher_id=spearow.id, match = True))
db.session.add(Swipe(matched_id=pikachu.id, matcher_id=ekans.id, match = True))
db.session.add(Swipe(matched_id=pikachu.id, matcher_id=poliwhirl.id, match = True))
db.session.commit()



db.session.add(Message(sender=moltres.id, receiver=pikachu.id, contents="......"))
db.session.add(Message(sender=pikachu.id, receiver=moltres.id, contents="pika pika pika pika "))
db.session.add(Message(sender=charmeleon.id, receiver=pikachu.id, contents="char char"))
db.session.add(Message(sender=pikachu.id, receiver=charmeleon.id, contents="pika pika pika pika"))
db.session.add(Message(sender=pikachu.id, receiver=blastoise.id, contents="pika pika pika pika"))
db.session.add(Message(sender=blastoise.id, receiver=pikachu.id, contents="squirttt"))
db.session.add(Message(sender=pikachu.id, receiver=caterpie.id, contents="pika pika pika pika"))
db.session.add(Message(sender=caterpie.id, receiver=pikachu.id, contents="caterpie...."))
db.session.add(Message(sender=pikachu.id, receiver=caterpie.id, contents="pika pika pika pika"))
db.session.add(Message(sender=caterpie.id, receiver=pikachu.id, contents="caterpie....."))
db.session.add(Message(sender=kakuna.id, receiver=pikachu.id, contents="......."))
db.session.add(Message(sender=caterpie.id, receiver=pikachu.id, contents="caterpie...."))
db.session.commit()

from .views import *
