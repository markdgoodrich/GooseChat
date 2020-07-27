import random


def creation():
    stats = ["1","2","3"]

    sexy = ["Sculpted muscles",
            "Majestic hair/beard/moustache",
            "Impeccable, pristine style",
            "Amazing bone structure",
            "Ethereal, graceful, and elegant",
            "Dangerous rebel with a cool jacket"]

    weapon_1 = ["Void", "Sepluchral", "Umbral", "Celestial", "Ghost-wolf",
                          "Fae", "Ember", "Crystal", "Rift", "Doom"]
    weapon_2 = ["Hammer", "Blades", "Whip", "Jezail", "Bow", "Cannon",
                          "Glaive", "Chain", "Fist", "Shield"]

    magic_school = ["Lore of Light", "Path of Beasts", "Secrets of Occult Shadowmancy",
                    "Arcana of Supreme Doorway", "Art of Hyperdimensional Splendour",
                    "Way of Ten Thousand Mirrors"]

    random.shuffle(stats)

    a = "Sexy Score: %s \nYour Sexy Trait is %s\nBattle Score: %s \nYour weapon is the fabled %s %s\nMagic Score: %s \nYou are a magician who studied the %s\n" %(stats[0], random.choice(sexy), stats[1], random.choice(weapon_1), random.choice(weapon_2), stats[2], random.choice(magic_school))
    #b = "Battle Score: %s \nYour weapon is the fabled %s %s\n" %(stats[1], random.choice(weapon_1), random.choice(weapon_2))
    #c = "Magic Score: %s \nYou are a magician who studied the %s\n" %(stats[2], random.choice(magic_school))

    return(a)

