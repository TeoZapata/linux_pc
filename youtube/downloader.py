from pytube import YouTube


def download():

    while True:
        try:
            url = input("please insert url youtube to download : ")
            if url=="exit": break
            link = YouTube(url)
            print("wait....")
            stream  = link.streams.get_audio_only()
            stream.download()
            break
        except:
            print("there is a problem with url youtube")
    
    print("done!")
    

download()



    