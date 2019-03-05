import json
from difflib import get_close_matches


def load_file():
    """
    Function loads a json object containing words and descriptions.
    :return: The dictionary library of words and descriptions
    """
    init_file = './dataset/data.json'
    return json.load(open(init_file, 'r'))


def find_word(word):
    """
    Retrieves the definition of an english word.
    :param word: word to search for
    :return: the definition of word that is searched for
    """
    word_list = load_file()
    if word in word_list:
        return word_list[word]
    elif len(get_close_matches(word, word_list.keys(), cutoff=0.8)) > 0:
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


def search_word():
    """

    :return:
    """
    var = input('Enter word: ')
    q_result = find_word(var.lower())
    if type(q_result) == list:
        for item in q_result:
            print(item)
    else:
        print(q_result)


search_word()
