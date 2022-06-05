from abc import ABC, abstractmethod


class IVideoEditor(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_movie_from_images_and_audios(self, audios_path: str, images_path: str, output_path: str = "") -> str:
        pass

    @abstractmethod
    def create_video_with_background_video(self, bg_video_path: str, centered_videos_path: str,
                                           output_path: str, bg_audio_path: str = "") -> str:
        pass
