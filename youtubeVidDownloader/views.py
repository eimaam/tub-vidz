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
        global link
        obj = YouTube(link)
        resolutions = []
        streams_all = obj.streams
        for stream in streams_all:
            resolutions.append(stream.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = link.replace("watch?v=", "embed/")
        return render(request, 'download.html', {object:obj, "embd":embed_link, "resl":resolutions})
    


def ytbVidDownloadDone(request, streams):
    global url
    homedir = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    if request.method == "POST":
        YouTube(url).streams.get_highest_resolution().download(dirs)
        return render(request,)
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