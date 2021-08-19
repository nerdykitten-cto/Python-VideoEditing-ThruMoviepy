# The Modules
import moviepy.editor as mpy

# Variables
# Encoder
aucodec = "libvorbis"
vcodec = 'libx264'
# The Files
loadtitle = 'nameYourLoadingTitle.mp4'
musicfile = 'nameYourMusicFile.mp3'
savetitle = 'nameYourSavingTitle.mp4'

# Adding Music
video = mpy.VideoFileClip(loadtitle)
audio_back = mpy.AudioFileClip(musicfile)
final_clip = video.set_audio(audio_back)

# The Code
final_clip.write_videofile(savetitle, codec = vcodec, audio_codec = aucodec)

