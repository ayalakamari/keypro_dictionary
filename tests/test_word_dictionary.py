from dictionary.word_dictionary import WordDictionary


def test_is_real_word():
    wd = WordDictionary("dictionary/english_words.txt")
    assert wd.is_real_word("cat") is True
    assert wd.is_real_word("xyzzy") is False


def test_get_words_with_only_known_letters():
    wd = WordDictionary("dictionary/english_words.txt")
    letters = set("cat")
    results = wd.get_words_with_only_known_letters(letters)
    assert all(set(word).issubset(letters) for word in results)


def test_suggest_words():
    wd = WordDictionary("dictionary/english_words.txt")
    results = wd.suggest_words("cat", max_len=3)
    assert all(set(word).issubset(set("cat")) for word in results)
    assert all(len(word) <= 3 for word in results)


def test_filter_real_words():
    wd = WordDictionary("dictionary/english_words.txt")
    test_list = ["cat", "dog", "qwerty"]
    result = wd.filter_real_words(test_list)
    assert "cat" in result or "dog" in result
    assert "qwerty" not in result
