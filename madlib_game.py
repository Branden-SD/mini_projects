import madlibs as mlib

madlib = mlib.Madlib()

party_story = "Party Story"
computer_program_story = "Computer Programing Story"

Title = f'{party_story} or {computer_program_story}'
print(Title)


def play_madlib():
    misspelled = "Sorry, that choice is invalid"
    story_to_play = input("Type what story you want to play: ")

    if story_to_play == party_story:
        print(madlib.party_story_madlib())
    elif story_to_play == computer_program_story:
        print(madlib.cp_story_madlib())
    else:
        if story_to_play != party_story or computer_program_story:
            print(misspelled)


play_madlib()
