import guess_the_number as gtn

number_game = gtn.NumberGamePlaylist()


def play_game():
    play_computer = "Play the computer"
    computer_play = "Computer plays you"
    failed_to_understand = "Sorry, that game is not listed above."
    pick_game = input(f"Type in what you'd like to play: "f"{play_computer} or {computer_play}?> ")

    if pick_game == computer_play:
        return number_game.number_guess()
    elif pick_game == play_computer:
        return number_game.computer_guess()
    else:
        if pick_game != computer_play or play_computer:
            print(failed_to_understand)


play_game()
