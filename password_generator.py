import string
import random

# define colours to be used in the program


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# create lists used to populate the password
alphabet_lowercase_list = list(string.ascii_lowercase)
alphabet_uppercase_list = list(string.ascii_uppercase)
special_characters_list = list(string.punctuation)
number_list = list(range(0, 10))
user_selected_lists = []
passwords = []

# Ask questions to the user
print(f'{bcolors.OKBLUE}{bcolors.BOLD}{bcolors.UNDERLINE}\nLET\'S GENERATE SOME PASSWORDS\n')
print(f'{bcolors.ENDC}I\'m going to ask a few questions to customize the password to your needs\n')


def number_of_characters_to_use():
    number_of_characters = input(
        f'{bcolors.OKGREEN}how many characters do want your password to have ')
    if number_of_characters.isdigit():
        return number_of_characters
    else:
        print(f'{bcolors.FAIL}Please make sure to enter a number')
        number_of_characters_to_use()


def use_lowercase_characters():
    use_lowercase = input(
        f'{bcolors.OKGREEN}Do you want to include lowercase characters (Y/N) ')
    if use_lowercase == 'Y':
        user_selected_lists.append(alphabet_lowercase_list)
        return True
    elif use_lowercase == 'N':
        return False
    else:
        print(f'{bcolors.FAIL}Please enter only Y or N')
        return use_lowercase_characters()


def use_uppercase_characters():
    use_uppercase = input(
        f'{bcolors.OKGREEN}Do you want to include uppercase characters (Y/N) ')
    if use_uppercase == 'Y':
        user_selected_lists.append(alphabet_uppercase_list)
        return True
    elif use_uppercase == 'N':
        return False
    else:
        print(f'{bcolors.FAIL}Please enter only Y or N')
        use_uppercase_characters()


def use_special_characters():
    use_special = input(
        f'{bcolors.OKGREEN}Do you want to include special characters(Y/N) ')
    if use_special == 'Y':
        user_selected_lists.append(special_characters_list)
        return True
    elif use_special == 'N':
        return False
    else:
        print(f'{bcolors.FAIL}Please enter only Y or N')
        use_special_characters()


def use_numbers_in_password():
    use_numbers = input(
        f'{bcolors.OKGREEN}Do you want to include numbers (Y/N) ')
    if use_numbers == 'Y':
        user_selected_lists.append(number_list)
        return True
    elif use_numbers == 'N':
        return False
    else:
        print(f'{bcolors.FAIL}Please enter only Y or N')
        use_numbers_in_password()


def number_of_passwords_to_create():
    number_of_passwords = input(
        f'{bcolors.OKGREEN}How many passwords do you want ')
    if number_of_passwords.isdigit():
        print(number_of_passwords)
        return number_of_passwords
    else:
        print(f'{bcolors.FAIL}Please make sure to enter a number')
        return number_of_passwords_to_create()


number_of_characters = number_of_characters_to_use()
use_lowercase = use_lowercase_characters()
use_uppercase = use_uppercase_characters()
use_special = use_special_characters()
use_numbers = use_numbers_in_password()
number_of_passwords = number_of_passwords_to_create()


def create_password():
  # TODO fix that 5.  to be replaced by the actual quantity needed
    for i in range(5):
        passwords = []
        number_of_chosen_lists = len(user_selected_lists)
        number_characters_per_list = float(
            number_of_characters) / number_of_chosen_lists

        for i in user_selected_lists:
            for item in range(int(number_characters_per_list)):
                selected_character = random.choice(i)
                passwords.append(selected_character)
        diff = float(number_of_characters) - float(len(passwords))
        if diff != 0:
            for i in range(int(diff)):
              # TODO This is a big mess.  I need to find a cleaner way
                # If the password does not have the required number of charaters, is
                # because the number of characteres wanted in the password does not return
                # an integer.
                # I'm checking if the result is shorter than requiered, and if this is the case
                # I itereate the required number of times and select needed characters
                passwords.append(random.choice(
                    random.choice(user_selected_lists)))
        ps = ''
        for i in passwords:
            ps += str(i)
        print(' ', ps)


print(f'''{bcolors.OKBLUE}  \n You selected: 
    number of characters: {number_of_characters}
    use_lowercase: {use_lowercase}
    use_uppercase: {use_uppercase}
    use_special: {use_special}
    use_numbers: {use_numbers}
    number_of_passwords: {number_of_passwords}
    \n 
    \n 
    Here is/are your password/s:
    {create_password()}
    ''')
