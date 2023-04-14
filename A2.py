import matplotlib
import numpy
import sys
import re
import matplotlib.pyplot as plt


def parseFile(lines, words_to_count, file_name):

    used_words = {}
    #print(lines)
    pattern = r'[^a-zA-Z]+'
    single_word = re.split(pattern,lines)
    word_count = 0
    unique_word = 0
    #print(single_word)
    for words in single_word:
        word_count += 1
        #print(words)
        words = words.lower()
        if words in used_words.keys():
            continue
        else:
            unique_word += 1
            used_words[words] = 0
            #print(words)
            for new_word in single_word:
                new_word = new_word.lower()
                if new_word == words:
                    used_words[words] += 1
        #print(used_words)
    #print(used_words)
    countMostFreqWords(used_words, words_to_count, unique_word, word_count, file_name)


def countMostFreqWords(words_dict, words_to_count, unique_word, word_count, file_name):

    sorted_dict = {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)}
    new_dict = {}
    new_dict = {k: words_dict[k] for k in list(sorted_dict.keys())[:words_to_count]}
    print(new_dict)
    names = list(new_dict.keys())
    values = list(new_dict.values())

    print("Word histogram of file: "+file_name)
    print()
    print("Total number of words: "+str(word_count))
    print("Number of different words: "+str(unique_word))
    print("The most common "+str(words_to_count)+" words are:")
    counter = 0
    for key, value in sorted_dict.items():
        print(key+ "         "+str(value))
        counter += 1
        if counter == words_to_count:
            break

    plt.bar(names, values)
    plt.title('Bar Plot of most common words')
    plt.xlabel('values')
    plt.ylabel('names')
    plt.show()


def main(argv):
    file = 0
    file_name = ""
    words_to_count = 10
    lines = ""
    prev_word = ""
    for word in argv:
        if word == "-file":
            prev_word = word
            continue
        if prev_word == "-file":
            prev_word = ""
            file_name = word
            with open(word, 'r') as file:
                lines = file.read().replace('\n', ' ')
        if word == "-num":
            prev_word = word
            continue
        if prev_word == "-num":
            words_to_count = int(word)
    parseFile(lines, words_to_count, file_name)


if __name__ == "__main__":
    main(sys.argv[1:])

