from pytube import YouTube

yt=YouTube("https://www.youtube.com/watch?v=-YfzGrt4E90")
#yt=YouTube("https://www.youtube.com/watch?v=CNlQFgPVxN4")

dw=yt.streams.first()
dw.download("C:/eric")
print("Download Completed\n")
