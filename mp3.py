from moviepy import editor

video = editor.VideoFileClip('francaise.mp4')
video.audio.write_audiofile('francais.mp3')
#mp4_file = "francaise.mp4"
#mp3_file = "francais.mp3"
#videoClip = VideoFileClip(mp4_file)
#audioclip = videoClip.audio
#audioclip.write_audiofile(mp3_file)
#audioclip.close()
#videoClip.close()