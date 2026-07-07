from typing import List

def get_word_length(words):
    return len(words)

def absoule_value(number):
    return abs(number)

def sort_words(words: List[str]) -> List[str]:
    return words.sort(key=get_word_length)


def sort_numbers(numbers: List[int]) -> List[int]:
    return numbers.sort(key=absoule_value)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
