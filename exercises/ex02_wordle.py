"""This program is designed to mimic the popular game 'Wordle' with a set secret word."""

"""Note that some lines get too long and so will split, which may impact viewing experience."""

__author__: str = "730745029"


def contains_char(word: str, character: str) -> bool:
    """Checks if the input letter is within the input word."""
    assert len(character) == 1, f"len('{character}') is not 1"
    gate: int = len(word)
    idx: int = 0

    while gate > 0:  # Using gate allows the function to cycle through each character.

        if word[idx] == character:
            return True

        else:
            idx = idx + 1
            gate = gate - 1

    return False


def emojified(guess: str, answer: str) -> str:
    """Creates a string of boxes of the correct positions of the letters."""
    assert len(guess) == len(answer), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    emoji_string: str = ""
    gate: int = len(answer)
    idx: int = 0
    while gate > 0:  # Adds a box depending on the answer and the input.

        if guess[idx] == answer[idx]:
            emoji_string += GREEN_BOX

        elif contains_char(word=answer, character=guess[idx]):
            emoji_string += YELLOW_BOX

        else:
            emoji_string += WHITE_BOX

        idx += 1
        gate -= 1
    return emoji_string


def input_guess(expected_length: int) -> str:
    """Makes sure that the guess and the answer are the same length."""
    while True:  # Gate is not present here :(

        guess_input: str = input(f"Enter a {expected_length} character word")

        if len(guess_input) != expected_length:  # Checks to see if length is not equal.
            print(f"That wasn't {expected_length} chars! Try Again:")

        elif expected_length == len(guess_input):
            return guess_input


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1

    while turn <= 6:  # Turns will tick down until ran out.

        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))  # Takes user input for emojified.
        print(emojified(guess, secret))

        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        turn = turn + 1


print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
