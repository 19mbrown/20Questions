#!/usr/bin/python3
import random

#####################
## NOT WORKING YET ##
#####################

global genders, charClasses, strength, powers

genders = ["Female", "Male"]
charClasses = ["Normal", " Fire", " Water", " Grass", " Electric", " Ice", " Fighting", " Poison", " Ground", " Flying", " Psychic", " Bug", " Rock", "Ghost", "Dragon"]
powers = ["Invisibility", "Shapshitfting", "Magnetism", "Night Vision", "Danger Sense"]

class character:
    gender = random.choice(genders)
    charClass = random.choice(charClasses)
    power = random.choice(powers)
    strength = random.randrange(1,100)

print(f"STRENGTH: {character.strength}\nGender: {character.gender}\nPowers: {character.power}\nClass: {character.charClass}")
