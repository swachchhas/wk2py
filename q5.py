
def main():
    # Test password strength checker
    print("\nTesting password strength checker:")
    print(check_password_strength("abc"))  # Weak
    print(check_password_strength("abc123"))  # Moderate
    print(check_password_strength("abc123@#$"))  # Strong

    # Test alternate word reverser
    print("\nTesting alternate word reverser:")
    print(reverse_alternate_words("Python is an amazing programming language"))

    # Test duplicate word finder
    print("\nTesting duplicate word finder:")
    words = ["apple", "banana", "apple", "orange", "banana", "banana"]
    print(find_duplicate_words(words))

    # Test book availability checker
    print("\nTesting book availability checker:")
    check_book_availability()

    # Test word frequency counter
    print("\nTesting word frequency counter:")
    word_list = ["This", "is", "good", "is"]
    print(count_word_frequency(word_list))

if __name__ == "__main__":
    main()