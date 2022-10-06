from asyncio import streams
from fileinput import filename
from django.shortcuts import render
from django.conf.global_settings import MEDIA_ROOT, MEDIA_URL
from pytube import YouTube
import ffmpeg

# Create your views here.
def ytbVidHome(request):
    if request.method == "POST":
        link = request.POST['ytlink']
        obj = YouTube(link)
        resolutions = []
        streams_all = obj.streams
        for stream in streams_all:
            resolutions.append(stream.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = link.replace("watch?v=", "embed/")
        print(resolutions)
        return render(request, 'index.html', {'res':resolutions, 'embd':embed_link})
    return render(request, 'index.html')

def ytbVidDownloader(request):
    if request.method == "POST":
        link = request.POST['ytlink']
        resolution = request.POST.get('format', False)
        obj = YouTube(link)
        obj.streams.filter(res=resolution).first().download(filename=MEDIA_ROOT+'vid.mp4')
        obj.streams.filter(abr='160kbps', progressive=False).first().download(filename=MEDIA_ROOT+'aud.mp3')
        vid = ffmpeg.input(MEDIA_ROOT+'vid.mp4')
        aud = ffmpeg.input(MEDIA_ROOT+'aud.mp3')
        filename = MEDIA_ROOT+obj.title +'.mp4'
        ffmpeg.output(aud, vid, filename).run(overwrite_output=True)
        embed_link = link.replace("watch?v=", "embed/")
        stat = "Your Video Is Downloading........"
        # download = vid.first().download()
        # if download:
        #     stat = "Downloaded"
        return render(request, 'download.html', {'res':resolution, 'embd':embed_link, 'status':stat})
    return render(request, 'download.html')


# def ytbVidDownloader(request):
#     if request.method == "POST":
#         link = request.POST['ytlink']
#         format = request.POST['format']
#         obj = YouTube(link)
#         resolutions = []
#         streams_all = obj.streams
#         for stream in streams_all:
#             resolutions.append(stream.resolution)
#         resolutions = list(dict.fromkeys(resolutions))
#         embed_link = link.replace("watch?v=", "embed/")
#         resolution = [res for res in resolutions if res == format]
#         print(resolutions)
#         return render(request, 'download.html', {'res':resolutio, 'embd':embed_link})
#     return render(request, 'index.html')