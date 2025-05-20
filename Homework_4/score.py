# YOUR TASK'S: IMPLEMENT THE FOLLOWING FUNCTIONS

def remove_non_alpha(string: str) -> str:
    """ (1 point)
    this function will remove all non-alphabetic
    character from a string and returns the 'cleaned'
    string.
    e.g.: 'a1bc4d' -> 'abcd'
          'A$tra.' -> 'Atra'
          '3.12'   -> ''

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use list comprehension or ternary operator!
    """
    only_letters = ""
    for char in string:    
        if char.isalpha(): # remove all numbers and symbols, keep only letters
            only_letters = only_letters + char
    return only_letters


def extract_words(lyrics: str) -> list[str]:
    """ (1 points)
    in this function, a string will be transformed
    into a list, where each 'word' of the string is
    part of. the definition of a 'word' will be:
    - only alphabetic characters (a-z, A-Z, äöüß)
      - HINT: the remove_non_alpha function may help
    - a whitespace character (space, newline, ...)
      separates words from each other
    - an empty string is not a valid word
    - the strings returned are all in lowercase
    e.g.: 'Hello, W0rld!' -> ['hello', 'wrld']
          '12.3 * 3' -> []
          '' -> []

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use list comprehension or ternary operator!
    """
    list_of_words = []
    for word in lyrics.split(): # split lyrics list to get all the words
        # pass word to remove_non_alpha to get word with only letters, in lowercase
        only_letters = remove_non_alpha(word).lower()
        if only_letters: # only add word to list if it is not empty
            list_of_words.append(only_letters) # add word with only letters to list of words

    return list_of_words


def uniq(strings: list[str]) -> list[str]:
    """ (1 point)
    this function will return a list with
    all UNIQ strings of the incoming list.
    The original list will not be modified!
    e.g.: ['a', 'b', 'a', 'c'] -> ['a', 'b', 'c']

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use list comprehension or ternary operator!
    """
    unique_strings = []
    for word in strings: # check every word in strings
        # if that word is currently not in unique_strings, add it
        # should work that every string only gets added once, no repeats
        if word not in unique_strings:
            unique_strings.append(word)
    return unique_strings


def lengths(strings: list[str]) -> list[int]:
    """ (1 point)
    this function will return a list of the lengths
    of the given list of strings. The incoming list
    will NOT be modified!
    e.g.: ['a', 'bc', 'def'] -> [1, 2, 3]
          ['', 'hello', 'world'] -> [5, 5] : empty strings will NOT be counted!
          [] -> []

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use list comprehension or ternary operator!
    """
    length_of_string = []
    for word in strings: # check every word in strings
        if word: # if strings is not empty
            length = len(word) # get char count of a word
            # word length should only be added if it isn't 0
            # if e.g. string is empty and length is 0, it should not be added
            if length:
                length_of_string.append(length)
    return length_of_string


def min(numbers: list[int]) -> int:
    """ (1 point)
    this function will return the smallest POSITIVE number
    of a list of numbers. when the list is empty of only
    contains negative numbers, it returns 0
    e.g.: [3, 1, 2] -> 1
          [-1, 1] -> 1
          [] -> 0

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    smallest_number = 99999999
    if not numbers: #  if list is empty, smallest number is 0
         smallest_number = 0
         return smallest_number
    for number in numbers:
            # finding a number smaller than 99999999 and replacing value of 
            # smallest_number with that
            if number > 0: # first check for smallest positive number
                if number < smallest_number:
                    smallest_number = number
    if smallest_number == 99999999: # means that number wasn't updated bc all numbers in list were negative
        smallest_number = 0      
    return smallest_number


def max(numbers: list[int]) -> int:
    """ (1 point)
    this function will return the largest POSITIVE number
    of a list of numbers. when the list is empty of only
    contains negative numbers, it returns 0
    e.g.: [3, 1, 2] -> 3
          [-1, 1] -> 1
          [] -> 0

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    biggest_number = 0
    if not numbers: #  if list is empty, biggest number is 0
        biggest_number = 0
        return biggest_number
    for number in numbers:
        # finding a number bigger than 0 and replacing value of 
        # biggest_number with that
        if number > biggest_number:
            biggest_number = number
        # shouldn't need anything else
        # since biggest_number starts at 0, if there are negative numbers
        # biggest_number stays at 0
    return biggest_number


