def add_prefix_un(word):
   
    return ("un" + word)
    """
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    """


def make_word_groups(vocab_words):
    prefix = ' :: ' + vocab_words[0] # "::" plus the first item in the list, which is the prefix
    result_data = prefix.join(vocab_words) # join the words in a list separated by :: whilst adding the prefix to the words
    return result_data
    pass
# ".join" is function which uses a joining word or character between the words of a list. e.g. myTuple = ("John", "Peter", "Vicky")

# x = "#".join(myTuple)

# print(x) (which gives "John#Peter#Vicky")

    """

    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    """

def remove_suffix_ness(word):
    no_ness = word[:-4] #the ":" cuts the word to use everything before that place
    if no_ness[-1] == "i": # the lack of a ":" looks for the character at that point in the string
        return (no_ness[:-1] + "y") # remove the "i" and add a "y"
    else:
        return no_ness # return the word without the "ness"

#analyse word
#if [-4] = "i",then need to add a "y"

    """
    This function takes in a word and returns the base word with `ness` removed.
    """

def noun_to_verb(sentence, index):
    #split sentence into list of words using " " as the separator
    #add an "en" to the word at that index
    #return word

    sentence_list = sentence[:-1].split(" ") # split sentence. ":-1" to exclude punctuation at the end
    verb = sentence_list[index] # assign word at index location
    return verb + "en" # add "en" to word at index location
    
    """

    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    """
