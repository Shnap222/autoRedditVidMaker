import moviepy
from moviepy.editor import AudioFileClip, ImageClip, VideoFileClip, concatenate_videoclips, CompositeVideoClip
import tempfile
import os
import time


class DefaultMovieMaker:

    def __init__(self):
        pass

    def create_movie_from_images_and_audios(self, audios_path: str, images_path: str, output_path: str = "") -> str:

        if not output_path:
            tempdir = tempfile.TemporaryDirectory()

            output_path = os.path.join(tempdir.name, 'half_made')
            os.mkdir(output_path)

        audio_files = sorted(os.listdir(audios_path), key=lambda file_name: int(file_name.split('.')[0]))
        image_files = sorted(os.listdir(images_path), key=lambda file_name: int(file_name.split('.')[0]))

        for pos in range(len(audio_files)):
            self.add_static_image_to_audio(image_path=os.path.join(images_path, image_files[pos]),
                                           audio_path=os.path.join(audios_path, audio_files[pos]),
                                           output_path=os.path.join(output_path, f'{pos}.mp4'))
        print('made movies')

        return output_path

        # self.create_video_using_multiple_cuts(half_made_path, output_path)

    def add_static_image_to_audio(self, image_path: str, audio_path: str, output_path: str):
        """Create and save a video file to `output_path` after
        combining a static image that is located in `image_path`
        with an audio file in `audio_path`"""
        # create the audio clip object
        audio_clip = AudioFileClip(audio_path)
        # create the image clip object
        image_clip = ImageClip(image_path)
        # use set_audio method from image clip to combine the audio with the image
        video_clip = image_clip.set_audio(audio_clip)
        # specify the duration of the new clip to be the duration of the audio clip
        video_clip.duration = audio_clip.duration
        # set the FPS to 1
        video_clip.fps = 1
        # write the resuling video clip
        video_clip.write_videofile(output_path)

    def create_video_using_multiple_cuts(self, cut_directory: str, output_path: str):
        clips = [VideoFileClip(os.path.join(cut_directory, file_path), ) for file_path in
                 sorted(os.listdir(cut_directory), key=lambda file: int(file.split('.')[0]))]

        print("finished processing")

        final = concatenate_videoclips(clips, method='compose')

        print("finished combining them")

        final.write_videofile(output_path)

    def create_video_with_background_video(self, bg_video_path: str, centered_videos_path: str,
                                           output_path: str, bg_audio_path: str = ""):
        centered_videos_files = sorted(os.listdir(centered_videos_path),
                                       key=lambda file_name: int(file_name.split('.')[0]))
        videos_list = []
        calc_duration = 0
        for video in centered_videos_files:
            video = VideoFileClip(os.path.join(centered_videos_path, video))
            video = video.set_start(calc_duration)
            video = video.resize(1.50)
            video = video.resize(width=video.w - 100)
            calc_duration += video.duration
            videos_list.append(video.set_position(('center', 0.55), relative=True))

        print("finished setting up videos")

        # audio = AudioFileClip(bg_audio_path).subclip(0, inner_video.duration + 1)
        bg_video = VideoFileClip(bg_video_path, audio=False).subclip(10, calc_duration + 11)

        # bg_video = bg_video.set_audio(audio)

        # bg_video = bg_video.volumex(0.05)

        bg_video_resized = bg_video.resize(height=1920)
        bg_video_resized = bg_video_resized.crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

        videos_list.insert(0, bg_video_resized)

        final = CompositeVideoClip(videos_list)
        final.write_videofile(output_path)
