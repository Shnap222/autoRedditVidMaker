from abc import ABC, abstractmethod

import tempfile


class IMovieMaker(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def combine_numbered_images_and_audios(self, images_path, audios_path) -> str:
        pass

    @abstractmethod
    def create_movie_with_centered_and_background_clips(self, centered_videos_path: str, bg_video_path: str,
                                                        background_audio: str = "") -> str:
        pass
