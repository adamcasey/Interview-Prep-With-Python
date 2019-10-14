#!/usr/local/bin/python3

# This was was my technical interview question with Pie Insurance in October, 2019

"""
    ** Prompt **
    Given a long string of text, count occurrence of unique words in it.
    When the count is complete, print them in a sorted by the frequency (most frequent first).
    The count should be case insensitive, and ignore extra whitespace and all punctuation.
    Hyphenated words (e.g. "brother-in-law") should count as a single word.
    The input string is declared in the class.
    There is a test method defined in the class. This method should print "Success!" when your input is sorted correctly.
    Proper error checking/exception handling is not required.

    For Example:
    excerpt = "Well The. quick, brown?    fox!! jumped over         the lazy dog The lazy brown dog jumped over the quick fox. ";
    
    Expected Test Output:
    the 4
    quick 2
    brown 2
    fox 2
    jumped 2
    over 2
    lazy 2
    dog 2
    well 1
    Success!
"""

#_EXCERPT = "Well The. quick, brown?    fox!! jumped over         the lazy dog The lazy brown dog jumped over the quick fox. "

_EXCERPT = """
A SQUAT grey building of only thirty-four stories. Over the main entrance the
 words, CENTRAL LONDON HATCHERY AND CONDITIONING CENTRE, and, in a shield, the
 World State's motto, COMMUNITY, IDENTITY, STABILITY. The enormous room on the
 ground floor faced towards the north. Cold for all the summer beyond the
 panes, for all the tropical heat of the room itself, a harsh thin light
 glared through the windows, hungrily seeking some draped lay figure, some
 pallid shape of academic goose-flesh, but finding only the glass and nickel
 and bleakly shining porcelain of a laboratory. Wintriness responded to
 wintriness. The overalls of the workers were white, their hands gloved with a
 pale corpse-coloured rubber. The light was frozen, dead, a ghost. Only from
 the yellow barrels of the microscopes did it borrow a certain rich and living
 substance, lying along the polished tubes like butter, streak after luscious
 streak in long recession down the work tables. """

import string, re, collections

# def cleanString(string_val):
#     return "".join(" " if i string.punctuation)

def _count_and_print_words(excerpt):

    punctuation = "!@#$%^&*()_+<>?:.,;"
    word_counts_by_word = {}
    count = 0
    #exclude = set(string.punctuation)
    #table = str.maketrans("","")
    #table = str.maketrans(dict.fromkeys(string.punctuation))
    remove_punct_map = dict.fromkeys(map(ord, string.punctuation))
    # grab each word from the string
    for each_word in excerpt.split(" "):
        # remove whitespaces and put into lowercase
        # add to dictionary
        if each_word != "":
            #each_word.translate(table, string.punctuation)
            #each_word = each_word.lower()
            #each_word.translate(remove_punct_map)
            #each_word.translate(str.maketrans({a:None for a in string.punctuation}))
            # check if hyphenated word
            if '-' in each_word:
                continue

            else:
                each_word = re.sub(r'[^\w\s]', '', each_word).lower()
            # word isn't in dict yet so add it
            if each_word not in word_counts_by_word:
                word_counts_by_word[each_word.strip()] = 1
            # if word is already in dict
            elif each_word in word_counts_by_word:
                # update the count of that word
                temp_value = word_counts_by_word.get(each_word)
                temp_value += 1
                word_counts_by_word[each_word.strip()] = temp_value
            
    # sort dictionary by value 
    sorted_dict = sorted(word_counts_by_word.items(), key=lambda x:x[1])
    new_dict = collections.OrderedDict()

    #print("sorted_dict: {}".format(sorted_dict))
    
    for item in reversed(sorted_dict):
        new_dict[item[0]] = item[1]
        #print(item)
        
    #print(len(new_dict))
    print("new_dict: {}".format(new_dict))
    return new_dict


def main():
    word_counts_by_word = _count_and_print_words(_EXCERPT)
    _test_that_solution_is_sorted_descending(word_counts_by_word)


def _test_that_solution_is_sorted_descending(word_counts_by_word):
    previous_count = len(word_counts_by_word) + 1
    print("word_counts_by_word: {}".format(word_counts_by_word))
    if len(word_counts_by_word) == 0:
        print("Failure: List Empty!")
        return
    for word, word_count in word_counts_by_word.items():
        print("word: {}, word_count: {}".format(word, word_count))
        print("previous_count: {}".format(previous_count))
        if word is None or word == "":
            print("Failure: Not a word: null or empty!");
            return
        if word == "thirtyfour":
            print("Failure: Not a word: \"thirtyfour\"!");
            return
        if "." in word or "," in word or "\"" in word:
            print("Failure: Word contains punctuation: \"{}\"!".format(word));
            return
        # This was '>=' but not even the example test string would pass...
        if word_count > previous_count:
            print("Failure: Not sorted correctly!")
            return
        previous_count = word_count
    print("Success!")


main()
