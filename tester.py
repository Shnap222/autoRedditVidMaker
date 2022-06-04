from moviepy.editor import *
from moviepy.video.tools.segmenting import findObjects
#
# im = ImageClip(r"C:\Users\smadar.KLAG\Pictures\צילום מסך 2022-05-28 212831.png")
#
# regions = findObjects(im)
#
# clips = [VideoFileClip(n, audio=True).subclip(0, 22) for n in
#          [r'C:\Users\smadar.KLAG\Videos\Free Stock Videos – winter scene snow storm blizzard on black background.mp4',
#           r'C:\Users\smadar.KLAG\AppData\Local\Temp\tmp8qm76yrs\half_made\nig.mp4']]
#
# comp_clips = [c.resize(r.size)
#                   .set_mask(r.mask)
#                   .set_pos(r.screenpos)
#               for c, r in zip(clips, regions)]
#
# cc = CompositeVideoClip(comp_clips, im.size)
# cc.write_videofile("comp.mp4")
import os

from MovieMakers import DefaultMovieMaker

# a = DefaultMovieMaker.DefaultMovieMaker()
#
# temp_file = r'C:\Users\smadar.KLAG\AppData\Local\Temp\tmpdpdfgb77'
#
# audio_path = os.path.join(temp_file,'audio')
# image_path = os.path.join(temp_file,'images')
#
# # a.create_movie_from_images_and_audios(audios_path=audio_path,images_path=image_path,output_path='asd')
#
# a.create_video_using_multiple_cuts(cut_directory=r'C:\Users\smadar.KLAG\AppData\Local\Temp\tmp8qm76yrs\half_made',output_path=r'C:\Users\smadar.KLAG\AppData\Local\Temp\tmp8qm76yrs\half_made\nig.mp4')

cool = AudioFileClip(r'C:\Users\smadar.KLAG\Downloads\LAKEY_INSPIRED_-_Better_Days_(getmp3.pro).mp3').subclip(0,6)
inner_video = VideoFileClip(r'C:\Users\smadar.KLAG\AppData\Local\Temp\tmplnvag06u\half_made\thankgod.mp4').subclip(0, 6)
video = VideoFileClip(r'C:\Users\smadar.KLAG\Downloads\Free To Use Gameplay (No Copyright) - Minecraft Parkour.mp4',
                      audio=True).subclip(2, 8)


video = video.set_audio(cool)

video = video.volumex(0.05)

inner_video = inner_video.resize(1.50)

inner_video = inner_video.resize(width=inner_video.w - 100)
video_resized = video.resize(height=1920)
video_resized = video_resized.crop(x1=1166.6, y1=0, x2=2246.6, y2=1920)

final = CompositeVideoClip([video_resized, inner_video.set_position(('center', 0.55),relative=True),])
final.write_videofile('test.mp4')
