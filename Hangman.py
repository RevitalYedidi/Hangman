HANGMAN_ASCII_ART = """ _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 7

# draw hangman by the wrong tries numbers
HANGMAN_PHOTOS = {
    0:
        """x-------x""",
    1:
"""x-------x
|
|
|
|
|""",
    2:
"""x-------x
|       |
|       0
|
|
|""",
    3:
"""x-------x
|       |
|       0
|       |
|
|""",
    4:
 """x-------x
|       |
|       0
|      /|\\
|
|""",
    5:
"""x-------x
|       |
|       0
|      /|\\
|      /
|""",
    6:
"""x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}


# for change the hangman's colors
COLORS_LIST = ['\33[37m', '\33[31m', '\33[33m', '\33[34m', '\33[32m', '\33[35m', '\33[36m']


def opening_screen():
    """
    print HANGMAN ASCII image and nums of max tries
    :return: None
    """
    print '\33[33m',
    print HANGMAN_ASCII_ART, "\n"
    print "You have", MAX_TRIES-1, "tries maximum."
    print '\033[0m'


def choose_word(file_path, index):
    """
    :param file_path: string
    :param index: int
    :return: the secret word the user chose at index : string
    """
    with open(file_path, "r") as words_file:
        words = words_file.readline()
        words_list = words.split(" ")
        new_index = (index - 1) % len(words_list)
        secret_word = words_list[new_index]

    return (secret_word)


def print_hangman(num_of_tries):
    """
    the function draw the photo of hangman belong num of user tries
    :param num_of_tries: int
    :return: None
    """
    print HANGMAN_PHOTOS[num_of_tries]


def show_hidden_word(secret_word, old_letters_guessed):
    """
    :param secret_word: string
    :param old_letters_guessed: list
    :return: string for show to user with '_' and correct chars
    """
    hidden_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            hidden_word += letter + " "
        else:
            hidden_word += "_ "
    hidden_word.rstrip()
    return hidden_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    :param letter_guessed: string
    :param old_letters_guessed: list
    :return: true if the input is valid or was't guessed else false
    """
    if (not is_valid_input(letter_guessed)):
        return False
    if letter_guessed.lower() in old_letters_guessed:
        return False
    return True


def is_valid_input(letter_guessed):
    """
    :param letter_guessed: string
    :return: true if it's valid else false
    """
    return (len(letter_guessed) == 1 and letter_guessed.isalpha())


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    the function use check_valid_input function,
    :param letter_guessed:
    :param old_letters_guessed:
    :return: if it's not valid return false,
    else the char will added to guessed list and return true
    """
    is_added = True
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
    else:
        print "X"
        print " -> ".join(sorted(old_letters_guessed))
        is_added = False
    return is_added


def check_win(secret_word, old_letters_guessed):
    """
    :param secret_word:
    :param old_letters_guessed:
    :return: true if the user guessed all the letters, else return false
    """
    guess_str = show_hidden_word(secret_word, old_letters_guessed)
    guess_str = guess_str.replace(" ", "")
    return guess_str == secret_word


def main():
    """
    the function manage the game and call the needed function
    :return: None
    """
    opening_screen()
    file_path = input("Enter file path: ")
    index = input("Enter index: ")
    secret_word = choose_word(file_path, index)
    num_of_tries = 0
    old_letters_guessed = []
    is_won = False
    print ("Let\'s start!")
    print_hangman(num_of_tries)
    while num_of_tries < MAX_TRIES-1 and not is_won:
        hidden_word = show_hidden_word(secret_word, old_letters_guessed)
        print hidden_word
        letter_guessed = raw_input("Guess a letter: ")

        while try_update_letter_guessed(letter_guessed, old_letters_guessed) is False:
            letter_guessed = raw_input("Guess a letter: ")

        if letter_guessed not in secret_word:
            num_of_tries += 1
            # change color
            print COLORS_LIST[num_of_tries],
            print "):"
            print_hangman(num_of_tries)
            # back to white
            print COLORS_LIST[0],

        is_won = check_win(secret_word, old_letters_guessed)

    print '\33[31m',

    if is_won:
        print """
                             __    __  _____     __ 
                            / / /\ \ \ \_   \ /\ \ \\
                            \ \/  \/ /  / /\//  \/ /
                             \  /\  //\/ /_ / /\  / 
                              \/  \/ \____/ \_\ \/  """
    else:
        print """
                             __    ____  _____  ______
                            / /   / __ \/ ___/ / ____/
                           / /   / / / /\__ \ / __/   
                          / /___/ /_/ /___/ // /___   
                         /_____/\____//____//_____/"""

    # reset
    print '\033[0m',


# run the game
if __name__ == "__main__":
    main()