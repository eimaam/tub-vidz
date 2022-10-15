from asyncio import streams
from fileinput import filename
from nturl2path import url2pathname
from django.shortcuts import render, redirect
from django.conf import settings
from pytube import YouTube
import ffmpeg
import os

# Create your views here.
def ytbVidHome(request):
    if request.method == "POST":
        global link
        link = request.POST['ytlink']
        obj = YouTube(link)
        resolutions = []
        streams_all = obj.streams
        for stream in streams_all:
            resolutions.append(stream.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = link.replace("watch?v=", "embed/")
        return redirect('Download')
    return render(request, 'index.html')

def ytbVidDownloader(request):
    if request.method == "POST":
        return redirect("DownloadDone")
    else:
        global link
        obj = YouTube(link)
        resolutions = []
        streams_all = obj.streams
        for stream in streams_all:
            resolutions.append(stream.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = link.replace("watch?v=", "embed/")
        context = {"vid":obj, "embd":embed_link, "resl":resolutions}
        return render(request, 'download.html', context)
    


def ytbVidDownloadDone(request):
    global link
    embed_link = link.replace("watch?v=", "embed/")
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    download = YouTube(link).streams.get_highest_resolution().download(dirs)
    if download:
        return render(request, 'done.html', {'embd':embed_link})
    else:
        return render(request, 'error.html')

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