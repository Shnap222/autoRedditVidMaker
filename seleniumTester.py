from SeleniumGrabber import SeleniumGrabber


a = SeleniumGrabber.SeleniumGraber("https://www.reddit.com/r/AmItheAsshole/","C:\Program Files (x86)\chromedriver102.exe")
a.get_images_and_voice()