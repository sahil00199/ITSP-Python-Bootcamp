import pafy

song = pafy.new("https://www.youtube.com/watch?v=d7C6W4kY-KQ")#Sample url taken. Try with your own!
#path = "/Users/Sarthak/Desktop" To download to specific path and pass it as a argument to the download function. 
#By default it is downloaded in the current working directory.
gaana = ""
songStreams = song.videostreams
mp4 =[]
for s in songStreams:
	if s.extension == 'mp4':
		gaana = s
		break
gaana.download()
audio = song.getbestaudio
audio.download()