def get_book_text(filepath): 

    # read a text file
    with open(filepath) as f:
        content = f.read()
        return content


def count_words(text):

    # split the text into words
    words_list = text.split()

    # get the length
    count = len(words_list)

    return count


def count_characters(text):
    # make it lower case
    text_all_low = text.lower()

    # empty dict
    chars = {}

    # logic for counting
    for c in text_all_low:
        if c not in chars.keys():
            chars[c] = 1
        else:
            chars[c]+= 1

    return chars

def sort_list_of_dicts(dictionary):
    # Empty dict
    res = []

    # creating list of dicts
    for char in dictionary:
        res.append({
            "char": char,
            "num": dictionary[char]
        })

    # sorting using helper function
    res.sort(key=sort_on, reverse=True)

    return res

# Helper function for sorting
def sort_on(item):
    return item["num"]
