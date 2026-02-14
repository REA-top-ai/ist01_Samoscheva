#Задание 1
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements['fire'])

#Задание 2
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements['energy'] = 'Not a Zodiac element'
if 'energy' in zodiac_elements:
    print(zodiac_elements['energy'])

#Задание 3
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
check = 'matcha'
caffeine_level['matcha'] = 30
try:
    print(caffeine_level[check])
except KeyError:
    print("Неизвестный уровень кофеина")

#Задание 4
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)
stack_id = user_ids.get('superStackSmash', 100000)
print(stack_id)

#Задание 5
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
classes = num_exercises.keys()
print(users)
print(classes)

#Задание 6
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)

#Задание 7
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor",5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10:"Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance",15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}
spread = {}
spread['прошлое'] = tarot[13]
spread['настоящее'] = tarot[22]
spread['будущее'] = tarot[10]
print(spread)

