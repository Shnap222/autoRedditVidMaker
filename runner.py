from config import *
import tempfile
import os
import random
import hashlib

from Utils import FileUtilities

# ------Consts--------
g_data_grabber = DATA_GRABBER
g_audio_manager = AUDIO_MANAGER
g_movie_maker = MOVIE_MAKER
g_word_cleaner = BLACKLIST_CONVERTOR
g_tempdir = ""


def main():
    posts = g_data_grabber.get_posts()

    for post_num, post in enumerate(posts):
        try:
            post_process(post, post_num)
        except Exception as e:
            print(e)


def post_process(post, post_num: int):
    post_path = os.path.join(g_tempdir.name, str(post_num))
    images_path = os.path.join(post_path, "images")
    audios_path = os.path.join(post_path, "audios")
    clips_path = os.path.join(post_path, "clips")

    for path in [post_path, images_path, audios_path, clips_path]:
        FileUtilities.mkdir(path)

    _, paragraphs = g_data_grabber.get_post_data(post, images_path)

    if FileUtilities.check_if_name_exists_in_dir(OUTPUT_PATH, hashlib.sha256(paragraphs[0].encode()).hexdigest(),
                                                 'mp4'):
        print("Already Exits - ", paragraphs[0])
        print(hashlib.sha256(paragraphs[0].encode()).hexdigest())
        return

    for audio_position, paragraph in enumerate(paragraphs):
        paragraph = g_word_cleaner.convert_paragraph(paragraph)
        g_audio_manager.record_text_to_file(path=os.path.join(audios_path, str(audio_position)), text=paragraph)

    g_movie_maker.create_movie_from_images_and_audios(audios_path=audios_path,
                                                      images_path=images_path,
                                                      output_path=clips_path)

    bg_video = choose_random_bg_video(BACKGROUND_VIDEOS_PATH)

    g_movie_maker.create_video_with_background_video(
        bg_video_path=bg_video,
        centered_videos_path=clips_path,
        output_path=os.path.join(OUTPUT_PATH, f"{hashlib.sha256(paragraphs[0].encode()).hexdigest()}.mp4")
    )

    input("next?")


def choose_random_bg_video(bg_path: str):
    return os.path.join(bg_path, random.choice(os.listdir(bg_path)))


if __name__ == '__main__':
    #: Init Processes
    g_data_grabber = DATA_GRABBER()
    g_audio_manager = AUDIO_MANAGER()
    g_movie_maker = MOVIE_MAKER()
    g_word_cleaner = BLACKLIST_CONVERTOR(BLACKLISTED_WORDS)

    g_tempdir = tempfile.TemporaryDirectory()

    main()
