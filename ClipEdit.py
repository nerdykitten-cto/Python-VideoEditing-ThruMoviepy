# The Modules
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# The Variables
# The Cut timings
cuts = ['startTime', 'endTime']
# The Files
loadtitle = 'nameYourLoadingVideo.mp4'
savetitle = 'nameYourSavingVideo.mp4'

ffmpeg_extract_subclip(loadtitle, cuts[0], cuts[1], savetitle)