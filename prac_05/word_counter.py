text_input = input("Text: ")
word_count_dict = {}
word_list = text_input.split(" ")
for word in word_list:
    if word.lower() in word_count_dict:
        word_count_dict[word.lower()] += 1
    else:
        word_count_dict[word.lower()] = 1
longest_word = 0
for word in word_count_dict:
    if len(word) > longest_word:
        longest_word = len(word)
for word, frequency in sorted(word_count_dict.items()):
    print("{:{}} {}".format(word, longest_word, frequency))
