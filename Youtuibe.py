from pytube import YouTube

while True:
    a=input("enter link\n")
    video=YouTube(a)
    videos=video.streams.all()
    st=list(enumerate(videos))
    for i in st:
        print(i)  
    print()
    s=int(input("enter : number of resolution setting you want to download\n"))
    videos[s].download()
    print("****************************SUCCESSFULLY DOWNLOADED*************************")

