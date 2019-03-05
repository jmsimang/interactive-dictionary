import json
from difflib import get_close_matches


def load_file(file_path):
    """
    Function loads a json object containing words and descriptions.
    :return: The dictionary library of words and descriptions
    """
    return json.load(open(file_path, 'r'))


def find_word(word):
    """
    Retrieves the definition of an english word.
    :param word: Word to be search for
    :return: The definition of word that is searched for or relevant error message
    """
    # Specify file path of json dictionary
    word_list = load_file('./dataset/data.json')
    # Perform search and return results
    if word in word_list:
        return word_list[word]
    elif word.title() in word_list:
        return word_list[word.title()]
    elif word.upper() in word_list:
        return word_list[word.upper()]
    elif len(get_close_matches(word, word_list.keys())) > 0:
        match = get_close_matches(word, word_list.keys(), cutoff=0.8)[0]
        yn = input("Did you mean '{}' instead? Enter Y if yes, or N if no: ".format(match))
        if yn.lower() == 'y':
            return word_list[match]
        elif yn.lower() == 'n':
            return "The word {} doesn't exist. Please double check it.".format(word)
            # return KeyError(word)
        else:
            return "We didn't understand your entry."
    else:
        return "The word {} doesn't exist. Please double check it.".format(word)


def search_word(word):
    """
    Function searches a word and prints the description of the word if found.
    :type word: Word to search for
    :return: None
    """
    q_result = find_word(word.lower())
    if type(q_result) == list:
        for item in q_result:
            print(item)
    else:
        print(q_result)


# Start program
var = input('Enter word: ')
search_word(var)