def counts(numbers: list[int]) -> list[int]:
    """ (1 point)
    this function returns a NEW list with the
    counts of every number between the SMALLEST
    and LARGEST number of the given list. The
    incoming list will NOT be modified!
    e.g.: [1, 2, 4, 1, 4] -> [2, 1, 0, 2]
          [2, 2, 2] -> [3]
          [3, 5, 3, 5, 5] -> [2, 0, 3]

    You're allowed to use every string-method,
    loops, lists (and list-methods, except of 'sort')
    and conditions, as well as arithmetic/boolean operators.
    Do NOT use the 'list.sort'-method or 'sorted', 'map' or
    any other function from 'collections' or other modules!
    Do NOT use the 'set'-function!
    Do NOT use the build-in 'min' or 'max' functions!
    Do NOT use list comprehension or ternary conditions!
    """
    counting_numbers = [] # where we save each numbers count
    # find smallest and largest numbers in the given list
    smallest_number = min(numbers)
    biggest_number = max(numbers)

    if not numbers: # if numbers is an empty list, return an empty list
        return counting_numbers
    
    # for any given number in the range between smallest number to biggest number
    # (even for numbers that aren't on the list but are on the range)
    # (+1 otherwise biggest number wont be part of the loop)
    for any_given_number in range(smallest_number, biggest_number +1):
        count = 0 # start a counter
        for actual_number in numbers: # for every number in the list
            # if it matches the current any_given_number, add to the counter
            # numbers in the range that don't match an actual_number on the 
            # list will have a count of 0
            if actual_number == any_given_number:
                count +=1
        # add that counter to our list of numbers count        
        counting_numbers.append(count)

    return counting_numbers


def score(lyrics: str) -> float:
    """ (3 points)
    calculate the score of lyrics

    this fictional score will be calculated
    through the following aspects:

    - The sum of the length of all words  (SAW)
    - The sum of the length of all uniq words  (SUW)
    - The sum of the count of the length of all words  (SCAW)
    - The sum of the count of the length of all uniq words (SCUW)

    The formula for the score is:
    (SCAW - SCUW) / (SAW - SUW + 1)

    Use the functions that are available in this file
    to get the values you need to calculate the score.
    Try to not repeat/copy code from other functions,
    in the best case, all you need are the available
    functions and some variables, as well as a simple
    arithmetic calculation at the end.
    To build a sum of a list of numbers, feel free to
    use the 'sum'-function from python, or create your
    own function to do that.

    Do NOT use list comprehension or ternary conditions,
    or any functions that you have to be imported
    """
    final_score = 0.0
    saw = 0  # sum of the length of all words
    suw = 0  # sum of the length of all uniq words
    scaw = 0 # sum of the count of the length of all words
    scuw = 0 # sum of the count of the length of all uniq words

    # first get all the words from the lyrics
    list_of_words = extract_words(lyrics)

    # then get lengths of all the words
    length_of_words = lengths(list_of_words)

    # sum up the length of all the words to get saw
    for length in length_of_words:
        saw += length
    
    # then get unique words
    list_of_unique_words = uniq(list_of_words)

    # get lengths for all unique words
    length_of_unique_words = lengths(list_of_unique_words)

    # sum up the length of all unique words to get suw
    for length in length_of_unique_words:
        suw += length
    
    # count the length of all words
    count_all_words = counts(length_of_words)

    # sum up count of length of all words to get scaw
    for count in count_all_words:
        scaw += count
    
    # count the length of all unique words
    count_unique_words = counts(length_of_unique_words)

    # sum up count of length of all unique words to get scuw
    for count in count_unique_words:
        scuw += count

    final_score = (scaw - scuw) / (saw - suw + 1)
    return final_score

# END OF YOUR TASK'S
