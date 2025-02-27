def count_word_frequency(words):
    """Count frequency of words in a list"""
    word_freq = {}
    for word in words:
        word = word.lower()  # Convert to lowercase for case-insensitive counting
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq