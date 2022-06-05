from abc import ABC, abstractmethod

from typing import List


class IWordBlacklistConvertor(ABC):

    def __init__(self, word_dict: dict):
        self.word_dict = word_dict

    @abstractmethod
    def convert_paragraph(self, pharagraph: str) -> str:
        pass

    @abstractmethod
    def convert_multiple_paragraphs(self, paragraphs: List[str]) -> List[str]:
        pass
