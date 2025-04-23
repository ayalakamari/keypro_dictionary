# KeyPro Dictionary Builder

This module is part of the **KeyPro** project – a smart touch-typing training plugin for VSCode.

📚 This component is responsible for managing a dictionary of valid English words used for generating customized typing exercises, based on the student's progress and known letters.

## Features

- Load a large word list from a text file
- Check if a word is a real English word
- Suggest valid words composed only from known letters
- Filter out non-dictionary words from any list

## Usage Example

```python
from dictionary.word_dictionary import WordDictionary

wd = WordDictionary("dictionary/english_words.txt")
print(wd.is_real_word("keyboard"))  # True
print(wd.suggest_words("cat", max_len=5))  # ['act', 'cat', 'at', 'tac', ...]
