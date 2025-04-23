# dictionary/word_dictionary.py

from typing import List, Set


class WordDictionary:
    def __init__(self, path: str = "dictionary/english_words.txt"):
        """טוען את כל המילים מקובץ מילים לקבוצה"""
        with open(path, "r", encoding="utf-8") as f:
            self.words: Set[str] = set(word.strip().lower() for word in f if word.strip())

    def is_real_word(self, word: str) -> bool:
        """בודק אם מילה היא אמיתית (נמצאת במילון)"""
        return word.lower() in self.words

    def get_words_with_only_known_letters(self, known_letters: Set[str], max_len: int = None) -> List[str]:
        """
        מחזיר מילים שניתן להרכיב אך ורק מאותיות שהתלמיד כבר מכיר.
        :param known_letters: קבוצת אותיות שהתלמיד כבר למד
        :param max_len: אורך מקסימלי של מילה (אם קיים)
        :return: רשימת מילים חוקיות מתוך המילון
        """
        results = [
            word for word in self.words
            if set(word).issubset(known_letters)
        ]
        if max_len:
            results = [word for word in results if len(word) <= max_len]
        return results

    def suggest_words(self, allowed_letters: str, max_len: int = 6) -> List[str]:
        """
        מציע מילים לשיעור הבא לפי האותיות שהתלמיד כבר מכיר.
        :param allowed_letters: מחרוזת של אותיות
        :param max_len: אורך מקסימלי של מילה
        :return: רשימת מילים חוקיות
        """
        allowed_set = set(allowed_letters.lower())
        return self.get_words_with_only_known_letters(allowed_set, max_len=max_len)

    def filter_real_words(self, word_list: List[str]) -> List[str]:
        """
        מסנן מילים ומחזיר רק את האמיתיות מתוך המילון.
        :param word_list: רשימת מילים
        :return: רק מילים שקיימות במילון
        """
        return [word for word in word_list if self.is_real_word(word)]
