import moviepy.editor as mpy

videoquality = "24"

compression = "slow"

vcodec = 'libx264'

loadtitle = 'nameYourLoadingTitle.mp4'
savetitle = 'nameYourSavingTitle.mp4'

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