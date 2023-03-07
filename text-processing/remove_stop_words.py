# this is just a example there are a lot of stop words
stop_words = [
    "I",
    "she",
    "he",
    "they",
    "them",
    "themselves",
    "is",
    "of",
    "is",
    "am",
    "should",
    "shouldn't",
    "this",
    "that",
    "has",
    "had",
    "the",
]


def remove_stop_words(sentence):
    resultant = []
    for word in sentence.split():
        if word not in stop_words:
            resultant.append(word)
    result = " ".join(resultant)
    return result


# read the sentences from the text file and remove stop words
def remove_stop_words_from_text_file(file):
    resultant = []
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            result = remove_stop_words(line)
            resultant.append(result)
    return resultant


if __name__ == "__main__":
    file = "/home/suman/Downloads/Python Fun/Python-Programs/static/readfile.txt"
    cleaned_text_file = remove_stop_words_from_text_file(file)
    print(cleaned_text_file)
