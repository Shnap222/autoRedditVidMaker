from config import *
import tempfile
import os

from Utils import FileUtilities

# ------Consts--------
g_data_grabber = DATA_GRABBER
g_audio_manager = AUDIO_MANAGER
g_movie_maker = MOVIE_MAKER
g_tempdir = ""


def main():
    posts = g_data_grabber.get_posts()

    for post_num, post in enumerate(posts):
        post_process(post, post_num)


def post_process(post, post_num: int):
    post_path = os.path.join(g_tempdir.name, str(post_num))
    images_path = os.path.join(post_path, "images")
    audios_path = os.path.join(post_path, "audios")
    clips_path = os.path.join(post_path, "clips")

    for path in [post_path, images_path, audios_path, clips_path]:
        FileUtilities.mkdir(path)

    _, paragraphs = g_data_grabber.get_post_data(post, images_path)

    for audio_position, paragraph in enumerate(paragraphs):
        g_audio_manager.record_text_to_file(path=os.path.join(audios_path, str(audio_position)), text=paragraph)

    g_movie_maker.create_movie_from_images_and_audios(audios_path=audios_path,
                                                      images_path=images_path,
                                                      output_path=clips_path)

    g_movie_maker.create_video_with_background_video(
        bg_video_path=r'C:\Users\smadar.KLAG\Downloads\Free To Use Gameplay (No Copyright) - Minecraft Parkour.mp4',
        centered_videos_path=clips_path,
        output_path=r"C:\Users\smadar.KLAG\PycharmProjects\FilmEditor\FINAL.mp4"
    )

    input("next?")


if __name__ == '__main__':
    #: Init Processes
    g_data_grabber = DATA_GRABBER()
    g_audio_manager = AUDIO_MANAGER()
    g_movie_maker = MOVIE_MAKER()

    g_tempdir = tempfile.TemporaryDirectory()

    main()
