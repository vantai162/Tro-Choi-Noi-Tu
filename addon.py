def check_similar_words(list):
    for word in list:
        if list.count(word) > 1:
            print(word)
    return