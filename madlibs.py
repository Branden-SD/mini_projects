class Madlib:

    def cp_story_madlib(self):
        adj = input("Type an adjective: ")
        verb1 = input("Type a verb: ")
        verb2 = input("Type your second verb: ")
        famous_person = input("Name a famous person: ")

        cp_story_madlib = f"Computer programing is so {adj}! It makes me so excited all the time because I love to" \
                          f" {verb1}. Stay hydrated and {verb2} like you are the {famous_person}!"

        return cp_story_madlib

    def party_story_madlib(self):
        greet_statement = input("Type in a greeting statement: ")
        place = input("Name a place: ")
        person = input("Name a person: ")
        gift = input("Name a gift: ")
        car = input("Name a car: ")
        decision = input("Yes or No: ")

        party_story_madlib = f"{greet_statement} {person}, I hate this party lets go " \
                             f"to {place} in my brand new {car}." \
                             f" Look I got you some {gift}. Do you like it?" \
                             f" {person} replies, {decision}."

        return party_story_madlib



