from abc import ABC, abstractmethod
from typing import Tuple, List


class IDataGatherer(ABC):

    def __init__(self, posts_amount: int = 0):
        self.posts_amount = posts_amount

    @abstractmethod
    def get_posts(self):
        pass

    @abstractmethod
    def get_post_data(self, post, output_dir_path: str) -> Tuple[str, List]:
        pass
