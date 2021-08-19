# 

# The Modules
import moviepy.editor as mpy
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# The Variables
# The Encoders
vcodec =   "libx264"
aucodec = "libvorbis"

# The Video Quality (Not to confused with the video framerate)
videoquality = "24"

# Compression: ultrafast, superfast, veryfast, faster, fast, medium, slow, slower, veryslow
compression = "slow"

# Music and Video Files
# Music Side
musicAfile = 'testMusicOG.mp3'
loadAtitle = 'TestVideoOG.mp4'
saveAtitle = 'AudioEdited.mp4'
# Text Side
loadTtitle = saveAtitle
saveTtitle = 'AudioandTextEdited.mp4'
# Cutting Side
loadVctitle = saveTtitle
# Final Side
savetitleEnd = 'Copyrighted.mp4'

# modify the Start and End times for your subclips
cuts = [00.00, 13.00]

# Now the Editing
# Step 1:- The Audio Editing
def audio_edit(loadtitle, musicfile, savetitle):
    video = mpy.VideoFileClip(loadtitle)
    audio_back = mpy.AudioFileClip(musicfile)
    final_clip = video.set_audio(audio_back)

    final_clip.write_videofile(savetitle, codec = 'libx264', audio_codec = aucodec)

# Step 2:- The TextEditing Part
def text_edit(loadtitle, savetitle):
    # load file
    videoText = mpy.VideoFileClip(loadtitle)

    # Adding Copyright Text
    copyrightTxt = mpy.TextClip('Copyright: Syed Ali Azhar', font='Courier',
                       fontsize=30, color='black', bg_color='transparent')
    copyrightTxt = copyrightTxt.set_position(('left', 0), relative=True)
    copyrightTxt = copyrightTxt.set_start((0, 1)) # (min, s)
    copyrightTxt = copyrightTxt.set_duration(12)
    copyrightTxt = copyrightTxt.crossfadein(0.5)
    copyrightTxt = copyrightTxt.crossfadeout(0.5)
    # Adding Introduction Text
    introText = mpy.TextClip('Hi, the Name is Syed Ali Azhar', font='Courier',
                        fontsize=100, color='white', bg_color='gray35')
    introText = introText.set_position(('center', 0), relative=True)
    introText = introText.set_start((0, 2))
    introText = introText.set_duration(2)
    introText = introText.crossfadein(0.5)
    introText = introText.crossfadeout(0.5)

    final_clip = mpy.CompositeVideoClip([videoText, copyrightTxt, introText])

    # save file
    final_clip.write_videofile(savetitle, threads=4, fps=24,
                               codec=vcodec,
                               preset=compression,
                               ffmpeg_params=["-crf",videoquality])

    videoText.close()

# Step 3:- The Cutting of the Video
def cut_video(loadtitle, savetitle):
    ffmpeg_extract_subclip(loadtitle, cuts[0], cuts[1], savetitle)

# if __name__ == '__main__': run video_edit and audio_edit
if __name__ == '__main__':
    audio_edit(loadAtitle, musicAfile, saveAtitle)
    text_edit(loadTtitle, saveTtitle)
    cut_video(loadVctitle, savetitleEnd)
    