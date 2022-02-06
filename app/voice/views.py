from pathlib import Path
import os

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import sys
#sys.path.append('./../../../speech_to_text/')
sys.path.append('./../speech_to_text/')
from Audio_into_Words import test, split_audio_transcript_to_words

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./../speech_to_text/cred.json"
abspath = os.path.abspath(os.path.join('.'))
from .forms import UploadForm, ConvertForm

def convert(request):
    if request.method == 'POST':
        form = ConvertForm(request.POST)
        if form.is_valid():
            print("trigger conversion")
            # TODO: convert
            return render(request, 'voice/home.html', {'form': form, "file_1":"", "file_2":""})
    else:
        form = UploadForm()
    return render(request, 'voice/home.html', {'form': form, "file_1":"", "file_2":""})

def uploaded(request):
    base_url_1 = ""
    base_url_2 = ""
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            song_text = form.cleaned_data['song']
            url_2 = form.cleaned_data['speech']
            
            # TODO: do something with song text
            # base_url_1 = './../../../media/' + url_1
            base_url_2 = './../../../media/' + url_2
            # print(base_url_1)
            print('=============')
            temp_path = abspath + '/app/media/'+url_2
            print(temp_path)
            split_audio_transcript_to_words(temp_path, cleandir=True)
            return render(request, 'voice/home.html', {'form': form, "file_2":base_url_2})
    else:
        form = UploadForm()
    return render(request, 'voice/home.html', {'form': form, "file_1":base_url_1, "file_2":base_url_2})

def home(request):
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = UploadForm()

    return render(request, 'voice/home.html', {'form': form})