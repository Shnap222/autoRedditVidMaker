from AudioManagers import DefaultAudioManager

from MovieMakers import DefaultMovieMaker

from SeleniumGrabber import SeleniumGrabber, AskRedditSeleniumGrabber

from Word_Cleaner import WordCleaner

import os

# DATA_GRABBER = SeleniumGrabber.SeleniumGraber
#
DATA_GRABBER = AskRedditSeleniumGrabber.AskRedditSeleniumGrabber

AUDIO_MANAGER = DefaultAudioManager.DefaultAudioManager

MOVIE_MAKER = DefaultMovieMaker.DefaultMovieMaker

BLACKLIST_CONVERTOR = WordCleaner.WordCleaner

BACKGROUND_VIDEOS_PATH = os.path.join(os.path.dirname(__file__), "background videos")

BLACKLISTED_WORDS = {
    "aita": "am i the asshole",
    "nigga": "black guy",
    "sex": "fun time",
    "vagina": "lady private part",
    "dick": "guy private part",
    "kill": "game over",
    "nigger": "black guy",
    "died": "game over",
    "dead": "game over",
    'die': "game over"
}

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "Finished_Product")
