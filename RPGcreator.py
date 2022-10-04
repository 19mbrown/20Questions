#!/usr/bin/python3
import random

global genders, charClasses, strength, powers

genders = ["Female", "Male"]
powers = ["Fire", "Water", "Electric", "Ice", "Fighting", "Poison", "Flying", "Psychic", "Ghost", "Dragon", "Invisibility", "Shapshitfting", "Magnetism", "Night Vision", "Danger Sense"]
charClasses = ["The Fighter", "The Rogue", "The Magician", "The Rangers", "The Clerics", "Rare Character"]

class character:
    gender = random.choice(genders)
    power = random.choice(powers)
    charClass = random.choice(charClasses)
    strength = random.randrange(1,100)

print(f"Strength: {character.strength}\nGender: {character.gender}\nPowers: {character.power}\nClass: {character.charClass}")
