from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest

def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    for _ in range(4):
        noun = get_noun(2)
        assert noun in plural_nouns

def test_get_verb():
    past = "past"
    present = "present"
    future = "future"
    plural = 1
    single = 2
    past_list = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    present_plural_list = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    present_single_list = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    future_list = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    for _ in range(4):
        verb = get_verb(plural, present)
        assert verb in present_plural_list
        verb = get_verb(single, past)
        assert verb in past_list
        verb = get_verb(single, present)
        assert verb in present_single_list
        verb = get_verb(single, future)
        assert verb in future_list

def test_get_preposition():
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    for _ in range(4):
        prep = get_preposition()
        assert prep in preps



def test_get_prepositional_phrase():
    #Putting preposition phrases into variables
    phrase_sing = get_prepositional_phrase(1)
    phrase_plur = get_prepositional_phrase(2)
    #Splitting variables into lists
    list_sing = list_plur = phrase_sing.split()
    #Getting length of the lists
    sing_length = plu_length = len(list_sing)
    # making sure list is 3 strings long
    assert sing_length == 3
    assert plu_length == 3
    preps = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    preposition = list_sing[0]
    assert preposition in preps
    
    
    


    # Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
