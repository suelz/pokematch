import random
import secrets
import string

alphabet = string.ascii_letters + string.digits
count = 0

locations = [
{'long':41.8995, 'lat':87.9403},
{'long':41.8898, 'lat':87.9890},
{'long':41.8398, 'lat':87.9536},
{'long':41.8239, 'lat':87.8517}
]


bios = ["Living vicariously through myself", "I can quote Top Gun better than you and all your friends.", "an’t remember who I stole my bio from or why.",
        "The only thing stopping me is my lack of motivation.", "Here to serve….cats", "I used to act. I also belly dance and eat Jolly Ranchers – not always at the same time though.",
        "I’m me you knucklehead","its 11:11 make a wish", "cool story bro", "cool story bro", "leave me alone", "When the above code is executed, it produces the following result",
        "ADD ELPAISACOMPA", "elpaisacompa", "EL PAISA COMPA SNAPCHAT ADD IT", "OMAR WAS HERE" ]

pokemon = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard",
           "Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle",
           "Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow",
           "Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran","Nidorina",
           "Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales",
           "Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect",
           "Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey",
           "Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra",
           "Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool",
           "Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite",
           "Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster",
           "Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode",
           "Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing",
           "Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu",
           "Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados",
           "Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops",
           "Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]

def generateName():
    x = random.randint(1, len(pokemon)-1)
    y = pokemon[x]
    del pokemon[x]
    return y

def generateEmail():
    return str(count) + "@gmail.com"

def generatePassword():
    return ''.join(secrets.choice(alphabet) for i in range(20)) 

def generateBio():
    x = random.randint(1, len(bios)-1)
    y = bios[x]
    del bios[x]
    return y

def generateYoungBirths():
    month = random.randint(1,12)
    day = random.randint(1,30)
    year = random.randint(1993,2000)
    return str(month) + "/" + str(day) + "/" + str(year)

def generateOldBirths():
    month = random.randint(1,12)
    day = random.randint(1,30)
    year = random.randint(1950,2000)
    return str(month) + "/" + str(day) + "/" + str(year)

def generateDistance():
    return random.randint(1,25)

def generateGender():
    x = random.randint(0,1)
    if x == 1:
       return "male"
    else:
       return "female"

def generatePreference():
    x = random.randint(0,2)
    if x == 1:
       return "male"
    if x == 0:
       return "female"
    else:
       return "both"

def generateLocataion():
    x = random.randint(1,len(locations)-1)
    return locations[x]
    

for i in range(15):
    count +=1
    print(generateName())
    print(generateEmail())
    print(generatePassword())
    print(generateBio())
    print(generateYoungBirths())
    print(generateDistance())
    print(generateGender())
    print(generatePreference())
    print(generateLocataion())
    print(" ")
