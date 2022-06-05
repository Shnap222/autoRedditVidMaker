from Abstract import IWordBlacklistConverter
from typing import List
import re


class WordCleaner(IWordBlacklistConverter.IWordBlacklistConvertor):

    def __init__(self, word_dict: dict):
        super().__init__(word_dict)

    def convert_paragraph(self, paragraph: str) -> str:
        paragraph = paragraph.lower()
        cleaned_words = []
        for word in paragraph.split(" "):
            for blacklisted_word in self.word_dict.keys():
                word = word.replace(blacklisted_word, self.word_dict[blacklisted_word]) if not str(
                    re.sub(blacklisted_word, "", word)).isalpha() else word
            cleaned_words.append(word)
        return " ".join(cleaned_words)

    def convert_multiple_paragraphs(self, paragraphs: List[str]) -> List[str]:
        cleaned_paragraphs = []

        for paragraph in paragraphs:
            cleaned_paragraphs.append(self.convert_paragraph(paragraph))
        return cleaned_paragraphs
